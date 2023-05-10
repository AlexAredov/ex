import matplotlib.pyplot as plt
import numpy as np

def lagrange(x, xs, ys):
    s = 0
    n = len(xs)
    for i in range(n):
        p=1
        for j in range(n):
            if i == j: continue
            p *= (x - xs[j])/(xs[i] - xs[j])
        s += ys[i] * p
    return s
    
xs = np.linspace(-2, -0.1, 100)
ys = 1244869/1244880*xs**3+531509/222300*xs**2-1119030769/124488000*xs-6086927/684000

x = np.array([-2, -1.3, -0.7, -0.1])
y = 1244869/1244880*x**3+531509/222300*x**2-1119030769/124488000*x-6086927/684000

yl = [lagrange(x_, x, y) for x_ in xs]

plt.plot(xs, ys, label="Действительное")
plt.plot(x, y, "o", label="Дискретное")
plt.plot(xs, yl, ls=":", c="r", label="Лагранж")

f = lambda x: 1244869/1244880*x**3+531509/222300*x**2-1119030769/124488000*x-6086927/684000
xs = np.linspace(-2,-0.1, 100)
ys = f(xs) + np.random.randn(xs.size)/4

arrs = (np.ones(xs.size), xs, xs**2)
P = np.stack(arrs, axis=-1)

a = np.linalg.inv(P.T @ P) @ (P.T @ ys)

yc = a[0]+a[1]*xs+a[2]*xs**2

plt.scatter(xs, ys, alpha=0.3)


plt.legend()
plt.show()