#使用迭代查找一个list中最小和最大值，并返回一个tuple
# tuple:一旦定义出来就不可变了；所以没有append()，insert()这样的方法。
# 定义一个tuple：t = (1, 2)
# ps.list:L = [x,y,z]
# -*- coding: utf-8 -*-
def findMinAndMax(L):
	if L == []:
		return (None, None)
	else:
		max = L[0]
		min = L[0]
		for m in L:
			if m <= min:
				min = m
		for M in L:
			if M >= max:
				max = M
		R = (min,max)
		return R