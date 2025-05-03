import matplotlib.pyplot as plt
categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]
etiquetas = ["Grafo 1", "Grafo 2", "Grafo 3", "Grafo 4"]
plt.bar(categorias, valores)
for i, v in enumerate(valores):
    plt.text(i, v + 0.5, str(v), ha = "center", va ="bottom")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()