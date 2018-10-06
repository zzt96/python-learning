# -*- coding: utf-8 -*-
def move(n, a, b, c): # 借助b将a上所有的盘子移动到c
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)# 借助c将上面（n-1）个盘子从a移动到b
        move(1,a,b,c)# 将a上剩下的一个盘子从a移动到c
        move(n-1,b,a,c)# 借助a，将b上面（n-1）个盘子移动到c