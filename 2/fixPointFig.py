from matplotlib import pyplot as plt
import numpy as np

class fixPointFig():
    def __init__(self, func, x0):
        self.func = func
        self.x0 = x0
    
    def fixpt(self, epsilon=1.0E-5, N=500, store=False):
        y = self.func(self.x0)
        n = 0
        if store:
            Values = [(self.x0, y)]
        while abs(y-self.x0) >= epsilon and n < N:
            self.x0 = self.func(self.x0)
            n += 1
            y = self.func(self.x0)
            if store:
                Values.append((self.x0, y))
        if store:
            return y, Values
        else:
            if n >= N:
                return "No fixed point for given start value"
            else:
                return self.x0, n, y

    def plot(self):
        res, points = solution.fixpt(store = True)

        xx = np.arange(1.2, points[0][0]+2*(points[0][0]-points[0][1]), 1e-5)

        plt.plot(xx, self.func(xx), 'b')
        plt.plot(xx, xx, 'r')
        plt.legend()

        i = 0
        for x, y in points:
            i += 1
            plt.title("{} iteration".format(i))
            plt.xlabel("x")
            plt.ylabel("y")
            plt.plot([x, x], [x, y], 'g')
            plt.text(x, y, [round(x, 3), round(y, 3)])
            plt.pause(0.5)
            
            plt.xlim(x-2*(x-y), x+2*(x-y))
            plt.ylim(x-2*(x-y), x+2*(x-y))
            
            plt.plot([x, y], [y, y], 'g')
            plt.text(x, y, [round(x, 3), round(y, 3)])
            plt.pause(0.5)

        plt.show()

def f(x):
    return ((-58 * x - 3) / (7 * x ** 3 - 13 * x ** 2 - 21 * x - 12)) ** (1 / 2)

solution = fixPointFig(f, 1.5)
solution.plot()



    
    
    
    