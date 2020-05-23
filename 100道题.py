# 1. 导入numpy库并简写为 np
import numpy as np 

# 2. 打印numpy的版本和配置说明
# print(np.__version__)
# np.show_config()

# 3. 创建一个长度为10的空向量
# Z = np.zeros(10)
# print(Z)

# 4. 如何找到任何一个数组的内存大小？
# Z = np.zeros((10,10))
# print("%d bytes" % (Z.size * Z.itemsize))

# 5. 如何从命令行得到numpy中add函数的说明文档?
# np.info(np.add)

# 6. 创建一个长度为10并且除了第五个值为1的空向量 
# Z = np.zeros(10)
# Z[4]=1
# print(Z)

# 7. 创建一个值域范围从10到49的向量
# Z = np.arange(10,50)
# print(Z)

# 8. 反转一个向量(第一个元素变为最后一个) 
# Z = np.arange(50)
# Z = Z[::-1]
# print(Z)

# 9. 创建一个 3x3 并且值从0到8的矩阵
# Z = np.arange(9).reshape(3,3)
# print(Z)

# 10. 找到数组[1,2,0,0,4,0]中非0元素的位置索引
# nz = np.nonzero([1,2,0,0,4,0])
# print(nz)

# 11. 创建一个 3x3 的单位矩阵
# z = np.eye(3)
# print(z)

# 12. 创建一个 3x3x3的随机数组
# z = np.random.random((3,3,3))
# print(z)

# 13. 创建一个 10x10 的随机数组并找到它的最大值和最小值
# z = np.random.random((10,10))
# zmin,zmax=z.min(),z.max()
# print(zmin,zmax)

# 14. 创建一个长度为30的随机向量并找到它的平均值
# z=np.random.random(30)
# m=z.mean()
# print(m)

# 15. 创建一个二维数组，其中边界值为1，其余值为0 
# z=np.ones((10,10))
# z[1:-1,1:-1]=0
# print(z)

# 16. 对于一个存在在数组，如何添加一个用0填充的边界?
# array——表示需要填充的数组；
# pad_width——表示每个轴（axis）边缘需要填充的数值数目。
# mode——表示填充的方式（取值：str字符串或用户提供的函数）,总共有11种填充模式；
#     ‘constant’——表示连续填充相同的值，每个轴可以分别指定填充值，constant_values=（x, y）时前面用x填充，后面用y填充，缺省值填充0
#     ‘edge’——表示用边缘值填充
#     ‘linear_ramp’——表示用边缘递减的方式填充
#     ‘maximum’——表示最大值填充
#     ‘mean’——表示均值填充
#     ‘median’——表示中位数填充
#     ‘minimum’——表示最小值填充
#     ‘reflect’——表示对称填充
#     ‘symmetric’——表示对称填充
#     ‘wrap’——表示用原数组后面的值填充前面，前面的值填充后面

# z=np.ones((5,5))
# z=np.pad(z,pad_width=1,mode='constant',constant_values=0)
# print(z)

# 17. 以下表达式运行的结果分别是什么? 
# print(0*np.nan)
# print(np.nan==np.nan)
# print(np.inf>np.nan)
# print(np.nan - np.nan)
# print(0.3 == 3 * 0.1)

# 18. 创建一个 5x5的矩阵，并设置值1,2,3,4落在其对角线下方位置
# array是一个1维数组时，结果形成一个以一维数组为对角线元素的矩阵
# array是一个二维矩阵时，结果输出矩阵的对角线元素
# z=np.diag(1+np.arange(4),k=-1)
# print(z)

# 19. 创建一个8x8 的矩阵，并且设置成棋盘样式
# z=np.zeros((8,8),dtype=int)
# z[1::2,::2]=1
# z[::2,1::2]=2
# print(z)

# 20. 考虑一个 (6,7,8) 形状的数组，其第100个元素的索引(x,y,z)是什么
# print(np.unravel_index(100,(6,7,8)))

# 21. 用tile函数去创建一个 8x8的棋盘样式矩阵
# z=np.tile(np.array([[0,1],[1,0]]),(4,4))
# print(z)

# 22. 对一个5x5的随机矩阵做归一化
# z=np.random.random((5,5))
# zmax,zmin=z.max(),z.min()
# z=(z-zmin)/(zmax-zmin)
# print(z)

# 23. 创建一个将颜色描述为(RGBA)四个无符号字节的自定义dtype
# color = np.dtype([("r", np.ubyte, 1),
#                   ("g", np.ubyte, 1),
#                   ("b", np.ubyte, 1),
#                   ("a", np.ubyte, 1)])
# color

# 24. 一个5x3的矩阵与一个3x2的矩阵相乘，实矩阵乘积是什么
# z=np.dot(np.ones((5,3)),np.ones((3,2)))
# print(z)

# 25. 给定一个一维数组，对其在3到8之间的所有元素取反
# z=np.arange(11)
# z[(3<z)&(z<=8)]*=-1
# print(z)

# 26. 下面脚本运行后的结果是什么
# print(sum(range(5),-1))
# range(5)
# from numpy import *
# print(sum(range(5),-1))
# range(5)

# 27. 考虑一个整数向量Z,下列表达合法的是哪个
# Z**Z
# 2 << Z >> 2
# Z <- Z
# 1j*Z
# Z/1/1
# Z<Z>Z

# 28. 下列表达式的结果分别是什么
# print(np.array(0) / np.array(0))
# print(np.array(0) // np.array(0))

# 29. 如何从零位对浮点数组做舍入
# z=np.random.uniform(-10,+10,10)
# print(z)
# print(np.copysign(np.ceil(np.abs(z)),z))

# 30. 如何找到两个数组中的共同元素
# z1=np.random.randint(0,10,10)
# z2=np.random.randint(0,10,10)
# print(np.intersect1d(z1,z2))
