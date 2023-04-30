# @author :  Hao.Li
# @time : 2023-04-25
# @file : np_two.py
# @describe :
import numpy as np
a = np.array([[1,2,4], [4,5,6],[7,8,9]])
b = np.array([[1,2,3], [4,5,6],[7,8,9]])
c = np.array([[2],[3],[5]])
# 矩阵广播化逐元素相乘
# 单列，对应的行相乘,行列数最好一致，
print(a * c)
print(a * b)
# 矩阵向量化相乘，列数相同即可
print(a @ b)
print(a @ c)
# 计算数组均值、方差、标准差，可以加入axis计算所有行或者列的均值，不加则默认整个数组
print(np.mean(a, axis=1))
print(np.mean(a, axis=0))
# 方差一般使用variance
print(np.var(a))
print(np.std(a))
# 以a和c 为例，求解线性方程组
print(np.linalg.solve(a, c))
# 计算一个逆矩阵，
print(np.linalg.inv(a))



