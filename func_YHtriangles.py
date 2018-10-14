# 杨辉三角
# range函数:生成数组 range(1,3) = [1,2]
# 特别注意：range(0)=[]；
# -*- coding: utf-8 -*-

# 方法1
def triangles():
	row = [1]
	while True:
		yield(row)
		# 先生成第一行row = [1]
		row = [1] + [row[k-1] + row[k] for k in range(len(row) - 1)] + [1]
		# 计算第二行的时候，row = [1],len(row)=1，k在range(0)中取空；所以第二行是[1,1]
		# 计算第三行的时候，row = [1,1],len(row)=2,k在range(1)中取0；row[-1]+row[0]=1+1=2 ; 所以第二行是[1,2,1]
# 方法2
def triangles1():
	N = [1]
	while True:
		yield N
		N.append(0)
		# 现在N的后面增加一个0;[1,0]
		N = [N[i-1] + N[i] for i in range(len(N))]
		# 计算第二行的时候，len(N)=2, range(2)=[0,1]；i = 0时，N[i-1] + N[i] = 1；i = 1时，N[i-1] + N[i]=1；所以N=[1,1]
		# 这个解题思路非常好，先给数组补充一个0，将其len增长1，保正最后一位数字一直是：1+0=1。  

# 验证
n = 0
result =[]
for t in triangles():
	print(t)
	result.append(t)
	n = n+1
	if n == 10:
		break
