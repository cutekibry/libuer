#!/usr/bin/python3


from shortcuts import write_accepted_csv

from pathlib import Path


data_dir = Path('data')

if data_dir.is_file():
	print('ERROR: "data" is a file instead of a directory.')
	print('Please move the file somewhere else.')
	print('Aborted.')
	exit(0)
elif not data_dir.exists():
	data.mkdir()


print('This program will crawl all the accepted problems of the user you specified,')
print('and then output the submissions into "data/{username}.csv".')
print('For the same problem, this program will only store the oldest accepted submission.')
print('-' * 32)

username = input('Please input the username: ')
print('The username is "%s".' % username)
if input('Confirm? [y/N] ').lower() != 'y':
	print('Aborted.')
	exit(0)

write_accepted_csv('data/%s.csv' % username, username)
