# Basic Python Learning Recording
all resources are from liao:https://www.liaoxuefeng.com
- Python Basics:
- Python function:

### 列表生成器
- list(range(1, 11))：生成 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- [x * x for x in range(1, 11)]生成[1x1, 2x2, 3x3, ..., 10x10]
	- 把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
	- for循环后面还可以加上if判断：[x * x for x in range(1, 11) if x % 2 == 0]
	- 还可以使用两层循环，可以生成全排列：[m + n for m in 'ABC' for n in 'XYZ']
- for循环其实可以同时使用两个甚至多个变量，使用dict的items()可以同时迭代key和value

### 生成器