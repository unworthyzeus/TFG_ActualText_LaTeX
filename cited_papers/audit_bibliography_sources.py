import csv
import importlib.util
import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
BIB_HELPER = ROOT / "build_citation_audit_data.py"
OUT = ROOT / "bibliography_source_audit.json"
MANIFEST = ROOT / "download_manifest.csv"


spec = importlib.util.spec_from_file_location("audit_helper", BIB_HELPER)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def read_manifest() -> dict[str, dict]:
    with MANIFEST.open(newline="", encoding="utf-8-sig") as handle:
        return {row["key"]: row for row in csv.DictReader(handle)}


def count_pdf_pages(path: str) -> int | None:
    if not path:
        return None
    p = Path(path)
    if not p.is_file() or p.suffix.lower() != ".pdf":
        return None
    try:
        return len(PdfReader(str(p)).pages)
    except Exception:
        return None


def first_page_hint(path: str) -> str:
    if not path:
        return ""
    p = Path(path)
    if not p.is_file() or p.suffix.lower() != ".pdf":
        return ""
    try:
        reader = PdfReader(str(p))
        text = reader.pages[0].extract_text() or ""
        text = re.sub(r"\s+", " ", text).strip()
        return text[:600]
    except Exception:
        return ""


def crossref_by_doi(doi: str) -> dict:
    if not doi:
        return {}
    cache_dir = ROOT / ".metadata_cache" / "crossref"
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path = cache_dir / (re.sub(r"[^A-Za-z0-9._-]+", "_", doi.lower()) + ".json")
    if cache_path.exists():
        return json.loads(cache_path.read_text(encoding="utf-8"))
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
        msg = data.get("message", {})
    except Exception as exc:
        msg = {"_error": str(exc)}
    cache_path.write_text(json.dumps(msg, indent=2, ensure_ascii=False), encoding="utf-8")
    time.sleep(0.12)
    return msg


def openalex_by_title(title: str) -> dict:
    if not title:
        return {}
    cache_dir = ROOT / ".metadata_cache" / "openalex"
    cache_dir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^A-Za-z0-9._-]+", "_", title.lower())[:120]
    cache_path = cache_dir / f"{slug}.json"
    if cache_path.exists():
        cached = json.loads(cache_path.read_text(encoding="utf-8"))
        if isinstance(cached, list):
            return cached[0] if cached else {}
        return cached
    url = "https://api.openalex.org/works?per-page=3&search=" + urllib.parse.quote(title)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            data = json.loads(response.read().decode("utf-8"))
        results = data.get("results", [])
    except Exception as exc:
        results = [{"_error": str(exc)}]
    cache_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    time.sleep(0.12)
    return results[0] if results else {}


def normalize_pages(value: str | None) -> str:
    value = (value or "").strip()
    value = value.replace("--", "-").replace("–", "-")
    return re.sub(r"\s+", "", value)


def main() -> None:
    bib = helper.parse_bib(helper.BIB_PATH.read_text(encoding="utf-8"))
    keys = helper.active_order_from_aux()
    manifest = read_manifest()
    rows = []
    for number, key in enumerate(keys, start=1):
        entry = bib[key]
        fields = entry["fields"]
        current_pages = normalize_pages(fields.get("pages", ""))
        doi = fields.get("doi", "")
        crossref = crossref_by_doi(doi)
        openalex = openalex_by_title(fields.get("title", "")) if not doi else {}
        manifest_row = manifest.get(key, {})
        file_path = manifest_row.get("file", "")
        pdf_pages = count_pdf_pages(file_path)
        crossref_pages = normalize_pages(crossref.get("page", ""))
        openalex_biblio = openalex.get("biblio") or {}
        openalex_pages = ""
        if openalex_biblio.get("first_page") and openalex_biblio.get("last_page"):
            openalex_pages = normalize_pages(f"{openalex_biblio.get('first_page')}-{openalex_biblio.get('last_page')}")
        elif openalex_biblio.get("first_page"):
            openalex_pages = normalize_pages(str(openalex_biblio.get("first_page")))
        rows.append(
            {
                "number": number,
                "key": key,
                "entry_type": entry["type"],
                "title": fields.get("title", ""),
                "authors": fields.get("author", ""),
                "year": fields.get("year", "") or fields.get("date", "")[:4],
                "doi": doi,
                "url": fields.get("url", ""),
                "current_pages": current_pages,
                "current_eid": fields.get("eid", ""),
                "crossref_title": " ".join(crossref.get("title", [])) if isinstance(crossref.get("title"), list) else "",
                "crossref_container": " ".join(crossref.get("container-title", [])) if isinstance(crossref.get("container-title"), list) else "",
                "crossref_pages": crossref_pages,
                "crossref_doi": crossref.get("DOI", ""),
                "crossref_error": crossref.get("_error", ""),
                "openalex_doi": openalex.get("doi", ""),
                "openalex_pages": openalex_pages,
                "openalex_first_page": openalex_biblio.get("first_page", ""),
                "openalex_title": openalex.get("title", ""),
                "manifest_status": manifest_row.get("status", ""),
                "file": file_path,
                "pdf_pages": pdf_pages,
                "first_page_hint": first_page_hint(file_path),
            }
        )
    OUT.write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"rows": len(rows), "out": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
