# Local Handoff: acx behavior in WSL

## Goal
When running `acx` in WSL Bash:
1. automatically `cd` to `.../<contest>/a`
2. automatically open `main.cpp` (or `main.py`) in the current editor window

## Required setup (WSL side)
Create `~/.bash_aliases` with this function:

```bash
acx() {
  local repo="$HOME/Documents/atcoder/atcoder-wsl-cpp"
  local script="$repo/tools/acx"

  if [[ ! -x "$script" ]]; then
    echo "acx wrapper error: $script is not executable." >&2
    return 1
  fi

  local output status line
  local cd_target=""
  local open_target=""

  output="$($script "$@" 2>&1)"
  status=$?

  while IFS= read -r line; do
    case "$line" in
      CD:*)
        cd_target="${line#CD:}"
        ;;
      OPEN:*)
        open_target="${line#OPEN:}"
        ;;
      *)
        printf '%s\n' "$line"
        ;;
    esac
  done <<< "$output"

  if [[ $status -ne 0 ]]; then
    return $status
  fi

  if [[ -n "$cd_target" && -d "$cd_target" ]]; then
    cd "$cd_target" || return 1
  fi

  if [[ -n "$open_target" && -f "$open_target" ]]; then
    if command -v code >/dev/null 2>&1; then
      code -r -g "$open_target" >/dev/null 2>&1 &
    elif command -v cursor >/dev/null 2>&1; then
      cursor -r -g "$open_target" >/dev/null 2>&1 &
    fi
  fi
}
```

And ensure `~/.bashrc` contains:

```bash
[ -f ~/.bash_aliases ] && source ~/.bash_aliases
```

## Validation
Run:

```bash
source ~/.bashrc
type acx
acx abc420
pwd
```

Expected:
- `type acx` => `acx is a function`
- `pwd` ends with `/abc420/a`
- editor opens `main.cpp` or `main.py`
