# coding=utf-8


# 赋值符号 “=” 前后各有一个空格
a = 10
c = 10

# 所有的二元运算符都应该使用空格与操作符分开
a += c + d

# 一元运算符：算法运算符取反“——”和和运算符取反“-”
b = 10
a = -10
y = -b

# 括号内不要有空格，Python中括号包括小括号“（）”、中括号“[]”和大括号“{}”，
# 推荐:
doque(cat[1], {dogs: 2}, [])
#不要在逗号，分好、冒号前面有空格，而是要在他们后面有一个空格，除非该符号已经是行尾了。
# 推荐
if x == 88:
    print x,y
x,y = y,x

#参数列表、索引或切片的左括号前不应有空格。
#推荐：

doque(1)
dog['key'] = list[index]
