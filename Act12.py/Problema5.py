import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.scatter(x, y, color= "red")
plt.show()