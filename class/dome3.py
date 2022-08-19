import numpy as np
class fun(object):
    def gauss(a, b):
        m, n = a.shape  # m=矩阵的行数，n=矩阵的列数
        # 求上三角矩阵
        l = np.zeros((n, n))
        for i in range(n):
            # 限制条件
            if a[i][i] == 0:
                print("无法计算答案")
                break
        # j表示列
        for k in range(n - 1):  # 按列遍历（1到n-1列）
            for i in range(k + 1, m):  # 按行遍历（k+1到m行）
                l[i][k] = np.around(a[i][k]/a[k][k], 3)  # 精确到小数点后三位
                for j in range(k, n):
                    a[i][j] = np.around(a[i][j]-l[i][k] * a[k][j], 3)
                b[i] = np.around(b[i] - l[i][k] * b[k], 3)
        # 回代求出方程解
        x = np.zeros(n)
        x[n - 1] = np.around(b[n-1]/a[n-1][n-1], 3)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                b[i] -= a[i][j] * x[j]
            x[i] = np.around(b[i] / a[i][i], 3)
        print("x" " = ", x)

    def L_Gauss(a,b):
        m, n = a.shape  # m=矩阵的行数，n=矩阵的列数
        l = np.zeros((n, n))
        c = []
        # 求上三角矩阵
        for i in range(n):
            # 限制条件
            if a[i][i] == 0:
                print("无法计算答案")
                break
        # j表示列
        for k in range(n - 1):  # 按列遍历（1到n-1列）
            for x in range(k, m):
                c.append(abs(a[x][k]))
            max = np.argmax(c)
            tmp1 = np.copy(a[max])
            a[max] = a[k]
            a[k] = tmp1
            #交换b数组中的值
            tmp2 = b[max]
            b[max] = b[k]
            b[k] = tmp2
            c = []

            for i in range(k + 1, m):  # 按行遍历（k+1到m行）
                l[i][k] = np.around(a[i][k]/a[k][k], 3)  # 精确到小数点后三位
                for j in range(k, n):
                    a[i][j] = np.around(a[i][j]-l[i][k] * a[k][j], 3)
                b[i] = np.around(b[i] - l[i][k] * b[k], 3)

        # 回代求出方程解
        x = np.zeros(n)
        x[n - 1] = np.around(b[n-1]/a[n-1][n-1], 3)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                b[i] -= a[i][j] * x[j]
            x[i] = np.around(b[i]/a[i][i], 3)
        print("x" " = ", x)

#定义矩阵a，线性方程组的解矩阵b
a=np.array([[2.51,1.48,4.53],[1.48,0.93,-1.3],[2.68,3.04,-1.48]])
b=np.array([0.05,1.03,-0.53])
fun.gauss(a,b)
a=np.array([[2.51,1.48,4.53],[1.48,0.93,-1.3],[2.68,3.04,-1.48]])
b=np.array([0.05,1.03,-0.53])
fun.L_Gauss(a,b)



