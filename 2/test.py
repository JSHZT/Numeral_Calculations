import numpy as np

def iteration_GS(A, n, epsilon=1.0E-5):
    b = np.array([3, 15, 10])
    D = np.diag(np.diag(A))
    L = np.tril(A, k=0) - D
    U = np.triu(A, k=0) - D
    B = np.dot(-np.linalg.inv(D + L), U)
    g = np.dot(np.linalg.inv(D + L), b).T
    x0 = np.array([0] * n).T
    ans = x0
    m = 0
    while max(abs(ans - x0)) <= epsilon:
        x0 = ans
        m += 1
        ans = np.dot(B, ans) + g
    return ans

A = np.array([[10, -2, -3],
              [-2, 10, -1],
              [-1, -2, 5]])
n = 3
ans = iteration_GS(A, n)