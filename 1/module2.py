from concurrent.futures import process
from math import sqrt, pow
import time
import csv
class Solution(object):
    def Equation_solving_by_iteration(self, x0, strings, epsilon = 10**(-5), clockup_way=None):
        return self.get_res(self, strings, x0, epsilon, clockup_way)
        # with open('output.csv', 'w', encoding='utf-8-sig', newline='') as fp:
        #     write = csv.writer(fp)
        #     for i in process_1:
        #         write.writerow(i)
        #     write.writerow('----------')    

    def get_res_clockup(self, clockup_way, strings, x0, epsilon = 10**(-5)):
        def aitken(xn, x_n1, x_n2):
            ans =xn - (((xn - x_n1)**2)/(xn - 2 * x_n1 + x_n2)) 
            return ans
        def steffensen(x):
            temp = self.get_res_one(strings, x)
            ans = x - ((temp - x)**2)/(self.get_res_one(strings, temp) - 2 * temp + x)
            return ans
        if clockup_way == 'aitken':
            xn_2 = x0
            xn_1_hat = xn_1 = self.get_res_one(strings, xn_2)
            xn = self.get_res_one(strings, xn_1)
            xn_hat = aitken(xn, xn_1, xn_2)
            cnt = 1
            process = [[0, x0], [1, xn_1_hat]]
            while abs(xn_hat - xn_1_hat) >= epsilon or cnt < 15:
                cnt += 1
                xn_1_hat = xn_hat
                xn_2 = xn_1
                xn_1 = xn
                try:
                    xn = self.get_res_one(strings, xn_1)
                    xn_hat = aitken(xn, xn_1, xn_2)
                    process.append([cnt, xn_hat])
                except:
                    return process
        elif clockup_way == 'steffensen':
            x_last = x0
            x_new = steffensen(x0)
            cnt = 1
            process = [[0, x0], [1, x_new]]
            while abs(x_new - x_last) >= epsilon or cnt < 15:
                x_last = x_new
                try:
                    x_new =steffensen(x_new)
                    cnt += 1
                    process.append([cnt, x_new])
                except:
                    return process
        else:
            return []
        return process
    
    def get_res(self, strings, x0, epsilon = 10**(-5), clockup_way = None):
        if strings != '1' and strings != '2' and strings != '3' and strings != '4' and strings != '5':
            return []
        elif clockup_way != None:
            process = self.get_res_clockup(clockup_way, strings, x0, epsilon)
            return process
        cnt = 1
        new_x = self.get_res_one(strings, x0)
        process = [[0, x0], [1, new_x]]
        last_x = x0
        while abs(new_x - last_x) >= epsilon or cnt < 15:
            last_x = new_x
            try:
                new_x = self.get_res_one(strings, new_x)
                cnt += 1
                process.append([cnt, new_x])
            except:
                return process
        return process
    
    def get_res_one(self, strings, x):
        def iterative_scheme_1(x):
            ans = 7 * x**5 - 13 * x**4 - 21 * x**3 - 12 * x**2 + 59 * x + 3
            return ans
        
        def iterative_scheme_2(x):
            ans = pow((13 * x**4 + 21 * x**3 + 12 * x**2 - 58 * x - 3) / 7, 1/5)
            return ans
        
        def iterative_scheme_3(x):
            ans = (13 + (21 / x) + (12 / x**2) - (58 / x**3) - (3 / x**4)) / 7
            return ans
        
        def iterative_scheme_4(x):
            ans = pow((((12 * x**2) - (58 * x) - 3)/((7 * x**2) - (13 * x) -21)), 1/3)
            return ans
        
        def iterative_scheme_5(x):
            ans = sqrt(((-58 * x) - 3)/((7 * x**3) - (13 * x**2) - (21 * x) - 12))
            return ans
        
        if strings == '1':
            ans = iterative_scheme_1(x)
        elif strings == '2':
            ans = iterative_scheme_2(x)
        elif strings == '3':
            ans = iterative_scheme_3(x)
        elif strings == '4':
            ans = iterative_scheme_4(x)
        elif strings == '5':
            ans = iterative_scheme_5(x)
        else:
            return None
            
        return ans

    def newton(self, x0, epsilon = 10**(-5)):
        def fn(x):
            return 7 * x**5 - 13 * x**4 - 21 * x**3 - 12 * x**2 + 58 * x + 3
        def fx_1(x):
            return 35 * x**4 - 52 * x**3 - 63 * x**2 - 24 * x + 58
        last_x = x0
        new_x = x0 - fn(x0)/fx_1(x0)
        cnt = 1
        process = [[0, x0], [1, new_x]]
        while abs(new_x - last_x) >= epsilon or cnt < 15:
            cnt += 1
            last_x = new_x
            new_x = new_x - fn(new_x)/fx_1(new_x)
            process.append([cnt, new_x])
        return process
    
    def secant(self, strings, x1, x2, epsilon = 10**(-5)):
        def fn(x):
            return 7 * x**5 - 13 * x**4 - 21 * x**3 - 12 * x**2 + 58 * x + 3
        def secant_OnePoint(xn, x0):
            return xn - (fn(xn) * ((xn-x0)/(fn(xn)-fn(x0))))
        def secant_dp(xn, xn_1):
            return xn - (((fn(xn)) * (xn - xn_1))/(fn(xn) - fn(xn_1)))
        if strings == 'OnePoint':
            last_x = x1
            new_x = secant_OnePoint(x2, x1)
            cnt = 2
            process = [[0, x1], [1, x2], [2, new_x]]
            while abs(new_x - last_x) >= epsilon or cnt < 15:
                cnt += 1
                try:
                    new_x = secant_OnePoint(new_x, x1)
                    last_x = new_x
                    process.append([cnt, new_x])
                except:
                    return process
        elif(strings == 'dp'):
            last_x = x2
            new_x = secant_dp(x2, x1)
            cnt = 2
            process = [[0, x1], [1, x2], [2, new_x]]
            while abs(new_x - last_x) >= epsilon or cnt < 15:
                cnt += 1
                try:
                    new_x = secant_dp(new_x, last_x)
                    last_x = new_x
                    process.append([cnt, new_x])
                except:
                    return process
        else:
            return []
        return process
    
    def T2_fx(self, x):
        fx = 7 * x**5 - 13 * x**4 - 21 * x**3 - 12 * x**2 + 58 * x + 3
        return fx
    
    def test_2(self, left, right):
        le = []
        ri = []
        Mid = []
        rsl = []
        limit = 10**(-5)
        while abs(left - right) >= limit:
            le.append(left)
            ri.append(right)
            mid = left + ((right - left) / 2)
            Mid.append(mid)
            rsl.append(self.T2_fx((right-left)/2))
            temp_mid = self.T2_fx(mid)
            temp_l = self.T2_fx(left)
            temp_r = self.T2_fx(right)
            if temp_mid == 0:
                break
            elif temp_r * temp_mid < 0:
                left = mid
            elif temp_l * temp_mid < 0:
                right = mid
        return le, ri, Mid, rsl

        
if __name__ == '__main__':
    process_1 = Solution().Equation_solving_by_iteration(1.5, '2', 10**(-5), clockup_way='steffensen') ##example
    le, ri, mid, rsl = Solution().test_2(1.5, 2)
    process_2 = Solution().newton(1.5)
    process_3 = Solution().secant('dp', 1.5, 2)
    #some deal function
