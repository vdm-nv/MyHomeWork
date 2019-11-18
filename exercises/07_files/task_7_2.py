#!/usr/bin/env python3

from sys import argv

file_name = argv[1]


with open(file_name) as scr:
    for line in scr:
        if line[0] == '!':
            continue
        if not line:
            continue
        print(line.strip().rstrip())
