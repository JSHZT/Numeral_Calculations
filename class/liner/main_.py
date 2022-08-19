from __future__ import division
import numpy as np
import math


def swap(a, b, k, n):  # 找到主元并交换，这仅是一个仅用来交换的函数
    ans = 0
    maxn = 0
    for i in range(k, n):
        if ans < np.fabs(a[i][k]):  # fabs是绝对值，将a中绝对值最大的找出来
            ans = a[i][k]
            maxn = i
    a[[k, maxn], :] = a[[maxn, k], :]  # 交换
    b[k], b[maxn] = b[maxn], b[k]


def LU(a, b):
    n, m = a.shape
    if (n != m):
        print("错误类型")
        return 0
    L = np.eye(n)
    Xarray = [0] * n
    Yarray = [0] * n

    for k in range(n - 1):
        l = np.eye(n)
        for i in range(k + 1, n):
            L[i][k] = a[i][k] / a[k][k]
            l[i][k] = -L[i][k]
        a = np.dot(l, a)
    Yarray[0] = b[0]
    for i in range(1, n):
        for j in range(n):
            b[i] -= L[i][j] * Yarray[j]
        Yarray[i] = b[i]
    Xarray[n - 1] = Yarray[n - 1] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        for j in range(n):
            Yarray[i] -= a[i][j] * Xarray[j]

        Xarray[i] = Yarray[i] / a[i][i]
    print(Xarray)
    return 0


def Gauss_Jordan(a, b):
    n, m = a.shape
    if (n != m):
        print("错误类型")
        return 0
    for k in range(n):
        swap(a, b, k, n)

        l = a[k][k]
        for i in range(k, n):
            a[k][i] = a[k][i] / l

        b[k] = b[k] / l
        for i in range(n):
            if (i != k):
                q = a[i][k] / a[k][k]
                for j in range(n):
                    a[i][j] -= a[k][j] * q

                b[i] -= b[k] * q

    print(a)
    print(b)
    return 0


def Norm(a, type):
    m, n = a.shape
    if (type == 1):
        Aarry = []
        for i in range(m):
            A = 0
            for j in range(n):
                A += abs(a[i][j])
            Aarry.append(A)
        Aarry.sort()
        # print("列和范数为： {}".format(Aarry[n-1]))
        return Aarry[n - 1]
    if (type == 8):
        Aarry = []
        for i in range(m):
            A = 0
            for j in range(n):
                A += abs(a[j][i])
            Aarry.append(A)
        Aarry.sort()
        # print("行和范数为： {}".format(Aarry[ - 1]))
        return Aarry[- 1]
    if (type == 2):
        m, v = np.linalg.eig(np.mat(a) * np.mat(a.T))
        m.sort()
        r = m[-1]
        # print(math.sqrt(r))
        return math.sqrt(r)
    return 0


def Cond(a):
    m, n = a.shape
    cot = 0
    for i in range(m):
        for j in range(n):
            if (a[i][j] == a[j][i]):
                continue
            cot = 1
    if (cot == 0):  ##该矩阵为对称矩阵
        r, v = np.linalg.eig(a)
        r.sort()
        # print( "Cond(A)2的值为：{}".format(r[-1]/r[0]))
        return r[-1] / r[0]
    else:
        r, v = np.linalg.eig(np.mat(a) * np.mat(a.T))
        r.sort()
        # print("Cond(A)2的值为：{}".format(math.sqrt(r[-1]/r[0])))
        return math.sqrt(r[-1] / r[0])
    return 0


# 第七题
# Norm
# a = np.array([[-2,1,0,0],[1,-2,1,0],[0,1,-2,1],[0,0,1,-2]])
# Norm(a,2)
# #Cond
# Cond(a)


# 第二题
##LYZGauss
# a = np.array([[2.51, 1.48, 4.53], [1.48, 0.93, -1.3], [2.68, 3.04, -1.48]])
# b = np.array([0.05, 1.03, -0.53])
# LZYgaussin(a, b)


##Gauss
# a1 = np.array([[2.51, 1.48, 4.53], [1.48, 0.93, -1.3], [2.68, 3.04, -1.48]])
# b1 = np.array([0.05, 1.03, -0.53])
# Gaussin(a1,b1)

# 第三题
##LU
# a = np.array([[1, 3, 1], [1, 2, 4, ], [5, 1, 2]])
# LU(a, [10, 17, 13])


##Gauss_jordan
# a = np.array([[2.0,-1.0,3.0],[4.0,2.0,5.0],[1.0,2.0,0.0]])
# Gauss_Jordan(a,[1.0,4.0,7.0])

# 第八题
a = np.array([[10.0, 7.0, 8.0, 7.0], [7.0, 5.0, 6.0, 5.0], [8.0, 6.0, 10.0, 9.0], [7.0, 5.0, 9.0, 10.0]])
at = np.array([[10.0, 7.0, 8.0, 7.0], [7.0, 5.0, 6.0, 5.0], [8.0, 6.0, 10.0, 9.0], [7.0, 5.0, 9.0, 10.0]])
b = np.array([32.0, 23.0, 33.0, 31.0])
br = np.array([32.1, 22.9, 33.1, 30.9])
x = LU(a, b)
xr = LU(at, br)
