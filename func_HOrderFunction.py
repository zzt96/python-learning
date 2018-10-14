# 高阶函数：函数可以作为参数传入，在本例子中abs 作为第三参数传入add。

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))
