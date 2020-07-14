#!/usr/bin/python3

from format import format_into_table, format_accepted_problems
from shortcuts import read_file, write_file, write_csv

data = format_into_table(format_accepted_problems(eval(read_file('result'))))
write_csv('result.csv', data)
