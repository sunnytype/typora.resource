#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

print('Typora:')

def find_word(file_path, word):
    line_num = -1
    file = open(file_path, 'r')
    lines = file.readlines()
    idx = 0
    for line in lines:
        if word in line:
            line_num = idx
            break
        idx += 1
    return line_num

def replace_line(file_path, line_num, line_new):
    lines = None
    with open(file_path, 'r') as file_read:
        lines = file_read.readlines()
    lines[line_num] = line_new
    with open(file_path, 'w') as file_write:
        file_write.writelines(lines)


file_path = '/Users/sunny/Library/Application Support/abnerworks.Typora/themes/clean.css'

def replace_line_word(file_path, word, line_new):
    line_num = find_word(file_path, word)
    if line_num > 0:
        replace_line(file_path, line_num, line_new)

if len(sys.argv) > 1:
    max_width = sys.argv[len(sys.argv) - 1] + 'px'
    replace_line_word(file_path, '/*root-max-width*/', '    max-width: ' + max_width + '; /*root-max-width*/\n')
    print('Succeed! max-width=' + max_width)

