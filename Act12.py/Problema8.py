import matplotlib.pyplot as plt
etiquetas = ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas']
tamaños = [30, 25, 20, 25]
colores = ["red" , "orange", "yellow" , "purple"]
plt.pie(tamaños, labels = etiquetas, colors = colores)
plt.show()