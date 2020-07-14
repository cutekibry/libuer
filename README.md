# libuer
一个为 Tsukimaru 临时写的里布尔欧杰（[LibreOJ](https://loj.ac)）小工具。

运行 `python3 main.py`，输入用户名，它就会帮你把这位用户的所有 AC 状态爬下来，保存到 `data/{username}.csv` 里。

* 提交状态按时间从最近（Latest）到最远（Oldest）排序。
* 对于同一道题目，仅保存时间最远的提交状态。

范例可参见 [`data/moonoshawott.csv`](https://github.com/cutekibry/libuer/blob/master/data/moonoshawott.csv)。

```shell
cutekibry@cutekibry-JZOI ~/文档/libuer (master*) $ python3 main.py
This program will crawl all the accepted problems of the user you specified,
and then output the submissions into "data/{username}.csv".
For the same problem, this program will only store the oldest accepted submission.
--------------------------------
Please input the username: moonoshawott
The username is "moonoshawott".
Confirm? [y/N] N
Aborted.
```
