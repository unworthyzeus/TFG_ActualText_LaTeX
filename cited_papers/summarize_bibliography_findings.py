import json
from pathlib import Path


ROWS = json.loads((Path(__file__).resolve().parent / "bibliography_source_audit.json").read_text(encoding="utf-8"))


def clean_title(value: str) -> str:
    return " ".join(value.replace("{", "").replace("}", "").split()).lower()


print("PAGE_MISMATCHES")
for row in ROWS:
    source_pages = row["crossref_pages"] or row["openalex_pages"]
    if source_pages and row["current_pages"] != source_pages:
        print(
            f"{row['number']:02d} {row['key']}: current={row['current_pages']!r} "
            f"source={source_pages!r} pdf={row['pdf_pages']} title={row['title'][:90]}"
        )

print("\nDOI_ERRORS")
for row in ROWS:
    if row["doi"] and row["crossref_error"]:
        print(f"{row['number']:02d} {row['key']}: {row['doi']} -> {row['crossref_error']}")

print("\nMISSING_PAGES_WITH_PDF")
for row in ROWS:
    if (
        not row["current_pages"]
        and row["pdf_pages"]
        and row["entry_type"] in {"article", "inproceedings", "techreport", "report", "book"}
    ):
        print(
            f"{row['number']:02d} {row['key']}: pdf={row['pdf_pages']} "
            f"doi={row['doi']!r} openalex={row['openalex_pages']!r} title={row['title'][:90]}"
        )

print("\nTITLE_MISMATCHES")
for row in ROWS:
    if row["doi"] and row["crossref_title"]:
        bib_title = clean_title(row["title"])
        source_title = clean_title(row["crossref_title"])
        if bib_title[:25] not in source_title and source_title[:25] not in bib_title:
            value = f"{row['number']:02d} {row['key']}: bib={row['title']} | crossref={row['crossref_title']}"
            print(value.encode("ascii", "backslashreplace").decode("ascii"))
