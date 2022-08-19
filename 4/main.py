import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import leastsq
from math import *
from Equation import Solution

def q1():
    A_a = np.array([[2, 4], [3, -5], [1, 2], [2, 1]]) #系数矩阵
    A_a_ = (A_a.T).dot(A_a) #左乘系数矩阵转置
    b_a = np.array([11, 3, 6, 7]) #右端矩阵
    b_a_ = (A_a.T).dot(b_a) #左乘系数矩阵转置
    A_b = np.array([[1, -2, 4], [1, -1, 1], [1, 0, 0], [1, 1, 1], [1, 2, 4]])#系数矩阵
    A_b_ = (A_b.T).dot(A_b)    #左乘系数矩阵转置
    b_b = np.array([0, 1, 2, 1, 0]) #右端矩阵
    b_b_ = (A_b.T).dot(b_b) #左乘系数矩阵转置
    equation_a = Solution(A_a_, b_a_) #创建a正规方程组对象
    equation_b = Solution(A_b_, b_b_) #创建b正规方程组对象
    res_a = equation_a.col_Gauss_Jordan() #使用高斯若当法解正规方程
    res_b = equation_b.col_Gauss_Jordan() #使用高斯若当法解正规方程
    print(res_a) #打印结果
    print(res_b) #打印结果

def q2():
    #线性化方程为 1/y = c0/x + c1
    x = np.array([1, 2, 4, 5]) #原x的值
    x_1 = 1 / x #准备计算S1
    x_2 = 1 / (np.square(x)) #准备计算S2
    A = np.array([[len(x), np.sum(x_1)], [np.sum(x_1), np.sum(x_2)]])#计算正规方程的系数矩阵
    y = np.array([0.33, 0.40, 0.44, 0.45])#原y的值
    y_ = 1 / y #准备计算T0
    y_1 = np.array([np.sum(y_), np.sum(np.multiply(y_, x_1))])#计算T0和T1
    equation = Solution(A, y_1)#创建正规方程对象
    res = equation.col_Gauss_Jordan()#使用高斯若当法解正规方程
    
    print(len(x))#打印S0
    print(np.sum(x_1)) #打印S1
    print(np.sum(x_2)) #打印S1
    print(np.sum(y_))#打印T0
    print(np.sum(np.multiply(y_, x_1)))#打印T1
    
    print(A) #打印系数矩阵
    print(y_1) #打印右端矩阵
    
    print(res)#[c0, c1]
    return
    
if __name__ == "__main__":
    q2()