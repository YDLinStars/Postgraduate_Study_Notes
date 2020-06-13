import numpy as np
from numpy import  array
# 第二单元： Numpy创建array
# 2.1一维array创建
# a = np.array([2,23,4],dtype=np.int32) #np.int 默认为int32
# print(a)
# print(a.dtype)
#多维array创建
# a = np.zeros((3,4))
# print(a) # 生成3行4列的全零矩阵
# 创建全1数据
# a = np.ones((3,4),dtype=np.int)
# print(a)
# 创建连续数组
# a = np.arange(10,21,2) # 10-20的数据，步长为2
# print(a)
# 创建连续型数据
# a = np.linspace(1,10,20) # 开始端口1，结束端10，且分割成20个数据，生成线段
# print(a)
# # 同时也可以reshape
# b = a.reshape((5,4))
# print(b)

# 第三单元：3.Numpy基本运算
# a = np.array([10,20,30,40])
# b = np.arange(4)
# print(a,b)
# # 在Numpy中，想要求出矩阵中各个元素的乘方需要依赖双星符号 **，以二次方举例，即：
# c = b **2
# print(c)
# # Numpy中具有很多的数学函数工具
# d = np.sin(a)
# print(d)
# print(b<2)
# e = np.array([1,1,4,3])
# d = np.arange(4)
# print(e == d)
# 多维矩阵运算
# a = np.array([[1,1],[0,1]])
# b = np.arange(4).reshape((2,2))
# print(a)
# print(b)
# 多维矩阵乘法不能直接使用'*'号
# a = np.random.random((2,4))
# print(np.sum(a))
# print('a= ',a)
# # 当axis的值为0的时候，将会以列作为查找单元，
# # 当axis的值为1的时候，将会以行作为查找单元。
# print("sum=",np.sum(a,axis=1))
# 3.3 基本计算
# A = np.arange(2,14).reshape((3,4))
# print(A)
# # 最小元素索引
# print(np.argmin(A)) # 0
# # 最大元素索引
# print(np.argmax(A)) # 11
# # 求整个矩阵的均值
# print(np.mean(A)) # 7.5
# print(np.average(A)) # 7.5
# print(A.mean()) # 7.5
# # 中位数
# print(np.median(A)) # 7.5
# # 累加
# print(np.cumsum(A))
# # 仿照列表排序
# B = np.arange(14,2,-1).reshape((3,4)) # -1表示反向递减一个步长
# print(B)
# print(np.sort(A))
# # 矩阵逆置
# print(np.transpose(B))
# # 矩阵转置
# print(B.T)
# print(B)
# # clip(Array,Array_min,Array_max)
# # 将Array_min<X<Array_max X表示矩阵A中的数，如果满足上述关系，则原数不变。
# # 否则，如果X<Array_min，则将矩阵中X变为Array_min;
# # 如果X>Array_max，则将矩阵中X变为Array_max.
# print(np.clip(A,5,9))

#第四单元： Numpy索引与切片
# A = np.arange(3,15)
# print(A)
# B = A.reshape(3,4)
# print(B)
# # list切片操作
# print(B[1,1:3]) # [8 9] 1:3表示1-2不包含3
# # 如果要打印列，则进行转置即可
# for column in B.T:
#     print(column)

#第五单元： Numpy array合并
# A = np.array([1,1,1])
# B = np.array([2,2,2])
# print(np.vstack((A,B)))
# #数组转置为矩阵
# print(A[np.newaxis,:]) # [1 1 1]变为[[1 1 1]]

#第六单元： 6.Numpy array分割
# 6.2 等量分割
# A = np.arange(12).reshape((3,4))
# print(A)
# # 等量分割
# # 纵向分割同横向合并的axis
# print(np.split(A, 2, axis=1))

# 7.Numpy copy与 =
# `=`赋值方式会带有关联性
# a = np.arange(4)
# print(a)  # [0 1 2 3]
# b = a
# c = a
# d = b
# a[0] = 11
# print(a) # [11 1 2 3]
# 7.2copy()赋值方式没有关联性
# a = np.arange(4)
# print(a)
# b =a.copy() # deep copy
# print(b) # [0 1 2 3]
# a[3] = 44
# print(a) # [ 0 1 2 44]
# print(b) # [0 1 2 3]
# 此时a与b已经没有关联

# 第八章：广播机制
# numpy数组间的基础运算是一对一，也就是a.shape==b.shape，但是当两者不一样的时候，就会自动触发广播机制，如下例子：
# a = array([[ 0, 0, 0],
# [10,10,10],
# [20,20,20],
# [30,30,30]])
# b = array([0,1,2])
# print(a+b) #图三、图四

# 第九章：常用的函数：
# np.bincount 统计索引出现次数
x = np.array([1, 2, 3, 3, 0, 1, 4])
print(np.bincount(x))
w = np.array([0.3,0.5,0.7,0.6,0.1,-0.9,1])
print(np.bincount(x,weights=w))
# np.argmax()  函数表示返回沿轴axis最大值的索引,从0 开始。
x = np.array([1, 1, 5, 3, 0, 1, 0])
print(x.argmax())
# 9.3 上述合并实例
x = np.array([1, 2, 3, 3, 0, 1, 4])
print(np.argmax(np.bincount(x)))
# np.around 求取精度
np.around([-0.6,1.2798,2.357,9.67,13], decimals=0)#取指定位置的精度
#看到没，负数进位取绝对值大的！
np.around([1,2,5,50,56,190], decimals=-2)
#看到没，必须看两位，超过50才会进位，190的话，就看后面两位，后两位90超过50，进位，那么为200！
#计算沿指定轴第N维的离散差值
x = np.arange(1 , 16).reshape((3 , 5))
print(x)


