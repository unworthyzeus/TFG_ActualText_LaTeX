import importlib.util
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
HELPER_PATH = ROOT / "build_citation_audit_data.py"
OUT = ROOT / "citation_contexts_full.json"

spec = importlib.util.spec_from_file_location("audit_helper", HELPER_PATH)
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def paragraph_bounds(text: str, position: int) -> tuple[int, int]:
    start = text.rfind("\n\n", 0, position)
    end = text.find("\n\n", position)
    if start == -1:
        start = max(0, position - 900)
    else:
        start += 2
    if end == -1:
        end = min(len(text), position + 900)
    return start, end


def main() -> None:
    keys = helper.active_order_from_aux()
    active = set(keys)
    contexts = {key: [] for key in keys}
    tex_files = [
        path
        for path in helper.THESIS.glob("*.tex")
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
        section_spans = [(m.start(), helper.clean_latex(m.group(1))) for m in section_re.finditer(text)]
        for match in cite_re.finditer(text):
            cited_keys = [key.strip() for key in match.group(1).split(",")]
            start, end = paragraph_bounds(text, match.start())
            raw_para = text[start:end]
            clean_para = helper.clean_snippet(raw_para)
            section = helper.current_section(section_spans, match.start())
            for key in cited_keys:
                if key in active:
                    contexts[key].append(
                        {
                            "file": path.name,
                            "section": section,
                            "raw_cite": match.group(0),
                            "paragraph": clean_para,
                        }
                    )
    ordered = [
        {
            "number": idx + 1,
            "key": key,
            "contexts": contexts.get(key, []),
        }
        for idx, key in enumerate(keys)
    ]
    OUT.write_text(json.dumps(ordered, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"rows": len(ordered), "out": str(OUT)}, indent=2))


if __name__ == "__main__":
    main()
