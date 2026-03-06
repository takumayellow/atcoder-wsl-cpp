#!/bin/zsh

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: scripts/build_problem_pdf.sh <label>" >&2
  exit 1
fi

label="${1:u}"
lower_label="${label:l}"

scripts/export_problem_tex.sh "$label" >/dev/null
scripts/export_solution_tex.sh "$label" >/dev/null || true

tmp_dir="$(mktemp -d /tmp/tessoku-problem-XXXXXX)"
trap 'rm -rf "$tmp_dir"' EXIT

wrapper_tex="$tmp_dir/${lower_label}.tex"
problem_tex="$(pwd)/tex/problems/${lower_label}.tex"
solution_tex="$(pwd)/tex/solutions/${lower_label}.tex"

solution_input=""
if [[ -f "$solution_tex" ]]; then
  solution_input="\\input{$solution_tex}"
fi

cat > "$wrapper_tex" <<EOF
\documentclass[a4paper,12pt]{ltjsarticle}

\input{$(pwd)/tex/preamble/problem_pdf_preset}

\begin{document}
\input{$problem_tex}
$solution_input
\end{document}
EOF

/Library/TeX/texbin/latexmk -r latexmkrc -lualatex -jobname="$lower_label" "$wrapper_tex"
find build -maxdepth 1 -type f ! -name '*.pdf' -delete

echo "build/${lower_label}.pdf"
