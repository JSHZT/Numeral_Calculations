import math
ERF_NAN = 0x00000001
ERF_INF = 0x00000002
ZERO = 0.0
rootCount = 0

def compute_(a, b, c, rootCount):
    x = [0]*2
    EPS = 1
    if(abs(a - 0.0) < EPS):
	    if (abs(b - 0.0) > EPS):
            x[0] = -c / b
            rootCount = 1
    else:
        b /= a
        c /= a
        a = 1.0
        delta = b * b - 4.0 * a * c
        if (delta > ZERO):
            if (abs(c - 0.0) < EPS):	
                x[0] = 0.0
                x[1] = -b / a
            else:
                sqrtDelta = math.sqrt(delta)
                if (b > 0.0):
                    x[0] = (-2.0 * c) / (b + sqrtDelta)
                    x[1] = (-b - sqrtDelta) / (2.0 * a)
                else:
                    x[0] = (-b + sqrtDelta) / (2.0 * a)
                    x[1] = (-2.0 * c) / (b - sqrtDelta)
            rootCount = 2
        elif (abs(delta - 0.0) < EPS):
            x[0] = x[1] = -b / (2.0 * a)
            rootCount = 2
        else:
            rootCount = 0
    return x, rootCount
