# coding=utf-8
# 代码文件：chapter/8.1.1/hello.py

import sys

score = int(sys.argv[1])

if score >=85:
    print("优秀！")

if score <=60:
    print(("努力"))

if (score > 60) and (score <85):
    print("凑合事吧！")