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
