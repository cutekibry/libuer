#!/usr/bin/python3

import csv
from pathlib import Path

from terminaltables import AsciiTable
import database
import crawl
from config import BASEURL, NEWONLY, DEBUG
import format


def write_csv(file, table, encoding='utf-8'):
    dir = Path(file[:file.rfind('/')])
    if not dir.is_dir():
        dir.mkdir(parents=True)

    f = open(file, 'w', encoding=encoding)
    writer = csv.writer(f)
    writer.writerows(table)
    f.close()


def query(params=''):
    return AsciiTable([format.HEADERS] + database.query(params)).table


def queryusers():
    res = set([x[1] for x in database.query()])
    if '' in res:
        res.remove('')
    return list(res)


# def upcrawl(params, baseurl=BASEURL, newonly=NEWONLY, debug=DEBUG):
#     res = crawl.crawl(params, baseurl, newonly, debug)
#     database.updates(res)
#     database.commit()


def upuserac(user, baseurl=BASEURL, newonly=NEWONLY, debug=DEBUG):
    if not user:
        raise ValueError('Username is void')
    res = crawl.crawluserac(user, baseurl, newonly, debug)
    res = format.unique(res)
    for each in res:
        if not database.query("user=\"%s\" AND problemId=%d AND result=\"Accepted\"" % (each['user'], each['problemId'])):
            database.update(each)
    database.commit()


def upalluserac(baseurl=BASEURL, newonly=NEWONLY, debug=DEBUG):
    for user in queryusers():
        upuserac(user, baseurl, newonly, debug)


def dumpuserac(user, file=None, syzoj=True):
    if not user:
        raise ValueError('Username is void')

    data = format.unique(database.query('user="%s"' % user))
    data = sorted(data, key=lambda x: x[7], reverse=True)

    if file is None:
        file = 'outputs/%s.csv' % user

    if syzoj:
        data = format.formatsyzoj(data)
    else:
        data = format.formatcsv(data)
    write_csv(file, data)


def dumpalluserac(syzoj=True):
    for user in queryusers():
        dumpuserac(user, syzoj=syzoj)
