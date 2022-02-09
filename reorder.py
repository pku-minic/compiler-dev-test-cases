#!/usr/bin/env python3

'''
Scan all test cases ('*.c'), rename each test case to the format
'{id}_name.c', and make sure they all have unique and continuous ids.

Usage:
  reorder.py            # reorder all files in directories in the configuration
  reorder.py DIR        # reorder all files in DIR
  reorder.py DIR COUNT  # reorder all files in DIR, start counting from COUNT
'''

import os
import re


# ========== configurations begin ==========
test_case_dirs = [
    'testcases',
]
# ==========  configurations end  ==========

__NAME_PATTERN = re.compile(r'(\d+_)?(.+).c')


def get_id(zero_count: int, count: int) -> str:
  id = str(count)
  assert zero_count >= len(id)
  return (zero_count - len(id)) * '0' + id


def rename_file(root: str, old_name: str, new_name: str):
  cur_file = os.path.join(root, old_name)
  new_file = os.path.join(root, new_name)
  os.rename(cur_file, new_file)


def scan_and_rename(dir: str, start_count: int = 0):
  for root, _, files in os.walk(dir):
    cases = [f for f in sorted(files) if f.endswith('.c')]
    zeros = len(str(len(cases) + start_count - 1))
    count = start_count
    for f in cases:
      cur_id = get_id(zeros, count)
      # rename test case
      case_name = __NAME_PATTERN.findall(f)[0][1]
      new_case_name = f'{cur_id}_{case_name}.c'
      rename_file(root, f, new_case_name)
      # check & rename test input
      in_name = f'{f[:-2]}.in'
      if os.path.exists(os.path.join(root, in_name)):
        new_in_name = f'{cur_id}_{case_name}.in'
        rename_file(root, in_name, new_in_name)
      count += 1


if __name__ == '__main__':
  import sys
  if len(sys.argv) >= 2:
    start_count = 0
    if len(sys.argv) >= 3:
      start_count = int(sys.argv[2])
    scan_and_rename(sys.argv[1], start_count)
  else:
    for i in test_case_dirs:
      scan_and_rename(i)
