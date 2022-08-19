import numpy as np
import sympy as sy


def NewtonInt(x_value, y_value):
    N = len(x_value)
    res = np.zeros((N, N))
    res[:, 0] = y_value
    for i in range(1, N):  # i 阶
        for j in range(N - i):  # j 个
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

x_v=np.array([0.0,1.0,2.0])
y_v=np.array([1.0,2.0,3.0])
# x_v=np.array([0,1,2,5,3])
# y_v=np.array([2,3,12,147,30])
res, Nx= NewtonInt(x_v,y_v)
x_v=np.array([1.0,3.0,4.0,7.0])
y_v=np.array([0.0,2.0,15.0,12.0])
res, Nx= NewtonInt(x_v,y_v)