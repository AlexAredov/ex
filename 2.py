import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(nrows= 1 , ncols= 2)
fig. suptitle('Two plots')

x = np.arange(-2, 2, 0.2)
y = np.tan(3*x)-np.sin(2*x)
z = np.sin(x)*np.cos(x)

axs[0].plot(x, y)
axs[1].plot(x, z)

axs[0].grid(True)
axs[1].grid(True)
plt.show()