import matplotlib.pyplot as plt
x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]
plt.plot(x, y1, label = "Datos 1", color = "blue")
plt.plot(x, y2, label = "Datos 2", color = "green")
plt.legend()
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.show()
