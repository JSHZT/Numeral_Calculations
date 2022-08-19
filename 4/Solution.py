import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import leastsq
from math import *

class Solution(object):
    def line_fun(self, x, s=[0, 0]):
        k1, b = s
        return k1 * x + b
    
    def quadratic_fun(self, x, s=[0, 0, 0]):
        k1, k2, b = s
        return k1 * x**2 + k2 * x + b
    
    def cubic_fun(self, x, s=[0, 0, 0, 0]):
        k1, k2, k3, b = s
        return k1 * x**3 + k2 * x**2 + k3 * x + b
    
    def fpower_fun(self, x, s=[0, 0, 0, 0, 0]):
        k1, k2, k3, k4, b = s
        return k1 * x**4 + k2 * x**3 + k3 * x**2 + k4 * x + b
    
    def myfuns(self, x, s=[0, 0, 0]):
        a, b, c = s
        return a * np.exp(-b*(x-c))

if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    solution = Solution()
    
    x = np.arange(0, 25, 1, dtype='float')
    y = np.array([15, 14, 14, 14, 14, 15, 16, 18, 20, 22, 23, 25,
                28, 31, 32, 31, 29, 27, 25, 24, 22, 20, 18, 17, 16], dtype='float')

    plt.figure()
    plt.title(u'某天的气温变化')
    plt.xlabel(u't/h')
    plt.ylabel(u'T/摄氏度')

    plt.axis([0, 24, 10, 35])
    plt.grid(True)
    plt.plot(x, y, 'k.')
    # plt.show()
    param0 = [0, 0, 0]
    param1 = [0, 0, 0, 0]
    param2 = [0, 0, 0, 0, 0]
    param3 = [0, 0, 0]
    

    def dist(a, fun, x, y):
        return fun(x, a) - y

    funs = [solution.quadratic_fun, solution.cubic_fun, solution.fpower_fun, solution.myfuns]
    params = [param0, param1, param2, param3]
    colors = ['blue', 'red', 'black', 'green']
    fun_name = ['quadratic_fun', 'cubic_fun', '4power_fun', 'a*exp(-b*(t-c))']

    for i, (func, param, color, name) in enumerate(zip(funs, params, colors, fun_name)):
        var = leastsq(dist, param, args=(func, x, y))
        plt.plot(x, func(x, var[0]), color)
        print('[%s] 二范数：%.4f, abs(bias)：%.4f, bias_std：%.4f' %(name,
            ((y-func(x, var[0]))**2).sum(),
            (y-func(x, var[0])).std(),
            (abs(y-func(x, var[0]))).mean())
            )
    plt.legend(['sample data', 'quadratic_fun', 'cubic_fun', '4power_fun', 'a*exp(-b*(t-c))'], loc= 'upper left')
    plt.show()