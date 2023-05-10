import numpy as np

def quad(f, a, b, n):
    res = 0
    h = (b - a)/n
    for i in range(n): res += f(a + h*i)
    return res


f = lambda x: np.cos(x)/(x+1)

a, b = 0.5, 1.5

res = quad(f, a, b, 100)
print(res)