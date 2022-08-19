import numpy as np
import csv

class Hilbert():
    def __init__(self, n):
        self.n = n
        self.A = self.get_H(n)
    
    def __set__(self, n):
        self.n = n
        self.A = self.get_H(n)
        
    def get_H(self, n):
        x = 1. / (np.arange(1, n+1) + np.arange(0, n)[:, np.newaxis])
        return x

    def is_convergence_GS(self, B):
        eigenvalue, _ = np.linalg.eig(B)
        return True if np.max(np.abs(eigenvalue)) < 1 else False
    
    def is_convergence_J(self, B):
        eigenvalue, _ = np.linalg.eig(B)
        return True if np.max(np.abs(eigenvalue)) < 1 else False

    def iteration_GS(self, epsilon=1.0E-5):
        b = np.dot(self.A, np.array([[1] * self.n]).T)
        D = np.diag(np.diag(self.A))
        L = np.tril(self.A, k=0) - D
        U = np.triu(self.A, k=0) - D
        B = np.dot(-np.linalg.inv(D + L), U)
        if not self.is_convergence_GS(B):
            return (self.n, None, 0)
        g = np.dot(np.linalg.inv(D + L), b)
        x0 = np.array([[0] * self.n]).T
        ans = np.dot(B, x0) + g
        m = 1
        while np.max(np.abs(ans - x0)) >= epsilon:
            x0 = ans
            m += 1
            ans = np.dot(B, ans) + g
        return (self.n, np.squeeze(np.round(ans.T, 3)), m)

    def iteration_J(self, epsilon=1.0E-5):
        LU = self.A
        row, col = np.diag_indices_from(self.A)
        LU[row, col] = 0
        D = -np.linalg.inv(self.A)
        B = np.dot(D, LU)
        if not self.is_convergence_J(B):
            return (self.n, None, 0)
        b = np.dot(self.A, np.array([[1] * self.n]).T)
        g = np.dot(np.linalg.inv(D), b).T
        x0 = np.array([0] * self.n).T
        ans = np.dot(B, x0) + g
        m = 1
        while max(abs(ans - x0)) >= epsilon:
            x0 = ans
            m += 1
            ans = np.dot(B, ans) + g
        return (self.n, np.squeeze(np.round(ans.T, 3)), m)

def col_Gauss_Jordan(A, n):
    A = np.mat(A)
    b = np.mat(np.dot(A, np.array([[1] * n]).T))
    mat = np.hstack((A, b))
    for i in range(0, mat.shape[0]):
        if mat[i,i] == 0:
            break
        else:
            current_column  = mat[i:,i] 
            max_index = np.argmax(current_column) + i
            mat[[i,max_index],:] = mat[[max_index,i],:] 
            mat[i,:] = mat[i,:] / mat[i, i]   
            for j in range(0, i):
                mat[j,:] = mat[j,:] - mat[j,i] * mat[i,:] 
            for k in range(i+1, mat.shape[0]):
                mat[k,:] = mat[k,:] - mat[k,i] * mat[i,:]
    ans = np.mat(np.zeros(mat.shape[0],dtype=float))
    n = ans.shape[1]-1
    ans[0, n] = mat[n,n+1]/mat[n,n]
    for i in range(n):
        n -= 1
        ans[0,n] = (mat[n, mat.shape[1]-1] - np.sum(np.multiply(ans[0, n+1:], mat[n,n+1:mat.shape[1]-1])))/mat[n,n]
    return np.round(ans, 3)
    
    
if __name__ == "__main__":
    demo = Hilbert(2)
    process_Gauss = []
    process_Gauss.append((2, col_Gauss_Jordan(demo.A, 2)))
    
    # process_GS = []
    # process_J = []
    # process_GS.append(demo.iteration_GS())
    # process_J.append(demo.iteration_J())
    for i in range(3, 13):
        demo.__set__(i)
    #     process_GS.append(demo.iteration_GS())
        process_Gauss.append((i, col_Gauss_Jordan(demo.A, i)))
        print(i)
    
    with open('output.csv', 'w', encoding='utf-8-sig', newline='') as fp:
             write = csv.writer(fp)
             for i in process_Gauss:
                 write.writerow(i)  
    print("OK")