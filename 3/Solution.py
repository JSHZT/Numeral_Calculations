import numpy as np
from matplotlib import pyplot as plt

class Interpolation(object):
    def __init__(self, data):
        self.data = np.array(data, dtype=np.float32)
        self.data_x = self.data[:, 0]
        self.data_y = self.data[:, 1]
    
    def Lagrange(self, target_x):
        predict = 0
        if target_x in self.data_x:
            return self.data_y[np.where(self.data_x == target_x)]
        for i in range(len(self.data_x)):
            af = 1.0
            for j in range(len(self.data_x)):
                if j != i:
                    af *= (1.0 * (target_x - self.data_x[j]) / (self.data_x[i] - self.data_x[j]))
            predict += self.data_y[i] * af
        return predict

    def DivedeLine(self, target_x):
        if target_x in self.data_x:
            return self.data_y[np.where(self.data_x == target_x)]
        # index = 0
        for j in range(len(self.data_x)):
            if self.data_x[j] < target_x and self.data_x[j+1] > target_x:
                # index = j
                break
        predict = 1.0 * (target_x - self.data_x[j]) * (self.data_y[j+1] - self.data_y[j]) / (self.data_x[j+1] - self.data_x[j]) + self.data_y[j]
        return predict
    
    def calF(self):
        F = [1] * (len(self.data))
        FM = []
        for i in range(len(self.data)):
            FME = []
            if i == 0:
                FME = self.data_y
            else:
                for j in range(len(FM[len(FM) - 1]) - 1):
                    delta = self.data_x[i + j] - self.data_x[j]
                    value = 1.0 * (FM[len(FM) - 1][j + 1] - FM[len(FM) - 1][j]) / delta
                    FME.append(value)
            FM.append(FME)
        F = [FME[0] for FME in FM]
        # print(FM)
        return F

    def NT(self, target_x):
        F = self.calF()
        predict = 0
        if target_x in self.data_x:
            return self.data_y[np.where(self.data_x == target_x)]
        else:
            for i in range(len(self.data_x)):
                Eq = 1
                if i != 0:
                    for j in range(i):
                        Eq = Eq * (target_x - self.data_x[j])
                    predict += (F[i] * Eq)
        return predict

    def plot_NT(self, nums):
        Area = [min(self.data_x), max(self.data_x)]
        X = [Area[0] + 1.0 * i * (Area[1] - Area[0]) / nums for i in range(nums)]
        X[len(X) - 1] = Area[1]
        Y = [self.NT(x) for x in X]  
        plt.plot(X, Y, label='Newton', color = 'yellow')
        for i in range(len(self.data_x)):
            plt.plot(self.data_x[i], self.data_y[i], 'ro', color='blue')
        # plt.savefig('Newton.jpg')
        # plt.show()

    def plot_LG(self, nums):
        Area = [min(self.data_x), max(self.data_x)]
        X = [Area[0] + 1.0 * i *(Area[1] - Area[0]) / nums for i in range(nums)]
        X[len(X)-1] = Area[1]
        Y = [self.Lagrange(x) for x in X]
        plt.plot(X, Y, label='Lagrange', color= 'red')
        for i in range(len(self.data_x)):
            plt.plot(self.data_x[i], self.data_y[i], 'ro', color = 'blue')
        # plt.savefig('LG.jpg')
        # plt.show()
    
    def plot_D(self, nums):
        Area = [min(self.data_x), max(self.data_x)]
        X = [Area[0] + 1.0 * i *(Area[1] - Area[0]) / nums for i in range(nums)]
        X[len(X)-1] = Area[1]
        Y = [self.DivedeLine(x) for x in X]
        plt.plot(X, Y, label='DivedeLine', color= 'green')
        for i in range(len(self.data_x)):
            plt.plot(self.data_x[i], self.data_y[i], 'ro', color = 'blue')

    def plot(self, name, nums):
        plt.title("Comparison of three interpolation methods")
        plt.xlabel('x')
        plt.ylabel('y')
        self.plot_NT(nums)
        self.plot_LG(nums)
        self.plot_D(nums)
        plt.legend(loc='lower right')
        plt.savefig(name +'.jpg')
        plt.show()
        
if __name__ == "__main__":
    data_x = np.array([-5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 
              0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
    data_y1 = np.array([-0.1923, -0.2118, -0.2353, -0.2642, -0.3, -0.3448, -0.4000, -0.4615, -0.5000, -0.4000,
                0, 0.4000, 0.5000, 0.4615, 0.4000, 0.3448, 0.3000, 0.2642, 0.2353, 0.2118, 0.1923])
    data_y2 = np.array([0.0016, 0.002, 0.0025, 0.0033, 0.0044, 0.0064, 0.0099, 0.0175, 0.0385, 0.1379,
                1.0000, 0.1379, 0.0385, 0.0175, 0.0099, 0.0064, 0.0044, 0.0033, 0.0025, 0.0020, 0.0016])
    data1 = np.column_stack([data_x, data_y1])
    data2 = np.column_stack([data_x, data_y2])
    dataset1 = Interpolation(data1)
    dataset2 = Interpolation(data2)
    dataset1.plot("dataset1", 1000)
    dataset2.plot("dataset2", 1000)