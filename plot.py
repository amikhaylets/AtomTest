#Practicing in plotting with matplotlib
#Import pyplot from matpotlib package
import numpy as np
import ggplot as gp
from matplotlib import pyplot as plt

x = np.arange(0, 1, 0.05)
y = np.power(x, 2)

plt.scatter(x, y)
plt.grid(b='on')
plt.show()

gp.qplot(x, y)
help(plt.grid)
