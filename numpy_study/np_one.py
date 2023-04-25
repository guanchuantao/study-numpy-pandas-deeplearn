# @author :  Hao.Li
# @time : 2023-04-18
# @file : np_one.py
# @describe :
# 导入模块
import numpy as np
a = np.array([[1, 2 ,3 ,4],[5 ,6 ,7 ,8]])
# 输出数组和数组格式
print(a, type(a))
# 打印第一行
print(a[0])
# 打印第三列(根据索引打印)
print(a[:, 2])
# 数组中的运算一般都对应着数组与数组之间的运算
# 只加一维的就会第一行相加，数量需要相同
b = np.array([1,1,1,1])
c = np.array([[1,1,1,2],[2,2,2,1]])
print(a + b)
print(a + c)
# 将二维数组变成一维
d = a.flatten()
print(d)
# 将d拆分成4行2列的数组
print(d.reshape(4,2))
s1 =np.array([2,3])
s2 =np.array([4,5])
s3 =np.array([6,7])
# 将这三个数组进行合并
s = np.array([s1,s2,s3])
e = s.flatten()
print(e,type(e))