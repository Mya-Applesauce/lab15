"""
Lab 15
Ari Papke
Plotting a shape
05/14/26
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10, 10, 420)
y = (4 * (x ** 2)) + (1 / (x ** 2)) - (4 * (x ** 2))

fig, ax = plt.subplots()
ax.plot(x, y)
plt.ylabel('some numbers')
plt.show()
