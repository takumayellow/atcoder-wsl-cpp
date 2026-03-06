#!/bin/zsh

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: scripts/export_problem_tex.sh <label>" >&2
  exit 1
fi

label="${1:u}"

problem_info="$(
python - "$label" <<'PY'
import json
import sys

label = sys.argv[1]
with open("contest.acc.json") as f:
    tasks = json.load(f)["tasks"]

for task in tasks:
    if task["label"].upper() == label:
        print(task["title"])
        print(task["url"])
        sys.exit(0)

raise SystemExit(f"unknown label: {label}")
PY
)"

title="${problem_info%%$'\n'*}"
url="${problem_info#*$'\n'}"
output_path="tex/problems/${label:l}.tex"

mkdir -p tex/problems
html="$(curl -fsSL "$url")"

PROBLEM_HTML="$html" python - "$label" "$title" "$url" "$output_path" <<'PY'
import os
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

label, title, url, output_path = sys.argv[1:]
html = os.environ["PROBLEM_HTML"]


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


def normalize_math(text: str) -> str:
    text = unescape(text)
    text = text.replace("\u2212", "-")
    text = text.replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def strip_tags_preserve_text(raw_html: str) -> str:
    class PlainTextParser(HTMLParser):
        def __init__(self) -> None:
            super().__init__()
            self.parts = []

        def handle_data(self, data: str) -> None:
            self.parts.append(data)

    parser = PlainTextParser()
    parser.feed(raw_html)
    return unescape("".join(parser.parts))


class StatementParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_task_statement = False
        self.capture_ja = False
        self.lang_span_depth = 0
        self.list_depth = 0

        self.in_h3 = False
        self.in_p = False
        self.in_li = False
        self.in_pre = False
        self.in_var = False

        self.inline_parts = []
        self.pre_parts = []
        self.out_parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "div" and attrs.get("id") == "task-statement":
            self.in_task_statement = True
            return

        if not self.in_task_statement:
            return

        if tag == "span" and "lang-ja" in attrs.get("class", "").split():
            self.capture_ja = True
            self.lang_span_depth = 1
            return

        if not self.capture_ja:
            return

        if tag == "span":
            self.lang_span_depth += 1
            return

        if tag == "h3":
            self.in_h3 = True
            self.inline_parts = []
            return

        if tag == "p":
            self.in_p = True
            self.inline_parts = []
            return

        if tag == "ul":
            self.out_parts.append("\\begin{itemize}\n")
            self.list_depth += 1
            return

        if tag == "li":
            self.in_li = True
            self.inline_parts = []
            return

        if tag == "pre":
            self.in_pre = True
            self.pre_parts = []
            return

        if tag == "var":
            self.in_var = True
            return

    def handle_endtag(self, tag):
        if tag == "div" and self.in_task_statement and not self.capture_ja:
            self.in_task_statement = False
            return

        if not self.in_task_statement:
            return

        if self.capture_ja and tag == "span":
            self.lang_span_depth -= 1
            if self.lang_span_depth == 0:
                self.capture_ja = False
            return

        if not self.capture_ja:
            return

        if tag == "h3" and self.in_h3:
            heading = "".join(self.inline_parts).strip()
            if heading:
                self.out_parts.append(f"\\subsection*{{{heading}}}\n")
            self.in_h3 = False
            self.inline_parts = []
            return

        if tag == "p" and self.in_p:
            paragraph = "".join(self.inline_parts).strip()
            if paragraph:
                self.out_parts.append(paragraph + "\n\n")
            self.in_p = False
            self.inline_parts = []
            return

        if tag == "li" and self.in_li:
            item = "".join(self.inline_parts).strip()
            self.out_parts.append(f"\\item {item}\n")
            self.in_li = False
            self.inline_parts = []
            return

        if tag == "ul" and self.list_depth > 0:
            self.out_parts.append("\\end{itemize}\n\n")
            self.list_depth -= 1
            return

        if tag == "pre" and self.in_pre:
            pre_text = "".join(self.pre_parts)
            pre_text = pre_text.strip("\n")
            self.out_parts.append("\\begin{verbatim}\n")
            self.out_parts.append(pre_text + "\n")
            self.out_parts.append("\\end{verbatim}\n\n")
            self.in_pre = False
            self.pre_parts = []
            return

        if tag == "var":
            self.in_var = False
            return

    def handle_data(self, data):
        if not (self.in_task_statement and self.capture_ja):
            return

        if self.in_pre:
            self.pre_parts.append(data)
            return

        text = unescape(data)
        if not text:
            return

        if self.in_var:
            self.inline_parts.append(f"${normalize_math(text)}$")
            return

        if self.in_h3 or self.in_p or self.in_li:
            self.inline_parts.append(escape_tex_text(text))


section_html_match = re.search(
    r'<div id="task-statement">(.*)</div>\s*</div>\s*</div>',
    html,
    re.S,
)
if section_html_match:
    html = section_html_match.group(0)

parser = StatementParser()
parser.feed(html)
body = "".join(parser.out_parts).strip()
body = re.sub(r"\n{3,}", "\n\n", body)

score = ""
score_match = re.match(r"配点 : (.+?) 点\s*\n\n", body, re.S)
if score_match:
    score = score_match.group(1).strip()
    body = body[score_match.end():].lstrip()

meta_lines = []
if score:
    meta_lines.append(f"配点 : {score} 点")
meta_lines.append(f"\\texttt{{{escape_tex_text(url)}}}")
meta_block = "\n\n".join(meta_lines)

document = f"""\\section*{{{escape_tex_text(label)} {escape_tex_text(title)}}}
\\begin{{problemmeta}}
{meta_block}
\\end{{problemmeta}}

\\normalcolor
\\color{{black}}

{body}
"""

Path(output_path).write_text(document, encoding="utf-8")
print(output_path)
PY
