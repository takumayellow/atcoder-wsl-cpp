#!/bin/zsh

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "usage: scripts/problem_statement.sh <label> [--url]" >&2
  exit 1
fi

label="${1:u}"
mode="${2:-}"

python_output="$(
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

title="${python_output%%$'\n'*}"
url="${python_output#*$'\n'}"

if [[ "$mode" == "--url" ]]; then
  printf '%s\n' "$url"
  exit 0
fi

html="$(curl -fsSL "$url")"

PROBLEM_HTML="$html" python - "$label" "$title" "$url" <<'PY'
import re
import sys
import os
from html import unescape
from html.parser import HTMLParser

label, title, url = sys.argv[1:]
html = os.environ["PROBLEM_HTML"]

match = re.search(r'<span class="lang-ja">(.*?)</span>', html, re.S)
if match:
    html = match.group(1)

section = re.search(
    r'<span class="h2">問題文</span>(.*?)<hr\s*/?>',
    html,
    re.S,
)
if not section:
    section = re.search(r'<div id="task-statement">(.*?)</div>', html, re.S)

if section:
    html = section.group(1)

html = re.sub(r'<script.*?</script>', '', html, flags=re.S)
html = re.sub(r'<style.*?</style>', '', html, flags=re.S)
html = re.sub(r'<li>', '\n- ', html)
html = re.sub(r'<br\s*/?>', '\n', html)
html = re.sub(r'</p>', '\n\n', html)
html = re.sub(r'</h\d>', '\n\n', html)
html = re.sub(r'</li>', '\n', html)
html = re.sub(r'</tr>', '\n', html)
html = re.sub(r'</td>', '\t', html)
html = re.sub(r'</th>', '\t', html)

class StripTags(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

parser = StripTags()
parser.feed(html)
text = unescape(''.join(parser.parts))

command_map = {
    'le': '<=',
    'leq': '<=',
    'ge': '>=',
    'geq': '>=',
    'neq': '!=',
    'times': 'x',
    'cdot': '*',
    'cdots': '...',
    'ldots': '...',
    'to': '->',
}
text = re.sub(
    r'\\([A-Za-z]+)',
    lambda m: command_map.get(m.group(1), m.group(1)),
    text,
)

text = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', text)
text = re.sub(r'([A-Za-z0-9])_\{([^{}]+)\}', r'\1[\2]', text)
text = re.sub(r'([A-Za-z0-9])_([A-Za-z0-9]+)', r'\1[\2]', text)
text = re.sub(r'([A-Za-z0-9])\^\{([^{}]+)\}', r'\1^(\2)', text)
text = re.sub(r'([A-Za-z0-9])\^([A-Za-z0-9]+)', r'\1^\2', text)
text = text.replace('\\', '')

text = re.sub(r'\r', '', text)
text = re.sub(r'[ \t]+\n', '\n', text)
text = re.sub(r'\n{3,}', '\n\n', text)
text = text.strip()

print(f"{label} {title}")
print(url)
print()
print(text)
PY
