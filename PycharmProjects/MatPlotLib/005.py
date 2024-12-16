from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 35)
y = np.cos(3*x)
y1 = np.sin(3*x)

plt.figure("Grafico", figsize=(8, 4))
plt.plot(x, y, color="g", lw=2.0, marker="o", linestyle="solid")
plt.plot(x, y1, color="r", lw=2.0, marker="^", linestyle="dashed")
plt.grid()
plt.title("Gráfico do Cosseno e Seno")
plt.xlabel("Eixo de Tempo")
plt.ylabel("Eixo da Amplitude")
plt.show()
