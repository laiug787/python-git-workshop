# %%
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# %%
# 簡単なxy座標のグラフの作成
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6), dpi=300)
plt.plot(x, y, label="sin(x)")

# グラフの書式設定
plt.title("Simple XY Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.grid(True)

# グラフの表示
plt.show()


# %%
# 簡単なxy座標のグラフの作成 (using ax)
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, label="sin(x)")

# グラフの書式設定
ax.set_title("Simple XY Graph")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.legend()
ax.grid(True)

# グラフの表示
plt.show()


# %%
# データの準備
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# プロットの作成
fig = plt.figure(figsize=(10, 6), dpi=300)
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(x, y, z, cmap="viridis")

# グラフの表示
plt.show()
