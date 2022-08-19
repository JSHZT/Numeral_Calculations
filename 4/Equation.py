from math import *
import numpy as np

# 先判断是否有解
# 解是否唯一
# 解的关系

class Solution(object):
    def __init__(self, A = None, b = None):
        self.A = np.mat(A, dtype=np.float32)
        self.b = np.mat(b, dtype = np.float32).T
        if A is not None and b is not None:
            self.mat = np.hstack((self.A, self.b))
    
    def have_sol(self):
        return np.linalg.matrix_rank(self.mat) == np.linalg.matrix_rank(self.A)
    
    def get_ans(self):
        ans = np.mat(np.zeros(self.mat.shape[0],dtype=float))
        n = ans.shape[1]-1
        ans[0, n] = self.mat[n,n+1]/self.mat[n,n]
        for i in range(n):
            n -= 1
            ans[0,n] = (self.mat[n, self.mat.shape[1]-1] - np.sum(np.multiply(ans[0, n+1:], self.mat[n,n+1:self.mat.shape[1]-1])))/self.mat[n,n]
        return ans
    
    def Gauss(self, col = False):
        if not self.have_sol():
            print("方程无解\n")
            return
        for i in range(0, self.mat.shape[0]-1):
            if self.mat[i,i] == 0:
                break
            else:
                if col:
                    current_column  = self.mat[i:,i] 
                    max_index = np.argmax(current_column) + i
                    self.mat[[i,max_index],:] = self.mat[[max_index,i],:]    
                self.mat[i+1:,:] = self.mat[i+1:,:] - (self.mat[i+1:,i] / self.mat[i,i]) * self.mat[i,:]
        ans = self.get_ans()
        self.mat = np.hstack((self.A, self.b))
        return ans

    def col_Gauss_Jordan(self):
        if not self.have_sol():
            print("方程无解\n")
            return
        for i in range(0, self.mat.shape[0]):
            if self.mat[i,i] == 0:
                break
            else:
                current_column  = self.mat[i:,i] 
                max_index = np.argmax(current_column) + i
                self.mat[[i,max_index],:] = self.mat[[max_index,i],:] 
                self.mat[i,:] = self.mat[i,:] / self.mat[i, i]   
                for j in range(0, i):
                    self.mat[j,:] = self.mat[j,:] - self.mat[j,i] * self.mat[i,:] 
                for k in range(i+1, self.mat.shape[0]):
                    self.mat[k,:] = self.mat[k,:] - self.mat[k,i] * self.mat[i,:]
        ans = self.get_ans()
        self.mat = np.hstack((self.A, self.b))
        return ans
    
    def LU(self):
        if not self.have_sol():
            print("方程无解\n")
            return
        n  = self.A.shape[0]
        L = np.eye(n)
        ans = [0] * n
        Yarray = [0] * n
        a = self.A.A
        b = self.b.A
        for k in range(n - 1):
            l = np.eye(n)
            for i in range(k + 1, n):
                L[i][k] = a[i][k] / a[k][k]
                l[i][k] = -L[i][k]
            a = np.dot(l, a)
        Yarray[0] = b[0][0]
        for i in range(1, n):
            for j in range(n):
                b[i][0] -= L[i][j] * Yarray[j]
            Yarray[i] = b[i][0]
        ans[n - 1] = Yarray[n - 1] / a[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(n):
                Yarray[i] -= a[i][j] * ans[j]
            ans[i] = Yarray[i] / a[i][i]
        return np.mat(ans)
    
    def norm(self, ord, cond = False):
        if cond == False:
            return np.linalg.norm(self.A, ord=ord)
        else:
            return np.linalg.cond(self.A, p=ord)