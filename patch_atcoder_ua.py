import sys
import os

target_file = os.path.expanduser("~/.local/lib/python3.10/site-packages/onlinejudge/service/atcoder.py")

with open(target_file, 'r') as f:
    content = f.read()

old_str = "resp = form.request(session=session, headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})"
new_str = "resp = form.request(session=session, headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})"

if old_str in content:
    content = content.replace(old_str, new_str)
    with open(target_file, 'w') as f:
        f.write(content)
    print("Patched successfully.")
else:
    print("Target string not found in file.")
    # Debug: print near matches
    idx = content.find("form.request")
    if idx != -1:
        print("Found nearby:", content[idx:idx+200])
