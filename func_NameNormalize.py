# -*- coding: utf-8 -*-
# 字符串是不可变对象，不能使用下标的形式进行修改
# map返回的是iterator类型，所以需要将其转换成list类型返回

# 方法1 先将str全部转换为小写，再将首部转换为大写，最后拼接起来。
def normalize(name):
	def fn(str):
		str=str.lower()
		if len(str)>0 and str[0]>='a' and str[0]<='z':
			str = str[0].upper() + str[1:]
		return str
	return list(map(fn,name)) 

# 方法2，先创建一个空数组，将str按规则一一输入，再将数组中的字符串拼接起来
def normalize1(name):
	def fn(str):
		n = 1
		list = []
		l=''
		list.append(str[0].upper())
		while n < len(str):
			list.append(str[n].lower())
			n = n+1
		for m in range(len(list)):
			l = l + list[m]
		return l
	return list(map(fn,name)) 

print(normalize1(['kisa','kKsS']))
