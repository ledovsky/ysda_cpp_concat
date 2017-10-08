help = """
Script for concatenating your CPP project into one file for YSDA algorithms
course homeworks or Yandex.Contest or for anything where it suits

Usage. Copy cpp_concat.py to your project root and run it. For example:

python cpp_concat.py config.json

It's expected you have Python 3 and your files are in UTF-8

config example

{
    "files": [
        "file.h",
        "file.cpp",
        "main.cpp"
    ],
    "out_fn": "main_out.cpp"
}

Author: Alexander Ledovsky, 2017
"""

import argparse
import re
import json

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=help,
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('config_path', action='store')
    args = parser.parse_args()

    with open(args.config_path, 'r') as f:
        config = json.loads(f.read())

    # concatenation
    text = ''
    for f in config['files']:
        with open(f, 'r') as f:
            text += f.read()
            text += '\n'

    lines = text.split('\n')

    # include filtering
    filtered_lines = []
    include_lines = []
    includes = set()
    for l in lines:
        # skip inner includes
        if re.search(r'^#include "', l):
            continue

        # avoid duplicates of outter includes
        match = re.search(r'^#include <.*>', l)
        if match:
            if l in include_lines:
                continue
            else:
                include_lines.append(l)
                continue

        # keep all other lines
        filtered_lines.append(l)

    lines = include_lines + [''] + filtered_lines

    # filter excessive blank lines
    filtered_lines = []
    for l_1, l_2, l_3 in zip([None, None] + lines[:-2],
                             [None] + lines[:-1], lines):
        if l_3 == '':
            if l_1 == '' and l_2 == '':
                continue
        filtered_lines.append(l_3)
    lines = filtered_lines

    if not lines[-1]:
        lines = filtered_lines[:-1]

    with open(config['out_fn'], 'w') as f:
        f.write('\n'.join(lines))
