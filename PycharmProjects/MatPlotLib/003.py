import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
s = np.sin(x)
c = np.cos(x)

plt.figure("Gráficos Cosenoidais", figsize=(8, 4))
plt.suptitle("Gráficos")
plt.subplots_adjust(
    left = 0.12,
    right = 0.94,
    top = 0.9,
    bottom = 0.14,
    wspace = 0.43,
    hspace = 0.4
)

ax1 = plt.subplot(1, 2, 1)
plt.plot(x, s)
ax1.set_title("Gráfico do seno")
ax1.set_xlabel("Eixo de Tempo")
ax1.set_ylabel("Eixo de Amplitude")
ax1.grid()

ax2 = plt.subplot(1, 2, 2)
plt.plot(x, c)
ax2.set_title("Gráfico do Cosseno")
ax2.set_xlabel("Eixo de Tempo")
ax2.set_ylabel("Eixo de Amplitude")

plt.show()
