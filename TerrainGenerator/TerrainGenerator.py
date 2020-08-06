import numpy as np
import matplotlib.pyplot as plt
import math
import random

import PerlinNoise as PN 

size = 5
resolution = 200
waterlevel = -0.037

lin = np.linspace(0, size, resolution,endpoint=False)
x,y = np.meshgrid(lin,lin)
grid = PN.octavePerlin(x,y, 5, 0.7, seed=189)

for x in range(resolution):
    for y in range(resolution):
        grid[x][y] = grid[x][y] if grid[x][y] > waterlevel else -1
print(grid)

plt.imshow(grid,origin='upper')
plt.show()
