# conding=utf-8
# ! /usr/bin/env python

n_list = []
for x in range(10):
    if x % 1 == 0:
        n_list.append(x ** 2)
print(n_list)



# 0~9中偶数的平方数列也可以通过列表推导式实现，代码如下：
n_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(n_list)