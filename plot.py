#Practicing in plotting with matplotlib
#Import pyplot from matpotlib package
import numpy as np
import ggplot as gp
from matplotlib import pyplot as plt

#Generating arrays
x = np.arange(0, 1, 0.05)
y = np.power(x, 2)

#Plotting arrays with scatter
plt.scatter(x, y)
plt.grid(b='on')
plt.ylim(ymin=0, ymax=1)
plt.xlim(xmin=0, xmax=1)
plt.title('Earnings versus time')
plt.ylabel("Money earned, '000 000 $")
plt.xlabel('Time spent, years')
plt.show()

gp.qplot(x, y) + \
    gp.labs(x='Time spent, years',
            y="Money earned, '000 000 $",
            title="Earnings versus time") + \
    gp.theme_gray() + \
    gp.xlim(0, 1) + \
    gp.ylim(0, 1)

help(gp.ggtitle)
