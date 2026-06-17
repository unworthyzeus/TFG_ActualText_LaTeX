import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { Workbook, SpreadsheetFile } from "@oai/artifact-tool";

const here = path.dirname(fileURLToPath(import.meta.url));
const rowsPath = path.join(here, "citation_audit_rows.json");
const outPath = path.join(here, "citation_audit.xlsx");

const requestedColumns = [
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
];

const rawRows = JSON.parse(await fs.readFile(rowsPath, "utf8"));
const rows = rawRows.map((row) =>
  requestedColumns.map((column) => row[column] ?? "")
);

if (rows.length !== 58) {
  throw new Error(`Expected 58 citation rows, found ${rows.length}`);
}

const wb = Workbook.create();
const ws = wb.worksheets.add("Citation audit");
const notes = wb.worksheets.add("Notes");

const values = [requestedColumns, ...rows];
ws.getRange(`A1:K${values.length}`).values = values;
ws.tables.add(`A1:K${values.length}`, true, "CitationAudit");
ws.freezePanes.freezeRows(1);

ws.getRange("A1:K1").format.font.bold = true;
ws.getRange("A1:K1").format.fill.color = "#D9EAF7";
ws.getRange("A1:K1").format.wrapText = true;
ws.getRange(`A1:K${values.length}`).format.verticalAlignment = "top";
ws.getRange(`B2:B${values.length}`).format.wrapText = true;
ws.getRange(`G2:G${values.length}`).format.wrapText = true;
ws.getRange(`H2:K${values.length}`).format.wrapText = true;
ws.getRange(`A2:K${values.length}`).format.wrapText = true;

const widths = [15, 48, 24, 20, 21, 26, 72, 78, 30, 78, 48];
for (let index = 0; index < widths.length; index += 1) {
  const col = String.fromCharCode("A".charCodeAt(0) + index);
  ws.getRange(`${col}:${col}`).format.columnWidth = widths[index];
}

notes.getRange("A1:B10").values = [
  ["Field", "Meaning"],
  ["Number of citation", "Final numbered reference order from the thesis bibliography, excluding bibliography control entries."],
  ["which pages are cited?", "Publication page span from the bibliography entry, such as pp. 84-91 or pp. 4001-4015. Large numbers are journal or proceedings page labels, not PDF viewer pages."],
  ["total number of pages", "Published source length from the page span when available. If no span is available, this uses the downloaded PDF page count."],
  ["actual pages cited", "Thesis PDF pages where that numbered citation appears."],
  ["qué se cita exactamente de esta fuente", "Plain language summary of the specific idea, number, method, dataset, or source record cited from that reference."],
  ["is the cited information in the source?", "Support judgement after checking the thesis context against the paper, report, website, book, or repository."],
  ["support evidence / caveat", "Short audit note explaining why the source supports the thesis usage, or what limitation remains."],
  ["audit action", "Any text or citation action taken. If blank-sensitive fields do not apply, the note says so here."],
  ["Blank cells", "Left empty when the paper, website, or field could not be found or does not apply."],
];
notes.tables.add("A1:B10", true, "CitationAuditNotes");
notes.freezePanes.freezeRows(1);
notes.getRange("A1:B1").format.font.bold = true;
notes.getRange("A1:B1").format.fill.color = "#E6F0E6";
notes.getRange("A:B").format.wrapText = true;
notes.getRange("A:A").format.columnWidth = 44;
notes.getRange("B:B").format.columnWidth = 104;

const previewPaths = [];
for (const sheetName of ["Citation audit", "Notes"]) {
  const preview = await wb.render({
    sheetName,
    autoCrop: "all",
    scale: 1,
    format: "png",
  });
  const safeName = sheetName.toLowerCase().replace(/\s+/g, "_");
  const previewPath = path.join(here, `${safeName}_preview.png`);
  await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));
  previewPaths.push(previewPath);
}

const blob = await SpreadsheetFile.exportXlsx(wb);
await blob.save(outPath);

const inspectPath = `${outPath}.inspect.ndjson`;
let inspect = "";
try {
  inspect = await fs.readFile(inspectPath, "utf8");
} catch {
  inspect = "";
}

console.log(JSON.stringify({
  rows: rows.length,
  xlsx: outPath,
  inspect: inspectPath,
  inspectLines: inspect ? inspect.trim().split(/\r?\n/).length : 0,
  previews: previewPaths,
}, null, 2));
