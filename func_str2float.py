# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# -*- coding: utf-8 -*-
#  ** 幂次方
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2float(s):
	# 先确定浮点数中.的位置，然后使用replace将其取代；如果没有点，则默认点在数字最后的位置。
	n = 0
	for x in s:
		n = n + 1
		if x == '.':
			s=s.replace('.','')	
			break
		if n >= len(s):
			n = len(s)+1
			break
	def char2num(s):
		return DIGITS[s]
	def fn(x,y):
		return 10*x + y

	p = reduce(fn,map(char2num,s))# 将字符串转换为移除小数点后的整数
	result = p /(10**(len(s)-n+1))# 得出最终需要的浮点数。
	return result
print('str2float(\'123.456\') =', str2float('123456'))