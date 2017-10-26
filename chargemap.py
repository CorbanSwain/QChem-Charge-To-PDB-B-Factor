#!/usr/bin/python3
#charge_map.py

from glob import glob
import re
from pprint import pprint

def main():
    sec_header_str = 'Summary of Natural Population Analysis'
    qchem_out_files = glob('*.out')
    sections = {}
    for filename in qchem_out_files:
        filename_no_ext = filename.split('.')[0]
        sections[filename_no_ext] = ''
        with open(filename,'r') as f:
            flag = False
            for line in f.readlines():
                if flag:
                    if '=' in line: break
                    else: sections[filename_no_ext] += line
                if sec_header_str in line:
                    flag = True

    pattern_str = (r'(?<= {3}.\w)\s+'
                   '(?P<number>\d+)\s+'
                   '(?P<charge>-?\d+.\d+)')
    regex = re.compile(pattern_str)
    for name, text in sections.items():
        matches = regex.findall(text)
        matches = [(int(num), float(charge)) for num, charge in matches]
        pprint(matches)


if __name__ == "__main__":
    main()
