import numpy as np

def newton(f, J, x, eps = 0.03):
    fx = f(x)
    while np.linalg.norm(fx) > eps:
        x = x - np.linalg.inv(J(x)) @ fx
        fx = f(x)
    return x, fx
def f(x):
    x, y = x
    return np.array([
        np.sqrt(0.16-(x/3)**2)+y,
        np.cos(x)+y-0.5
    ])
def J(x):
    x, y = x
    return np.array([
        [-(5*x)/(3*np.sqrt(36-35*x**2)), 1],
        [np.sin(x), 1]
    ])

x, y = newton(f, J, [0.3, 0.3])
print(x, y, sep="\n")