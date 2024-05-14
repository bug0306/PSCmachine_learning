import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

def plot_scatter(x, y, ax, title=None):
    ax.scatter(x, y, s=0.5, c='darkblue')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    if title:
        ax.set_title(title, fontsize=10)

fig, axes = plt.subplots(3, 7, figsize=(9, 5))

num_points = 500
noise_levels = [0.02, 0.1, 0.25,1, 0.25, 0.1, 0.02]  
for i, corr in enumerate(np.linspace(1, -1, 7)):
    x = np.random.rand(num_points) * 2 - 1
    y = x * corr + np.random.randn(num_points) * noise_levels[i]
    plot_scatter(x, y, axes[0, i], title=f"{corr:.1f}")

num_points = 200
slopes = [0.8, 0.6, 0.2, 0, -0.2, -0.6,-0.8]  
for i in range(7):
    if i == 0 or i == 1 or i==2:
        x = np.random.rand(num_points) * 2 - 1
        y = slopes[i] * x + np.random.randn(num_points) * 0.02
        plot_scatter(x, y, axes[1, i],title="1")
    elif i == 4 or i == 5 or i==6:
        x = np.random.rand(num_points) * 2 - 1
        y = slopes[i] * x + np.random.randn(num_points) * 0.02
        plot_scatter(x, y, axes[1, i],title="-1")
    else:
        x = np.random.rand(num_points) * 2 - 1
        y = slopes[i] * x + np.random.randn(num_points) * 0.02
        plot_scatter(x, y, axes[1, i])

num_points = 500
x = np.random.rand(num_points) * 2 - 1
y1 = np.sin(3 * x) + np.random.randn(num_points) * 0.03
y2 = x**2 + np.random.randn(num_points) * 0.03
y3 = np.abs(x) + np.random.randn(num_points) * 0.03
y4 = np.sin(4 * x) * np.cos(x) + np.random.randn(num_points) * 0.03
y5 = np.sin(4 * x) * np.cos(x) + np.random.randn(num_points) * 0.03
y6 = (x**2 + y1**2 - 0.6) * np.exp(-x**2 - y1**2)
y7 = np.sqrt(x**2 + y1**2) + np.random.randn(num_points) * 0.02

plot_scatter(x, y1, axes[2, 0],title="0")
plot_scatter(x, y2, axes[2, 1],title="0")
plot_scatter(x, y3, axes[2, 2],title="0")
plot_scatter(x, y4, axes[2, 3],title="0")
plot_scatter(y1, y5, axes[2, 4],title="0")
plot_scatter(y1, y6, axes[2, 5],title="0")
plot_scatter(y1, y7, axes[2, 6],title="0")

plt.subplots_adjust(wspace=0.1, hspace=0.3)

plt.show()