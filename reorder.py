#!/usr/bin/env python3

'''
Scan all test cases ('*.c'), rename each test case to the format
'{id}_name.c', and make sure they all have unique and continuous ids.
'''

import os
from os import path
import re
import sys


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


def rename_file(root: str, old_name: str, new_name: str) -> None:
  cur_file = path.join(root, old_name)
  new_file = path.join(root, new_name)
  os.rename(cur_file, new_file)


def scan_and_rename(dir: str, start_count: int = 0) -> None:
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
      if path.exists(path.join(root, in_name)):
        new_in_name = f'{cur_id}_{case_name}.in'
        rename_file(root, in_name, new_in_name)
      count += 1


def eprint(root: str, file: str, msg: str) -> None:
  print(f'ERROR [{path.join(root, file)}]: {msg}', file=sys.stderr)


def scan_and_check(dir: str, start_count: int = 0) -> bool:
  ok = True
  for root, _, files in os.walk(dir):
    cases = [f for f in sorted(files) if f.endswith('.c')]
    zeros = len(str(len(cases) + start_count - 1))
    # check test inputs
    c_stems = {f[:-2] for f in cases}
    for in_file in files:
      if in_file.endswith('.in') and in_file[:-3] not in c_stems:
        eprint(root, in_file, 'no matching .c file')
        ok = False
    # check test cases
    seen_ids = {}
    for f in cases:
      # extract id
      m = __NAME_PATTERN.match(f)
      if not m or not m.group(1):
        eprint(root, f, 'missing numeric id prefix')
        ok = False
        continue
      id_str = m.group(1).rstrip('_')
      id_val = int(id_str)
      # check zero-padding
      if len(id_str) != zeros:
        expected_str = get_id(zeros, id_val)
        eprint(root, f,
               f'id "{id_str}" should be zero-padded to {zeros} digits (expected "{expected_str}")')
        ok = False
      # check duplicate ids
      if id_val in seen_ids:
        eprint(root, f,
               f'duplicate id {id_val} (also used by {seen_ids[id_val]})')
        ok = False
      else:
        seen_ids[id_val] = f
    # check gap in ids
    if seen_ids:
      expected = start_count
      for id_val in sorted(seen_ids):
        if id_val != expected:
          eprint(root, seen_ids[id_val],
                 f'expected id {expected} but got {id_val}')
          ok = False
        expected += 1
  return ok


if __name__ == '__main__':
  import argparse

  parser = argparse.ArgumentParser(
      description="Reorder or check test case file ids in a directory.")
  parser.add_argument('dirs', nargs='*', metavar='DIR',
                      help='directories to process (default: configured directories)')
  parser.add_argument('-s', '--start', type=int, default=0, metavar='COUNT',
                      help='starting count (default: 0)')
  parser.add_argument('-c', '--check', action='store_true',
                      help='check that ids are continuous from start without duplicates (no rename)')
  args = parser.parse_args()

  dirs = args.dirs if args.dirs else test_case_dirs

  if args.check:
    all_ok = True
    for d in dirs:
      if not scan_and_check(d, args.start):
        all_ok = False
    if not all_ok:
      exit(1)
  else:
    for d in dirs:
      scan_and_rename(d, args.start)
