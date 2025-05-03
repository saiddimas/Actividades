#import numpy as np
import matplotlib.pyplot as plt
categoria = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]
plt.xlabel("Categoria")
plt.ylabel("Valores")
plt.bar(categoria, valores, color = "blue")
plt.show()