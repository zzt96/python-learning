# -*- coding: utf-8 -*-
# 计算多个数乘积：
# 需要考虑没有乘积数的情况，抛出错误。
# TypeError：对类型无效的操作错误
# raise：自己抛出异常
# http://www.runoob.com/python/python-exceptions.html
def product(*xs ):
    if len(xs) < 1:
        raise TypeError('please input at least one param!')
    product = 1
    for x in xs:
        product = product * x
    return product