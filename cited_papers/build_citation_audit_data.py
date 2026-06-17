import csv
import json
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(r"C:\TFG")
THESIS = ROOT / "FINAL_THESIS" / "reduced" / "TFG"
BIB_PATH = THESIS / "TFG.bib"
AUX_PATH = THESIS / "TFG.aux"
PDF_PATH = THESIS / "TFG.pdf"
PAPERS_DIR = ROOT / "FINAL_THESIS" / "cited_papers"
MANIFEST_PATH = PAPERS_DIR / "download_manifest.csv"
SUPPORT_PATH = PAPERS_DIR / "citation_support_assessment.json"
OUT_JSON = PAPERS_DIR / "citation_audit_rows.json"
OUT_CSV = PAPERS_DIR / "citation_audit.csv"


def clean_latex(text: str) -> str:
    replacements = {
        r"\&": "&",
        r"\_": "_",
        r"\%": "%",
        r"\c{C}": "C",
        r"\u{g}": "g",
        r'\\"{u}': "u",
        r"\"{u}": "u",
        r"\'{e}": "é",
        r"\'{i}": "í",
        r"\'{a}": "á",
        r"\'{o}": "ó",
        r"\'{u}": "ú",
        r"\~{n}": "ñ",
        r"{\o}": "o",
        r"\o": "o",
        r"\aa": "a",
        r"\AE": "AE",
        r"\bibrangedash": "-",
        "--": "-",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"\\[A-Za-z]+\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z]+", "", text)
    text = text.replace("{", "").replace("}", "")
    return re.sub(r"\s+", " ", text).strip()


def parse_bib(text: str) -> dict:
    entries = {}
    i = 0
    while True:
        at = text.find("@", i)
        if at == -1:
            break
        match = re.match(r"@([A-Za-z]+)\s*\{", text[at:])
        if not match:
            i = at + 1
            continue
        entry_type = match.group(1).lower()
        start = at + match.end()
        depth = 1
        j = start
        while j < len(text) and depth:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        body = text[start : j - 1]
        comma = body.find(",")
        if comma == -1:
            i = j
            continue
        key = body[:comma].strip()
        entries[key] = {"type": entry_type, "fields": parse_fields(body[comma + 1 :])}
        i = j
    return entries


def parse_fields(text: str) -> dict:
    fields = {}
    i = 0
    n = len(text)
    while i < n:
        while i < n and (text[i].isspace() or text[i] == ","):
            i += 1
        match = re.match(r"([A-Za-z][A-Za-z0-9_\-]*)\s*=", text[i:])
        if not match:
            i += 1
            continue
        name = match.group(1).lower()
        i += match.end()
        while i < n and text[i].isspace():
            i += 1
        if i >= n:
            break
        if text[i] == "{":
            i += 1
            start = i
            depth = 1
            while i < n and depth:
                if text[i] == "{":
                    depth += 1
                elif text[i] == "}":
                    depth -= 1
                i += 1
            value = text[start : i - 1]
        elif text[i] == '"':
            i += 1
            start = i
            while i < n and text[i] != '"':
                i += 1
            value = text[start:i]
            if i < n:
                i += 1
        else:
            start = i
            while i < n and text[i] not in ",\n":
                i += 1
            value = text[start:i].strip()
        fields[name] = clean_latex(value)
    return fields


def active_order_from_aux() -> list:
    text = AUX_PATH.read_text(encoding="utf-8", errors="ignore")
    keys = []
    seen = set()
    for key in re.findall(r"\\abx@aux@cite\{[^}]*\}\{([^}]+)\}", text):
        if key not in seen:
            seen.add(key)
            keys.append(key)
    return keys


def read_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {}
    with MANIFEST_PATH.open(newline="", encoding="utf-8-sig") as handle:
        return {row["key"]: row for row in csv.DictReader(handle)}


def read_support_assessment() -> dict:
    if not SUPPORT_PATH.exists():
        return {}
    items = json.loads(SUPPORT_PATH.read_text(encoding="utf-8"))
    return {item["key"]: item for item in items}


