from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
ax = axes3d.Axes3D(plt.figure())
i = np.arange(-2, 2, 0.5)
x, y = np.meshgrid(i, i)
z = 3*(x-5)**2+3*(y-5)**2
ax.plot_wireframe(x, y, z, rstride=1, cstride=1)
plt.show()