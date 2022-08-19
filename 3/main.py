import numpy as np
from Solution import Interpolation
from scipy.interpolate import lagrange
import sympy as sy

def f1(x):
    return (x ** 2) + 4 * x - 7

def f2(x):
    return -(2 * (x ** 3)) + 5 * (x ** 2) + x - 2

def NewtonInt(x_value, y_value):
    N = len(x_value)
    res = np.zeros((N, N))
    res[:, 0] = y_value
    for i in range(1, N): 
        for j in range(N - i): 
            res[j, i] = (res[j + 1, i - 1] - res[j, i - 1]) / (x_value[i + j] - x_value[j])

    print("\n 差商表:\n   {:^16}{:^16}".format("xi", "yi"), end="")
    for i in range(1, N):
        print("{:^14}".format("{:2d}阶差商".format(i)), end="")
    print("")
    for i in range(N):  # i 阶
        print("%16.4E" % (x_value[i]), end="")
        for j in range(i + 1):  # j 个
            print("%16.4E" % res[i - j, j], end="")
        print("")
    str_Nx = ""
    for i in range(N):  # i 阶
        str_Nx += "%f" % res[0, i]
        for j in range(i):  # j 个
            str_Nx += "*(x- %f)" % x_value[j]
        str_Nx += " + "
    return sy.simplify(str_Nx[0:-3])

def R(dataset, x, f, phi=0): 
    n = len(dataset.data_x)
    for i in range(n):
        X, Y = 1, 1
        for j in range(n):
            if i != j:
                X = X * (x - dataset.data_x[j])
                Y = Y * (dataset.data_x[i] - dataset.data_x[j])
        phi += X / Y * dataset.data_y[i]
    return f(x) - phi

def q1():
    x1_list = [0, 1, 2]
    x2_list = [0, 1, 2, 3]
    y1_list = [f1(x) for x in x1_list]
    y2_list = [f2(x) for x in x2_list]
    dataset1 = Interpolation(np.column_stack([x1_list, y1_list]))
    dataset2 = Interpolation(np.column_stack([x2_list, y2_list]))
    
    res1 = lagrange(dataset1.data_x, dataset1.data_y)
    res2 = lagrange(dataset2.data_x, dataset2.data_y)
    print(res1)
    print(res2)

    r1 = R(dataset1, 5, f1)
    print(r1)
    r2 = R(dataset2, 7, f2)
    print(r2)
    return

def q6():
    data1 = [[0, 1], [1, 2], [2, 3]]
    data2 = [[1, 0], [3, 2], [4, 15], [7, 12]]
    dataset1 = Interpolation(data1)
    dataset2 = Interpolation(data2)
    res1 = lagrange(dataset1.data_x, dataset1.data_y)
    res2 = lagrange(dataset2.data_x, dataset2.data_y)
    print(res1)
    print(res2)
    
    Nx1= NewtonInt(dataset1.data_x, dataset1.data_y)
    print(Nx1)
    
    Nx2= NewtonInt(dataset2.data_x, dataset2.data_y)
    print(Nx2)
    
    return

if __name__ == "__main__":
    # q4()
    q6()