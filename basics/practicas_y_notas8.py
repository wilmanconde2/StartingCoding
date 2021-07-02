# LIBRERIAS
import math
import matplotlib.pyplot as plt

x = []
y = []

for i in range(0, 360, 1):
    angulo = math.radians(i)
    print(x)
    print(y)

    x.append(angulo)
    y.append(math.sin(angulo))

plt.plot(x, y)
plt.ylabel('funcion seno')
plt.show()
