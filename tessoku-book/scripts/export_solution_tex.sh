#!/bin/zsh

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: scripts/export_solution_tex.sh <label>" >&2
  exit 1
fi

label="${1:u}"
lower_label="${label:l}"

solution_info="$(
python - "$label" <<'PY'
import json
import sys

label = sys.argv[1]
with open("contest.acc.json") as f:
    tasks = json.load(f)["tasks"]

for task in tasks:
    if task["label"].upper() == label:
        print(task["directory"]["path"])
        sys.exit(0)

raise SystemExit(f"unknown label: {label}")
PY
)"

problem_dir="$solution_info"
source_file="${problem_dir}/main.cpp"
output_dir="tex/solutions"
output_file="${output_dir}/${lower_label}.tex"

if [[ ! -f "$source_file" ]]; then
  rm -f "$output_file"
  exit 0
fi

if rg -q "write code here" "$source_file"; then
  rm -f "$output_file"
  exit 0
fi

mkdir -p "$output_dir"

python - "$source_file" "$output_file" <<'PY'
import sys
from pathlib import Path

source_file, output_file = sys.argv[1:]

def escape_tex_text(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)

document = f"""\\subsection*{{自分のコード}}
\\texttt{{{escape_tex_text(source_file)}}}

\\VerbatimInput{{{source_file}}}
"""

Path(output_file).write_text(document, encoding="utf-8")
print(output_file)
PY
