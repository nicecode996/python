# ！usr/bin/env python 3
# coding=utf-8

print("----范围------")
for num in range(1,100):
    print("{0} * {0} = {1}".format(num ,num * num))

print("----范围------")
#  for语句
for item in 'Hello':
    print(item)
    
# 生命整数列表
numbers = {43,32,53,54,75,7,10}

print("----整数列表------")

# for语句
for item in numbers:
    print("Counts is : {0}".format(item))

sum = 0
for x in (1,2,3,4,5):
    sum = sum + x
print(sum)