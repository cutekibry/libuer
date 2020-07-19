#!/usr/bin/python3

import bs4
import requests
import json

from database import queryitem
from config import BASEURL, NEWONLY, DEBUG


def crawl(params, baseurl=BASEURL, newonly=NEWONLY, debug=DEBUG):
    """Get submissions from baseurl with specified query parameters.

    :param params: A dict contained the query parameters for the first query.
                   Possible keys:
                   * ``'problem_id'``: The id of problem.
                   * ``'submitter'``: The submitter.
                   * ``'min_score'``: The minimum score limit.
                   * ``'max_score'``: The maximum score limit.
                   * ``'language'``: The using language.
                   * ``'status'``: The submission status.
                   * ``'currPageTop'``: The maximum submission id of this page.
                                        Suggesting NOT to assign it in common cases.
                   * ``'currPageBottom'``: The minimum submission id of this page.
                                           Suggesting NOT to assign it in common cases.
                   * ``'page'``: The No. of the page.
                                 Usually equals to 1 if the pagination is invisible
                                 (e.g. https://loj.ac).
    :param baseurl: A string representing the site's root url.
                    Should NOT be end with ``'/'``.
    :param newonly: A boolean indicating whether stop crawling
                    if any submissions that were crawled have been crawled again.
    :param debug: A boolean indicating whether print debugging log or not.

    :return:
    :rtype: list
    """

    submissions = []

    r = requests.get(baseurl + '/submissions', params=params)
    i = 0
    flag = True
    while flag:
        i += 1
        if debug:
            print('# crawl: #%d: %s' % (i, r.url))

        soup = bs4.BeautifulSoup(r.text, 'lxml')

        table = soup.find(attrs={'id': 'submissionItemTemplate'}).findNext()
        code = table.contents[0]
        code = code[code.find('itemList'):]
        code = code[code.find('['):code.find(';')]
        for x in json.loads(code):
            if x['running']:
                continue

            y = {
                'submissionId': x['info']['submissionId'],
                'user': x['info']['user'],
                'userId': x['info']['userId'],
                # I don't know why, but it always has trending spaces in the last submission of the page
                'problemName': x['info']['problemName'].strip(),
                'problemId': x['info']['problemId'],
                'language': x['info']['language'],
                'codeSize': x['info']['codeSize'],
                'submitTime': x['info']['submitTime'],
                'result': x['result']['result'],
                'time': x['result']['time'],
                'memory': x['result']['memory'],
                'score': x['result']['score']
            }
            # For language is None
            if y['language'] is None:
                y['language'] = ''

            if queryitem(y):
                if flag:
                    print('# crawl: crawled a submission for the second time, break')
                flag = False
            else:
                submissions.append(y)

        nextpage = soup.find(attrs={'id': 'page_next'})

        if nextpage and 'href' in nextpage.attrs:
            r = requests.get(baseurl + nextpage.attrs['href'])
        else:
            if debug:
                print('# crawl: no page_next detected, break')
            flag = False

    if debug:
        print('# crawl: finish')

    return submissions


def crawluserac(user, baseurl=BASEURL, newonly=NEWONLY, debug=DEBUG):
    return crawl({'submitter': user, 'status': 'Accepted'}, baseurl, newonly, debug)
