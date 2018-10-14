# 使用map函数先将char逐个转换成num
# 再使用reduce将num累加转换为int型
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
	def char2num(s):
		return DIGITS[s]
	def fn(x,y):
		return 10*x + y
	return reduce(fn,map(char2num, s ))

print(str2int('12345'))

