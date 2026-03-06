#!/bin/zsh

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: scripts/test_samples.sh <problem-dir>" >&2
  exit 1
fi

problem_dir="$1"
test_dir="${problem_dir}/test"

if [[ ! -d "$test_dir" ]]; then
  echo "test directory not found: $test_dir" >&2
  exit 1
fi

exit_code=0

for input_file in "$test_dir"/sample-*.in; do
  if [[ ! -e "$input_file" ]]; then
    echo "no sample inputs in $test_dir" >&2
    exit 1
  fi

  case_name="${input_file:t:r}"
  expected_file="$test_dir/${case_name}.out"

  if [[ ! -f "$expected_file" ]]; then
    echo "expected output not found: $expected_file" >&2
    exit_code=1
    continue
  fi

  actual_file="/tmp/${problem_dir//\//_}_${case_name}.actual"

  if scripts/run_cpp.sh "$problem_dir" "$input_file" > "$actual_file"; then
    if diff -u "$expected_file" "$actual_file"; then
      echo "[PASS] $case_name"
    else
      echo "[FAIL] $case_name"
      exit_code=1
    fi
  else
    echo "[FAIL] $case_name (runtime or compile error)"
    exit_code=1
  fi
done

exit "$exit_code"
