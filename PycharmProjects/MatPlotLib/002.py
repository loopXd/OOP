import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 100)
y = np.cos(t)
x = np.sin(t)

plt.figure("Gráfico", figsize=(6, 4))
plt.plot(t, y)
plt.plot(t, x)
plt.title("Gráfico do Seno e Cosseno")
plt.xlabel("Eixo do Tempo")
plt.ylabel("Eixo da Amplitude")
plt.grid()
plt.show()
