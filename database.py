#!/usr/bin/python3

import sqlite3

from format import dict2list

db = sqlite3.connect('data.db')
cursor = db.cursor()


def init():
    cursor.execute('SELECT tbl_name FROM sqlite_master where name = "SUBS"')
    if not [x for x in cursor]:
        cursor.execute('''CREATE TABLE SUBS(
            submissionId    INTEGER,
            user            TEXT,
            userId          INTEGER,
            problemName     TEXT,
            problemId       INTEGER,
            language        VARCHAR(15),
            codeSize        INTEGER,
            submitTime      VARCHAR(20),
            result          VARCHAR(22),
            time            INTEGER,
            memory          INTEGER,
            score           INTEGER
            );''')

def update(submission):
    cursor.execute('''INSERT INTO SUBS VALUES(
        %d,
        "%s",
        %d,
        "%s",
        %d,
        "%s",
        %d,
        "%s",
        "%s",
        %d,
        %d,
        %d
        );''' % tuple(dict2list(submission)))

def updates(submissions):
    for x in submissions:
        update(x)


COMMITED_CHANGES = 0
def commit():
    global COMMITED_CHANGES

    print('# Commiting changes into database...')
    db.commit()
    print('# Commiting finished.')
    print('# Total changes:', db.total_changes - COMMITED_CHANGES)
    COMMITED_CHANGES = db.total_changes


def query(params=''):
    if params:
        cursor.execute('SELECT * FROM SUBS WHERE %s;' % params)
    else:
        cursor.execute('SELECT * FROM SUBS;')
    return [x for x in cursor]

def queryitem(x):
    params = ''
    for k, v in x.items():
        if params:
            params += ' AND '
        if type(v) == str:
            params += '%s="%s"' % (k, v)
        elif type(v) == int:
            params += '%s=%d' % (k, v)
        else:
            raise TypeError('Unknown Type %s' % str(type(v)))
    return query(params)
