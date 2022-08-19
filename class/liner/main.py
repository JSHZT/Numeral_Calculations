import numpy as np
import Solution

def q1():
    A = [[2.51, 1.48, 4.53],
         [1.48, 0.93, -1.3],
         [2.68, 3.04, -1.48]]
    b = [0.05, 1.03, -0.53]
    equation = Solution.Solution(A, b)
    ans_Gauss = equation.Gauss()
    ans_colGauss = equation.Gauss(col = True)
    print(ans_Gauss)
    print(ans_colGauss)

def q2():
    A = [[1, 2, 1, -2],
         [2, 5, 3, -2],
         [-2, -2, 3, 5],
         [1, 3, 2, 3]]
    b = [4, 7, -1, 0]
    equation = Solution.Solution(A, b)
    ans_colGaussJordan = equation.col_Gauss_Jordan()
    ans_lu = equation.LU()
    print(ans_lu)
    print(ans_colGaussJordan)
    return

def q3():
    A = [[-2, 1, 0, 0],
         [1, -2, 1, 0],
         [0, 1, -2, 1],
         [0, 0, 1, -2]]
    matr = Solution.Solution(A=A)
    norm_1 = matr.norm(ord=1)
    norm_2 = matr.norm(ord=2)
    norm_inf = matr.norm(ord=np.inf)
    cond_2 = matr.norm(ord=2, cond=True)
    print(norm_1)
    print(norm_2)
    print(norm_inf)
    print(cond_2)
    
def q4():
    A =[[10.0, 7.0, 8.0, 7.0], 
        [7.0, 5.0, 6.0, 5.0], 
        [8.0, 6.0, 10.0, 9.0], 
        [7.0, 5.0, 9.0, 10.0]]
    b = [32.0, 23.0, 33.0, 31.0]
    b_error = [32.1, 22.9, 33.1, 30.9]
    equation = Solution.Solution(A, b)
    equation_error = Solution.Solution(A, b_error)
    ans_ = np.squeeze(equation.LU())
    ans_error = np.squeeze(equation_error.LU())
    delta_b = np.array(b_error) - np.array(b)
    delta_x = ans_error - ans_
    b_error1 = np.linalg.norm(delta_b, ord = 1)/np.linalg.norm(b, ord=1)
    berror_inf = np.linalg.norm(delta_b, ord = np.inf)/np.linalg.norm(b, ord=np.inf)
    ans_error1 = np.linalg.norm(delta_x, ord = 1)/np.linalg.norm(ans_, ord=1)
    ans_error_inf = np.linalg.norm(delta_x, ord=np.inf)/np.linalg.norm(ans_, ord = np.inf)
    print(ans_)
    print(ans_error)
    print(b_error1)
    print(berror_inf)
    print(ans_error1)
    print(ans_error_inf)
    

if __name__ == "__main__":
    # q1()
    # q2()
    # q3()
#     A = [[1, 2, 1, -2],
#          [2, 5, 3, -2],
#          [-2, -2, 3, 5],
#          [1, 3, 2, 3]]
#     b = [4, 7, -1, 0]
#     equation = Solution.Solution(A, b)
#     ans_colGaussJordan = equation.col_Gauss_Jordan()
    q4()