import numpy as np
A = np.array([[10,7,8,7],
              [7,5,6,5],
              [8,6,10,9],
              [7,5,9,10]
              ])

b_1 = np.array([[32],[23],[33],[31]])
b_2 = np.array([[32.1],[22.9],[33.1],[30.9]])
x_1 = np.linalg.solve(A, b_1)
x_2 = np.linalg.solve(A, b_2)

#误差矩阵
x_3 = x_2-x_1

#x_1的范数
x1N_2 = round(np.linalg.norm(x_1, ord=2), 3)
x1N_inf = round(np.linalg.norm(x_1, ord=np.inf), 3)
#x_3的范数
x3N_2 = round(np.linalg.norm(x_3, ord=2), 3)
x3N_inf = round(np.linalg.norm(x_3, ord=np.inf), 3)
#b_1的范数
b1N_2 = round(np.linalg.norm(b_1, ord=2), 3)
b1N_inf = round(np.linalg.norm(b_1, ord=np.inf), 3)
#b_2的范数
b2N_2 = round(np.linalg.norm(b_2, ord=2), 3)
b2N_inf = round(np.linalg.norm(b_2, ord=np.inf), 3)

#无穷范数解相对误差
fin_inf = (x3N_inf/x1N_inf)
#1-范数解的相对误差
fin_2 = (x3N_2/x1N_2)

#扰动方程右端与原右端相对误差
finb_inf = (b2N_inf/b1N_inf)

finb_2 = (b2N_2/b1N_2)

print('方程的解:\n',b_2)
print('无穷范数解相对误差:',fin_inf)
print('1-范数解的相对误差:',fin_2)
print('扰动方程右端与原右端相对误差(无穷范数):',finb_inf)
print('扰动方程右端与原右端相对误差(无穷范数):',finb_2)