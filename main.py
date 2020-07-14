#!/usr/bin/python3

from format import format
from shortcuts import read_file, write_file, write_csv

data = format(eval(read_file('result')))
write_csv('result.csv', data)
