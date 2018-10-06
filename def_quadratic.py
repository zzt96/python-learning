# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
	# 判断输入参数是否是正规的值
	for i in [a,b,c]:
		if not isinstance(i, (int, float)):
			raise TypeError(i,'is a bad operand type')
	delta = b*b - 4*a*c
	if delta < 0:
		print('wrong params, no result!')
	elif delta == 0:
		x = -(b / 2*a)
		return x
	else:
		delta0 = math.sqrt(delta)
		x1=(- b + delta0)/(2*a)
		x2=(- b - delta0)/(2*a)#分母需要增加括号不然计算结果不正确
		return x1,x2

