from matplotlib import pyplot as plt
import numpy as np

plt.style.use("ggplot")

x = np.linspace(1, 5, 500)
y = np.log10(x)

fig, axe = plt.subplots(figsize=(7, 4))

axe.plot(x, y, lw=1.2)
axe.plot([0, 2.5], [0.4, 0.4], linestyle="--", color="gray", lw=0.8)
axe.plot([2.5, 2.5], [0, 0.4], linestyle="--", color="gray", lw=0.8)
axe.plot(2.5, 0.4, marker="o", color="gray")
axe.set_xticks(np.arange(0, 5.5, 0.5))

plt.show()