def count_pdf_pages(path: Path) -> int | None:
    try:
        return len(PdfReader(str(path)).pages)
    except Exception:
        return None


def source_page_count_from_manifest(key: str, manifest: dict) -> int | None:
    row = manifest.get(key)
    if not row:
        return None
    file_value = row.get("file") or ""
    if not file_value:
        return None
    path = Path(file_value)
    if path.is_file() and path.suffix.lower() == ".pdf":
        return count_pdf_pages(path)
    if path.is_dir():
        extracted = path / "extracted"
        if extracted.exists():
            total = 0
            found = False
            for pdf in extracted.glob("*.pdf"):
                pages = count_pdf_pages(pdf)
                if pages:
                    total += pages
                    found = True
            return total if found else None
    return None


def page_count_from_range(pages: str) -> int | None:
    if not pages:
        return None
    match = re.match(r"^\s*(\d+)\s*[-–]\s*(\d+)\s*$", pages)
    if match:
        start, end = int(match.group(1)), int(match.group(2))
        if end >= start:
            return end - start + 1
    return None


def citation_pages_by_number(max_number: int) -> dict[int, list[int]]:
    reader = PdfReader(str(PDF_PATH))
    refs_start = len(reader.pages)
    for idx, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        if re.search(r"(^|\n)\s*References\s*($|\n)", text):
            refs_start = idx
            break

    pages = {n: [] for n in range(1, max_number + 1)}
    bracket_re = re.compile(r"\[([0-9][0-9,\s\-–]*)\]")
    for idx in range(refs_start):
        text = reader.pages[idx].extract_text() or ""
        for group in bracket_re.findall(text):
            numbers = expand_numeric_group(group)
            for number in numbers:
                if 1 <= number <= max_number and (idx + 1) not in pages[number]:
                    pages[number].append(idx + 1)
    return pages


def expand_numeric_group(group: str) -> list[int]:
    values = []
    for part in re.split(r"\s*,\s*", group.strip()):
        if not part:
            continue
        range_match = re.match(r"^(\d+)\s*[-–]\s*(\d+)$", part)
        if range_match:
            start, end = int(range_match.group(1)), int(range_match.group(2))
            if 0 < start <= end <= 200:
                values.extend(range(start, end + 1))
        elif part.strip().isdigit():
            values.append(int(part.strip()))
    return values


def classify_entry(entry_type: str, fields: dict) -> str:
    how = fields.get("howpublished", "").lower()
    title = fields.get("title", "")
    if entry_type == "article":
        return "Journal article"
    if entry_type == "inproceedings":
        return "Conference paper"
    if entry_type == "misc" and "arxiv" in how:
        return "arXiv preprint"
    if entry_type == "misc" and "dataset" in how:
        return "Dataset"
    if entry_type == "online":
        return "Website"
    if entry_type == "book":
        return "Book"
    if entry_type == "techreport" or entry_type == "report":
        if "3GPP" in title or fields.get("institution", "").lower().startswith("3rd generation"):
            return "Standard / technical report"
        return "Technical report"
    if "github" in fields.get("publisher", "").lower() or "repository" in how:
        return "Software / repository"
    return entry_type.title()


def scan_tex_contexts(active_keys: set[str]) -> dict[str, list[dict]]:
    contexts = {key: [] for key in active_keys}
    tex_files = [
        path
        for path in THESIS.glob("*.tex")
        if not path.name.startswith("styles") and "Internal_Documentation" not in str(path)
    ]
    cite_re = re.compile(
        r"\\(?:cite|parencite|textcite|autocite|footcite|supercite|citeauthor|citeyear|bstctlcite)"
        r"(?:\[[^\]]*\])*"
        r"\{([^}]+)\}"
    )
    section_re = re.compile(r"\\(?:chapter|section|subsection|subsubsection|paragraph)\*?\{([^}]*)\}")
    for path in tex_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        section_spans = [(m.start(), clean_latex(m.group(1))) for m in section_re.finditer(text)]
        for match in cite_re.finditer(text):
            keys = [key.strip() for key in match.group(1).split(",")]
            section = current_section(section_spans, match.start())
            snippet = clean_snippet(text[max(0, match.start() - 240) : min(len(text), match.end() + 260)])
            for key in keys:
                if key in contexts and len(contexts[key]) < 4:
                    contexts[key].append(
                        {
                            "file": path.name,
                            "section": section,
                            "snippet": snippet,
                        }
                    )
    return contexts


