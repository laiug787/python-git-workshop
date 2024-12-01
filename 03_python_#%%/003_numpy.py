#%%
import numpy as np

# Create a 2D array (matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Perform matrix multiplication
result = np.dot(matrix, matrix)

print("Matrix:")
print(matrix)
print("\nMatrix multiplied by itself:")
print(result)

# Calculate the determinant of the matrix
determinant = np.linalg.det(matrix)
print("\nDeterminant of the matrix:")
print(determinant)

# Calculate the inverse of the matrix
try:
    inverse = np.linalg.inv(matrix)
    print("\nInverse of the matrix:")
    print(inverse)
except np.linalg.LinAlgError:
    print("\nMatrix is singular and cannot be inverted.")

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nEigenvalues of the matrix:")
print(eigenvalues)
print("\nEigenvectors of the matrix:")
print(eigenvectors)

"""
このスクリプトは、NumPyライブラリを使用して2次元配列（行列）に対していくつかの線形代数操作を実行します。

具体的には以下の操作を行います:
1. 2次元配列（行列）の作成
2. 行列の積の計算
3. 行列式の計算
4. 行列の逆行列の計算
5. 行列の固有値と固有ベクトルの計算

使用される関数とその説明:
- np.array: 配列を作成します。
- np.dot: 行列の積を計算します。
- np.linalg.det: 行列式を計算します。
- np.linalg.inv: 逆行列を計算します。行列が正則でない場合は例外をスローします。
- np.linalg.eig: 行列の固有値と固有ベクトルを計算します。

例外処理:
- np.linalg.LinAlgError: 行列が正則でない場合（逆行列が存在しない場合）にスローされます。

出力:
- 元の行列
- 行列の積
- 行列式
- 逆行列（存在する場合）
- 固有値
- 固有ベクトル
"""