import numpy as np
from Solution import Interpolation
from scipy.interpolate import lagrange

def f1(x):
    return (x ** 2) + 4 * x - 7

def f2(x):
    return -(2 * (x ** 3)) + 5 * (x ** 2) + x - 2

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
    
    a = lagrange(dataset1.data_x, dataset1.data_y)
    b = lagrange(dataset2.data_x, dataset2.data_y)
    print(a)
    print(b)

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
    
    
    return

if __name__ == "__main__":
    # q4()
    q6()