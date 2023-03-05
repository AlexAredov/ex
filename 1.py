import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)
y = -0.17*x**3 - 0.14*x**2 + 6.13*x + 18.48
plt.plot(x, y)
plt.grid(True)
plt.show()