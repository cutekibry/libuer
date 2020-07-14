#!/usr/bin/python3


HEADERS = ['提交编号', '题目编号', '题目名称', '状态', '分数', '总时间', '内存', '语言', '代码长度', '提交者', '提交时间']


def memformat(n):
	if n < 1024:
		return '%d K' % n
	else:
		return '%.2f M' % (n / 1024)

def lenformat(n):
	if n < 1024:
		return '%d B' % n
	else:
		return '%.1f K' % (n / 1024)


def format(data):
	res = [HEADERS]
	
	for x in data:
		row = [
			x['info']['submissionId'],
			x['info']['problemId'],
			x['info']['problemName'],
			x['result']['result'],
			x['result']['score'],
			'%d ms' % x['result']['time'],
			memformat(x['result']['memory']),
			x['info']['language'],
			lenformat(x['info']['codeSize']),
			x['info']['user'],
			x['info']['submitTime'],
		]
		
		res.append(row)
	
	return res
