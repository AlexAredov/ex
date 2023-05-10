import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3+2.391*x**2-8.989*x+8.899

def f_diff(x):
    return 3*x**2 + 4.782*x - 8.989

def pol_del(a, b, e):
    while abs(b-a)>2*e:
        x = (b+a)/2
        if f(a)*f(x)>0:
            a = x
        else:
            b = x
    x = (b+a)/2
    return x

def prost_it(a, b, e):
    if abs(f_diff(b))>abs(f_diff(a)):
        bb = -2/f_diff(b)
        x = b
    else:
        bb = -2/f_diff(a)
        x = a
    h = e+1
    while abs(h) > e:
        h = bb*f(x)
        x = x+h
    return x

def kos(x,e):
    h = e + 1
    while abs(h) > e:
        h = f(x)/f_diff(x)
        x = x - h
    return x

print(pol_del(-5, 5, 0.01))
print(prost_it(-5, 5, 0.01))
print(kos(-5, 0.01))
x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x**3+2.391*x**2-8.989*x+8.899)
plt.show()