import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "download_manifest.csv"
MISSING = ROOT / "open_pdf_not_found.txt"
SUMMARY = ROOT / "summary.json"

MANUAL_PATTERNS = {
    "walfisch1988": ["A_theoretical_model_of_UHF_propagation_in_urban_environments.pdf"],
    "ikegami1984": ["Propagation_factors_controlling_mean_field_strength_on_urban_streets.pdf"],
    "wocc2021": ["Channel_Modeling_of_Air-to-Ground_Signal_Measurement_with_Two-Ray_Ground-Reflection_Model_for_UAV_Communication_Systems.pdf"],
    "alhourani2014": ["Optimal_LAP_Altitude_for_Maximum_Coverage.pdf"],
    "pmnet_icassp2023": ["PMNet_*Large-Scale Channel Prediction System*.pdf"],
    "sip2net2025": ["SIP2Net_Situational-Aware_Indoor_Pathloss-Map_Prediction_Network_for_Radio_Map_Generation.pdf"],
    "yang2019a2gml": ["IET Microwaves Antenna*Yang*Machine*prediction methods*delay spread in.pdf"],
    "izydorczyk2019": ["Angular_Distribution_of_Cellular_Signals_for_UAVs_in_Urban_and_Rural_Scenarios.pdf"],
}


def pick_file(patterns: list[str]) -> Path | None:
    matches: list[Path] = []
    for pattern in patterns:
        matches.extend(ROOT.glob(pattern))
    matches = [path for path in matches if path.is_file()]
    if not matches:
        return None
    return sorted(matches, key=lambda path: ("(1)" in path.name, -path.stat().st_mtime))[0]


with MANIFEST.open(newline="", encoding="utf-8-sig") as handle:
    rows = list(csv.DictReader(handle))
    fieldnames = handle.readline()

if not rows:
    raise SystemExit("download_manifest.csv has no rows")

fieldnames = list(rows[0].keys())
updated: list[str] = []

for row in rows:
    key = row.get("key", "")
    if key not in MANUAL_PATTERNS:
        continue
    path = pick_file(MANUAL_PATTERNS[key])
    if not path:
        continue
    row["status"] = "already_downloaded"
    row["source_url"] = row.get("source_url") or row.get("url") or row.get("doi") or ""
    row["file"] = str(path)
    row["notes"] = f"manual local file present; {path.stat().st_size} bytes"
    updated.append(key)

with MANIFEST.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

remaining = [row for row in rows if row.get("status") == "open_pdf_not_found"]
MISSING.write_text(
    "\n".join(
        f"{row.get('key','')} | {row.get('title','')} | DOI: {row.get('doi','')} | URL: {row.get('url','')}"
        for row in remaining
    ),
    encoding="utf-8",
)

if SUMMARY.exists():
    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
else:
    summary = {}
summary["downloaded_or_already"] = sum(1 for row in rows if row.get("status") in {"downloaded", "already_downloaded", "downloaded_report_parts"})
summary["downloaded_pdfs"] = sum(
    1
    for row in rows
    if row.get("file", "").lower().endswith(".pdf")
    and row.get("status") in {"downloaded", "already_downloaded"}
)
summary["downloaded_report_parts"] = sum(1 for row in rows if row.get("status") == "downloaded_report_parts")
summary["skipped_non_paper_or_software"] = sum(1 for row in rows if row.get("status") == "skipped_non_paper_or_software")
summary["open_pdf_not_found"] = len(remaining)
SUMMARY.write_text(json.dumps(summary, indent=2), encoding="utf-8")

print(json.dumps({"updated": updated, "remaining_missing": [row.get("key") for row in remaining]}, indent=2))
