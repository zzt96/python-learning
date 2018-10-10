# 列表生成式
# 非字符串类型使用lower()会出错
# 使用isinstance()判断是否为字符串：isinstance(x, str)
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)==True]
print('L1 =',L1)
print('把list中所有字符串小写，并去除非字符串类型的数据，处理后的结果',L2)
# 期待输出：L2 == ['hello', 'world', 'apple']