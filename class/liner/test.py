import numpy as np

A = [[1, 0],
     [0, 1]]
B = [[4, 1],
     [2, 2]]
ans = np.dot(A, B)
ans_ = np.dot(np.mat(A), np.mat(B))

print(ans)
print(ans_)