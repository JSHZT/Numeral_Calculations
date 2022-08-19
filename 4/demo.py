from Solution import Solution
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import leastsq
from math import *


def dist(a, fun, x, y):
    return fun(x, a) - y

if __name__ == "__main__":
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    
    x = np.arange(1994, 2004, 1, dtype='int')
    y = np.array([67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777], dtype='float')
    solution = Solution()
    
    plt.figure()
    plt.title(u'石油产量年变化')
    plt.xlabel(u'年份')
    plt.ylabel(u'百万桶/天')
    
    plt.grid(True)
    plt.plot(x, y, 'k.')
    
    funs = [solution.line_fun, solution.quadratic_fun, solution.cubic_fun]
    colors = ['blue', 'red', 'black', 'green']
    fun_name = ['line_fun', 'quadratic_fun', 'cubic_fun']
    
    param0 = [0, 0]
    param1 = [0, 0, 0]
    param2 = [0, 0, 0, 0]
    params = [param0, param1, param2]
    process_ = []
    
    for i, (func, param, color, name) in enumerate(zip(funs, params, colors, fun_name)):
        var = leastsq(dist, param, args=(func, x, y))
        process_.append(var[0])
        plt.plot(x, func(x, var[0]), color)
        # 打印问题二的东西
        print('[%s] 二范数：%.4f, abs(bias)：%.4f, bias_std：%.4f' %(name,
            ((y-func(x, var[0]))**2).sum(),
            (y-func(x, var[0])).std(),
            (abs(y-func(x, var[0]))).mean())
            )
    plt.legend(['line_fun', 'quadratic_fun', 'cubic_fun'], loc= 'upper left')
    print(process_) #打印各个函数的参数，写报告的时候要规范写回公式
    plt.show()#拟合结果图
    # 打印2010预测值
    for i, (func, param, name) in enumerate(zip(funs, process_, fun_name)):
        print(name + ":::::::", func(2010, param))
