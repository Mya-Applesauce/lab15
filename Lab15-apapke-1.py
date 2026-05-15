"""
Lab 15
Ari Papke
Plotting a shape
05/14/26
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import math

x = np.linspace(-10, 10, 420)
y = (4 * (x ** 2))

fig, ax = plt.subplots()
polygon = Polygon([(10, 10), (60, 20), (50, 60)], edgecolor='orange', facecolor='yellow', linewidth=6)
ax.add_patch(polygon)
ax.set_xlim(0, 69)
ax.set_ylim(0, 69)
ax.set_aspect('equal')
ax.set_title("traingle")
plt.xlabel("its the triangel")
plt.ylabel("watch out")
plt.savefig("traingel.png")
