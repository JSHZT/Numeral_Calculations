#import numpy as np
import math

def Aitken(x0,epsilon,iternum,phi):#初值，精度要求，最大迭代次数,迭代函数
    xk_1 = x0
    for i in range(iternum):
        y = phi(xk_1)
        z = phi(y)
        if (z - 2*y +xk_1)!= 0:
            xk = xk_1 - (y - xk_1)**2 / (z - 2*y +xk_1)
            print("第",i+1,"次迭代 ","xk=",xk,"  xk-1=",xk_1,"  |xk - xk-1|=",abs(xk-xk_1))
            if abs(xk-xk_1)<epsilon:
                return xk
            else:
                xk_1 = xk
        else:
            return x0
    return 0
def phi(x): 
    return 7*x**5-13*x**4-21*x**3-12*x**2+58*x+3
    
Aitken(1.5,1/(10)**5,5,phi)#初值1.5，精度10^-5,最大迭代次数为5