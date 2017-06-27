#Practicing in plotting with matplotlib
#Import pyplot from matpotlib package
import numpy as np
import ggplot as gp
from matplotlib import pyplot as plt

x = np.arange(0, 1, 0.05)
y = np.power(x, 2)

plt.scatter(x, y)
plt.grid(b='on')
plt.ylim(ymin=0)
plt.xlim(xmin=0)
plt.title('Earnings versus time')
plt.ylabel('Money earned')
plt.xlabel('Time spent')
plt.show()

gp.qplot(x, y)
help(plt.grid)
