#!/usr/bin/python3

import bs4
import requests
import json

from format import format_accepted_problems


BASE_URL = 'https://loj.ac'


def get_submissions(params, max_page=50, LOG=False):
	"""
	params:
	problem_id
	submitter
	min_score
	max_score
	language
	status
	currPageTop
	currPageBottom
	page
	"""

	submissions = []

	r = requests.get(base_url + '/submissions', params=params)
	for i in range(max_page):
		if LOG:
			print('# crawl: #%d: %s', % (i + 1, r.url))

		soup = bs4.BeautifulSoup(r.text, 'lxml')
		
		table = soup.find(attrs={'id': 'submissionItemTemplate'}).findNext()
		code = table.contents[0]
		code = code[code.find('itemList'):]
		code = code[code.find('['):code.find(';')]
		submissions += json.loads(code)
		
		nextpage = soup.find(attrs={'id': 'page_next'})
		
		if nextpage and 'href' in nextpage.attrs:
			r = requests.get(base_url + nextpage.attrs['href'])
		else:
			if LOG:
				print('# crawl: no page_next detected, break')
			break 
	
	if LOG:
		print('# crawl: finish')
	
	return submissions
	

def get_accepted_problems(user, max_page=50, LOG=False):	
	submissions = get_submissions({'submitter': user, 'status': 'Accepted'}, max_page, LOG)
	return format_accepted_problems(submissions)
