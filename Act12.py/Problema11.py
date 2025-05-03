import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
tamaños = [20, 50, 80, 100, 150]
plt.xlabel("Eje X")
plt.ylabel("Eje y")
plt.scatter(x, y, s = tamaños)
plt.show()