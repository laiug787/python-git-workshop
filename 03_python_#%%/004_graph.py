# %%
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# %%
# 簡単なxy座標のグラフの作成
x = np.linspace(0, 10, 100)
y = np.sin(x)

# -- フォント --
plt.rcParams["font.family"] = "Arial"  # ["Arial", "Times New Roman", "Helvetica"]
# -- 目盛り --
plt.rcParams["xtick.labelsize"] = 20  # x軸の目盛りのフォントサイズ
plt.rcParams["ytick.labelsize"] = 20  # y軸の目盛りのフォントサイズ
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.major.width"] = 1.0
plt.rcParams["ytick.major.width"] = 1.0
plt.rcParams["xtick.minor.width"] = 1.0
plt.rcParams["ytick.minor.width"] = 1.0
plt.rcParams["xtick.top"] = True
plt.rcParams["xtick.bottom"] = True
plt.rcParams["ytick.left"] = True
plt.rcParams["ytick.right"] = True
# -- 軸ラベル --
plt.rcParams["font.size"] = 24
plt.rcParams["axes.linewidth"] = 1.0  # 軸の太さ
# -- 凡例 --
plt.rcParams["legend.frameon"] = True
plt.rcParams["legend.fontsize"] = 18  # 凡例のラベルのフォントサイズ
plt.rcParams["legend.title_fontsize"] = 18  # 凡例のタイトルのフォントサイズ
plt.rcParams["legend.fancybox"] = False  # 丸角
plt.rcParams["legend.edgecolor"] = "black"
# -- サイズ --
plt.rcParams["lines.markersize"] = 8  # マーカーサイズ
plt.rcParams["figure.figsize"] = [16, 6]  # グラフのサイズを設定 (幅, 高さ)

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
