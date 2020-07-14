#!/usr/bin/python3

import csv


from spider import get_accepted_problems
from format import format_into_table
from config import MAX_PAGE, DEBUG


def read_file(file, encoding='utf-8'):
	f = open(file, 'r', encoding=encoding)
	text = f.read()
	f.close()
	return text
	

def write_file(file, text, encoding='utf-8'):
	f = open(file, 'w', encoding=encoding)
	f.write(text)
	f.close()
	

def write_csv(file, table, encoding='utf-8'):
	f = open(file, 'w', encoding=encoding)
	writer = csv.writer(f)
	writer.writerows(table)
	f.close()
	

def write_accepted_csv(file, user, max_page=MAX_PAGE, debug=DEBUG):
	data = get_accepted_problems(user, max_page, debug)
	write_csv(file, format_into_table(data))
