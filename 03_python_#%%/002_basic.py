# %% [markdown]
# 1. データ型と変数

# %%
# 変数の基本
name = "田中"  # 文字列
age = 25  # 整数
height = 1.75  # 浮動小数点
is_student = True  # ブール値(真偽値)
is_teacher = False

# 型の確認
print(type(name))  # <class 'str'>

# %% [markdown]
# 2. 算術演算子

# %%
a = 5
b = 3

# 加算
print(a + b)  # 出力: 8
# 減算
print(a - b)  # 出力: 2
# 乗算
print(a * b)  # 出力: 15
# 除算
print(a / b)  # 出力: 1.6666666666666667
# 整数除算
print(a // b)  # 出力: 1
# 剰余
print(a % b)  # 出力: 2
# 累乗
print(a**b)  # 出力: 125

# %% [markdown]
# 3. 比較演算子

# %%
x = 5
y = 10

# 比較演算子の例
print("x < y:", x < y)  # x は y より小さい  : True
print("x <= y:", x <= y)  # x は y 以下       : True
print("x > y:", x > y)  # x は y より大きい  : False
print("x >= y:", x >= y)  # x は y 以上       : False
print("x == y:", x == y)  # x と y は等しい    : False
print("x != y:", x != y)  # x と y は等しくない : True

# %% [markdown]
# 4. 論理演算子

# %%
# or の例
print(True or False)  # 出力: True
print(False or False)  # 出力: False

# and の例
print(True and False)  # 出力: False
print(True and True)  # 出力: True

# and と or の組み合わせ
print(True or (False and True))  # 出力: True
print((True or False) and False)  # 出力: False

# %% [markdown]
# 5. 制御構造

# %%
# 条件式
a = 5
b = 3

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

# for文(繰り返し処理)
for i in range(5):
    print(i)

# while文 条件が真の間、繰り返し処理を行う
i = 0
while i < 5:
    print(i)
    i += 1

# %% [markdown]
# 6. 関数の定義と使用


# %%
# 関数の定義
def f(x: int) -> int:
    a, b, c = 1, 2, 3
    answer = a * x**2 + b * x + c
    return answer


# 関数の呼び出し
f_answer = f(x=2)
print(f_answer)  # 11


# %%
# 関数の定義
def g(x: int, y: int) -> int:
    answer = x**2 + y**2
    return answer


# 関数の呼び出し
g_answer = g(x=3, y=4)
print(g_answer)  # 25


# %%
# 戻り値を返さない関数
def greet(name):
    print(f"Hello, {name}!")


# 関数を呼び出す
greet("Alice")  # 出力: Hello, Alice!


# %%
# 複数の戻り値を持つ関数
# 足し算、引き算、掛け算、割り算の結果を返す
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else None  # 0で割らないようにする
    return addition, subtraction, multiplication, division


# 関数を呼び出し
add, sub, mul, div = calculate(10, 5)

# 結果を表示
print(f"足し算: {add}, 引き算: {sub}, 掛け算: {mul}, 割り算: {div}")

# %% [markdown]
# 7. クラス定義


# %%
# クラスの定義
class Car:
    # コンストラクタ: オブジェクトを生成するときの初期化する特別なメソッド
    def __init__(self, color, speed=0):
        self.color = color  # 属性: 色
        self.speed = speed  # 属性: 速度

    # メソッド: 加速する
    def accelerate(self, amount):
        self.speed += amount
        print(f"The car accelerates. New speed: {self.speed} km/h")

    # メソッド: ブレーキをかける
    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"The car slows down. New speed: {self.speed} km/h")


# オブジェクトの生成
my_car = Car("red")  # 赤い車を作成
print(my_car.color)  # red

# メソッドの呼び出し
my_car.accelerate(30)  # The car accelerates. New speed: 30 km/h
my_car.brake(10)  # The car slows down. New speed: 20 km/h
