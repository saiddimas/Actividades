import matplotlib.pyplot as plt
categoria = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]
plt.xlabel("Valores")
plt.ylabel("Categorias")
plt.barh(categoria, valores, color = "green")
plt.show()