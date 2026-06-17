import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AUDIT_ROWS = json.loads((ROOT / "citation_audit_rows.json").read_text(encoding="utf-8"))
SOURCE_ROWS = {
    row["key"]: row
    for row in json.loads((ROOT / "bibliography_source_audit.json").read_text(encoding="utf-8"))
}
SUPPORT_ROWS = {
    row["key"]: row
    for row in json.loads((ROOT / "citation_support_assessment.json").read_text(encoding="utf-8"))
}
OUT = ROOT / "citation_corrections_report.md"


CHANGES = {
    "vinogradov2026shadow": [
        "Added `pages = {1--6}` from Crossref DOI metadata.",
        "Added canonical DOI URL `https://doi.org/10.1109/ICNC68183.2026.11416865`.",
    ],
    "winner2": [
        "Added `pages = {1--82}` from the local report first page, which states `Page 1 (82)` and total number of pages 82.",
    ],
    "isola2017pix2pix": [
        "Changed `pages = {1125--1134}` to `pages = {5967--5976}` using IEEE/CVPR DOI metadata.",
        "Added DOI `10.1109/CVPR.2017.632`.",
    ],
    "kendall2017uncertainties": [
        "Added `pages = {5574--5584}` using NeurIPS/University of Oxford bibliographic metadata.",
    ],
    "perez2018film": [
        "Added `pages = {3942--3951}` using AAAI/ACM bibliographic metadata.",
    ],
    "izmailov2018swa": [
        "Added `pages = {876--885}` using UAI bibliographic metadata.",
    ],
    "pmnet2023": [
        "Added `pages = {4601--4606}` from Crossref DOI metadata.",
    ],
}


TEXT_CHANGES = {
    "dataset2212": [
        "Added this citation to the RadioUNet paragraph in `state_of_art.tex` as the source for the RadioMapSeer 80 dB path loss range.",
    ],
    "radiounet2020": [
        "Changed the RadioUNet paragraph in `state_of_art.tex` so the 80 dB conversion is attributed to `dataset2212` rather than to RadioUNet alone.",
    ],
    "radiodiff2025": [
        "Changed `obstacle prompts` to `environment features` in `state_of_art.tex`, matching the RadioDiff paper wording.",
    ],
}


SPECIAL_NOTES = {
    "threegpp22125": "No page span added because this is a whole 3GPP specification, not a paper chapter; fuzzy OpenAlex page suggestions were ignored.",
    "tr38901": "No page span added because this is a whole 3GPP technical report; fuzzy OpenAlex page suggestions were ignored.",
    "cost231": "No page span added because the COST 231 source is a multi part final report package rather than one article page range.",
    "rappaport": "No page span added because this is a whole book.",
    "goldsmith": "No page span added because this is a whole book.",
    "indoor2025results": "No page span added because this is a website/results page, not a paper.",
    "izydorczyk2019": "No change in this pass; the record has no DOI in OpenAlex/IEEE metadata, so the corrected IEEE article number, URL, and pages 1--5 were retained.",
}

SPECIAL_BASIS = {
    "threegpp22125": "3GPP specification entry and official URL/identifier",
    "tr38901": "3GPP technical report entry and official URL/identifier",
    "cost231": "local COST 231 report package and extracted report parts",
    "rappaport": "book entry and publisher bibliographic metadata",
    "winner2": "local report PDF first page and local PDF page count: 82",
    "kendall2017uncertainties": "NeurIPS/University of Oxford bibliographic metadata; local PDF page count: 12",
    "perez2018film": "AAAI/ACM bibliographic metadata; Crossref DOI metadata; local PDF page count: 13",
    "izmailov2018swa": "UAI bibliographic metadata; OpenAlex metadata; local PDF page count: 12",
    "indoor2025results": "challenge results website URL",
    "goldsmith": "book DOI and publisher bibliographic metadata",
}


def source_basis(row: dict, source: dict) -> str:
    key = row["_key"]
    if key in SPECIAL_BASIS:
        return SPECIAL_BASIS[key]
    pieces = []
    doi = source.get("doi") or ""
    if source.get("crossref_title"):
        pieces.append("Crossref DOI metadata")
    elif doi.startswith("10.48550/arXiv"):
        pieces.append("arXiv DOI/landing page")
    elif doi.startswith("10.21227"):
        pieces.append("IEEE DataPort DOI landing page")
    elif doi:
        pieces.append("DOI landing page")
    if source.get("openalex_title"):
        pieces.append("OpenAlex metadata")
    if source.get("pdf_pages"):
        pieces.append(f"local PDF page count: {source['pdf_pages']}")
    if source.get("manifest_status"):
        pieces.append(f"manifest status: {source['manifest_status']}")
    return "; ".join(pieces) if pieces else "Local BibTeX and URL/repository check"


def final_fields(row: dict, source: dict) -> str:
    pages = row.get("which pages are cited?") or ""
    total = row.get("total number of pages") or ""
    doi = source.get("doi") or ""
    url = source.get("url") or ""
    parts = []
    parts.append(f"pages: `{pages or 'blank'}`")
    parts.append(f"total pages: `{total or 'blank'}`")
    if doi:
        parts.append(f"doi: `{doi}`")
    if url:
        parts.append(f"url: {url}")
    return "; ".join(parts)


lines = [
    "# Citation Corrections Report",
    "",
    f"Generated: {date.today().isoformat()}",
    "",
    "Scope: 58 final numbered thesis citations. Each entry below records whether I changed the BibTeX, whether the thesis usage is supported by the source, and any thesis wording change made during this support audit.",
    "",
    f"BibTeX changed entries in this pass: {len(CHANGES)}.",
    f"BibTeX no change entries in this pass: {len(AUDIT_ROWS) - len(CHANGES)}.",
    f"Thesis wording/source attribution changes in this pass: {len(TEXT_CHANGES)}.",
    "",
]

for row in AUDIT_ROWS:
    key = row["_key"]
    source = SOURCE_ROWS.get(key, {})
    support = SUPPORT_ROWS.get(key, {})
    number = row["Number of citation"]
    title = row["Name of citation"]
    lines.append(f"## {number}. {title}")
    lines.append("")
    lines.append(f"- Key: `{key}`")
    if key in CHANGES:
        lines.append("- Status: CHANGED")
        for change in CHANGES[key]:
            lines.append(f"- Change: {change}")
    else:
        lines.append("- Status: NO CHANGE")
        note = SPECIAL_NOTES.get(key)
        if note:
            lines.append(f"- Reason: {note}")
        else:
            lines.append("- Reason: Existing bibliographic fields matched the available source metadata, or the entry type does not have a meaningful article page range.")
    for change in TEXT_CHANGES.get(key, []):
        lines.append(f"- Thesis text/source attribution change: {change}")
    if support.get("cited_info"):
        lines.append(f"- Información citada de esta fuente: {support['cited_info']}")
    lines.append(f"- Cited information support: {support.get('status', 'not assessed')}")
    if support.get("evidence"):
        lines.append(f"- Support evidence or caveat: {support['evidence']}")
    if support.get("action"):
        lines.append(f"- Support audit action: {support['action']}")
    lines.append(f"- Checked against: {source_basis(row, source)}")
    lines.append(f"- Final recorded fields: {final_fields(row, source)}")
    lines.append("")

OUT.write_text("\n".join(lines), encoding="utf-8")
print(json.dumps({"path": str(OUT), "entries": len(AUDIT_ROWS), "bib_changed": len(CHANGES), "text_changes": len(TEXT_CHANGES)}, indent=2))
