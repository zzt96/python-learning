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
一边循环，一边计算的机制，称为生成器。generator
- 创建生成器：
	- 方法一：把列表生成式的[]改为().可以通过next()打印出生成器生成的下一个元素，一般不用。
		- 一般使用for循环迭代生成器
	- 方法二：如果一个函数定义中包含**yield**关键字，那么这个函数就不再是一个普通函数，而是一个generator。
	 	- 这个函数遇到**yield**就会中断，当没有yield执行的时候就会报错。

### 迭代器
- 可迭代对象iterable：可作用于for循环的对象都是Iterable类型；
- 可以使用isinstance()判断一个对象是否是Iterable对象：isinstance('abc', Iterable) 
- 生成器不但可以作用于for循环，还可以被next\(\)函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。
- 迭代器：Iterator：可以被next()函数调用并不断返回下一个值的对象. 所以生成器都是iterator
- list，dict和str不是iterator,因为iterator是数据流，惰性，只有需要返回下一个数据的时候才会进行计算
- 但是可以通过iter()函数获得一个Iterator对象：iter('abc')

### 函数式编程
- 纯函数式编程：输入确定，输出就确定，没有副作用
- 非纯函数式编程，可以使用变量
- 函数式编程允许把函数本体作为参数传入下一个函数。

#### map/reduce
- map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
- reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做**累积计算**
