import matplotlib.pyplot as plt
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]
colores = ['red', 'blue', 'green', 'purple']
plt.bar(categorias, valores, color = colores)
plt.xlabel("Categorias")
plt.ylabel("Valores")
plt.show()