def current_section(section_spans: list[tuple[int, str]], position: int) -> str:
    current = ""
    for start, title in section_spans:
        if start <= position:
            current = title
        else:
            break
    return current


def clean_snippet(snippet: str) -> str:
    snippet = re.sub(r"%.*", " ", snippet)
    snippet = re.sub(r"\\(?:cite|parencite|textcite|autocite|footcite|supercite|citeauthor|citeyear)(?:\[[^\]]*\])*\{[^}]+\}", " [citation] ", snippet)
    snippet = clean_latex(snippet)
    return snippet[:360].strip()


def cited_for_text(contexts: list[dict]) -> str:
    if not contexts:
        return ""
    sections = []
    for ctx in contexts:
        label = ctx["section"] or ctx["file"]
        if label and label not in sections:
            sections.append(label)
    first = contexts[0]["snippet"]
    section_text = "; ".join(sections[:3])
    if first:
        return f"{section_text}. Context: {first}"
    return section_text


def format_pages(values: list[int]) -> str:
    if not values:
        return ""
    values = sorted(set(values))
    ranges = []
    start = prev = values[0]
    for value in values[1:]:
        if value == prev + 1:
            prev = value
            continue
        ranges.append((start, prev))
        start = prev = value
    ranges.append((start, prev))
    return ", ".join(str(a) if a == b else f"{a}-{b}" for a, b in ranges)


def main() -> None:
    bib = parse_bib(BIB_PATH.read_text(encoding="utf-8"))
    active_keys = active_order_from_aux()
    manifest = read_manifest()
    support = read_support_assessment()
    thesis_pages = citation_pages_by_number(len(active_keys))
    contexts = scan_tex_contexts(set(active_keys))

    rows = []
    for number, key in enumerate(active_keys, start=1):
        entry = bib.get(key, {"type": "", "fields": {}})
        fields = entry["fields"]
        pages = fields.get("pages", "")
        source_page_count = source_page_count_from_manifest(key, manifest)
        range_page_count = page_count_from_range(pages)
        total_pages = range_page_count or source_page_count or ""
        support_row = support.get(key, {})
        rows.append(
            {
                "Number of citation": number,
                "Name of citation": fields.get("title", key),
                "what is it": classify_entry(entry.get("type", ""), fields),
                "which pages are cited?": pages,
                "total number of pages": total_pages,
                "actual pages cited": format_pages(thesis_pages.get(number, [])),
                "what is it cited for": cited_for_text(contexts.get(key, [])),
                "qué se cita exactamente de esta fuente": support_row.get("cited_info", ""),
                "is the cited information in the source?": support_row.get("status", ""),
                "support evidence / caveat": support_row.get("evidence", ""),
                "audit action": support_row.get("action", ""),
                "_key": key,
            }
        )

    OUT_JSON.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    with OUT_CSV.open("w", newline="", encoding="utf-8-sig") as handle:
        fieldnames = [
            "Number of citation",
            "Name of citation",
            "what is it",
            "which pages are cited?",
            "total number of pages",
            "actual pages cited",
            "what is it cited for",
            "qué se cita exactamente de esta fuente",
            "is the cited information in the source?",
            "support evidence / caveat",
            "audit action",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in fieldnames})

    print(json.dumps({"rows": len(rows), "json": str(OUT_JSON), "csv": str(OUT_CSV)}, indent=2))


if __name__ == "__main__":
    main()
