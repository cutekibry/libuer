#!/usr/bin/python3


import csv


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
