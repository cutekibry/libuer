#!/usr/bin/python3


ZHHEADERS = ['提交编号', '题目编号', '题目名称', '状态', '分数',
             '总时间', '内存', '语言', '代码长度', '提交者', '提交时间']
HEADERS = ['submissionId', 'user', 'userId', 'problemName', 'problemId',
           'language', 'codeSize', 'submitTime', 'result', 'time', 'memory', 'score']


def unique(submissions):
    result = []
    idset = set()
    for x in submissions[::-1]:
        if type(x) == dict:
            pid = (x['userId'], x['problemId'])
        else:
            pid = (x[2], x[4])
        if pid not in idset:
            idset.add(pid)
            result.append(x)

    return result[::-1]


def memformat(n):
    return '%d K' % n if n < 1024 else '%.2f M' % (n / 1024)


def lenformat(n):
    return '%d B' % n if n < 1024 else '%.1f K' % (n / 1024)


def list2dict(x):
    return {
        'submissionId': x[0],
        'user': x[1],
        'userId': x[2],
        'problemName': x[3],
        'problemId': x[4],
        'language': x[5],
        'codeSize': x[6],
        'submitTime': x[7],
        'result': x[8],
        'time': x[9],
        'memory': x[10],
        'score': x[11]
    }


def dict2list(x):
    return [
        x['submissionId'],
        x['user'],
        x['userId'],
        x['problemName'],
        x['problemId'],
        x['language'],
        x['codeSize'],
        x['submitTime'],
        x['result'],
        x['time'],
        x['memory'],
        x['score']
    ]


def formatsyzoj(data):
    res = [ZHHEADERS]

    for x in data:
        if type(x) != dict:
            x = list2dict(x)
        row = [
            x['submissionId'],
            x['problemId'],
            x['problemName'],
            x['result'],
            x['score'],
            '%d ms' % x['time'],
            memformat(x['memory']),
            x['language'],
            lenformat(x['codeSize']),
            x['user'],
            x['submitTime'],
        ]

        res.append(row)

    return res


def formatcsv(data):
    res = [HEADERS]

    for x in data:
        if type(x) == dict:
            x = dict2list(x)
        res.append(x)

    return res
