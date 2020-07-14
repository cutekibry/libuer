#!/usr/bin/python3

from pprint import pprint
import bs4
import requests
import json

base_url = 'https://loj.ac'

"""
problem_id
submitter
min_score
max_score
language
status

currPageTop
currPageBottom=839619
page=1
"""

params = {
	'submitter': 'iot',
	'status': 'Accepted',
}

total = []

r = requests.get(base_url + '/submissions', params=params)
while True:
	print('#', r.url)

	soup = bs4.BeautifulSoup(r.text, 'lxml')
	
	table = soup.find(attrs={'id': 'submissionItemTemplate'}).findNext()
	code = table.contents[0]
	code = code[code.find('itemList'):]
	code = code[code.find('['):code.find(';')]
	total += json.loads(code)
	
	nextpage = soup.find(attrs={'id': 'page_next'})
	
	if nextpage and 'href' in nextpage.attrs:
		r = requests.get(base_url + nextpage.attrs['href'])
	else:
		break 
	
with open('result', 'w', encoding='utf-8') as f:
	pprint(total, stream=f)
