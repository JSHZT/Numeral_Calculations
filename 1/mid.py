from math import *
import time
import csv
class Solution(object):
    def fast_Exponentiation(a, n):
        ans = 1
        while n != 0:
            if n & 1:
                ans *= a
            a *= a
            n >> 1
        return ans
    
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
    le, ri, Mid, rsl = Solution().test_2(1, 2)
    with open('output.csv', 'w', encoding='utf-8-sig', newline='')as fp:
        write = csv.writer(fp)
        for i in le:
            write.writerow([str(i)])
        write.writerow('----------')
        for i in ri:
            write.writerow([str(i)])
        write.writerow('----------')
        for i in Mid:
            write.writerow([str(i)])
        write.writerow('----------')
        for i in rsl:
            write.writerow([str(i)])
    