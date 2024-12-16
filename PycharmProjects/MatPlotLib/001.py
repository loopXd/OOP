import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 100)
y = np.cos(t)
x = np.sin(t)

plt.figure("Seno", figsize=(5, 4))
plt.plot(t, y)
plt.title("Gráfico do Cosseno")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")

plt.figure("Cosseno")
plt.plot(t, x)
plt.title("Gráfico do Seno 2")
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")

plt.show()