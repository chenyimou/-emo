class Car:
    def __init__(self, brand, speed=0):
        """初始化汽车实例
        :param brand: 品牌
        :param speed: 初始速度，默认为0
        """
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        """加速方法，速度增加 m 次，每次增加 10
        :param m: 加速次数
        """
        self.speed += 10 * m
        print(f"{self.brand} 加速 {m} 次，当前速度: {self.speed}")

    def brake(self, n):
        """刹车方法，速度减少 n 次，每次减少 10，不低于 0
        :param n: 刹车次数
        """
        # 计算刹车后的速度，确保不低于0
        self.speed = max(0, self.speed - 10 * n)
        print(f"{self.brand} 刹车 {n} 次，当前速度: {self.speed}")


# 创建Car实例并测试
if __name__ == "__main__":
    # 创建普通汽车实例
    my_car = Car("Toyota", 30)
    print(f"初始速度: {my_car.speed}")

    # 测试加速和刹车
    my_car.accelerate(2)  # 加速2次 -> 30 + 20 = 50
    my_car.brake(1)  # 刹车1次 -> 50 - 10 = 40
    my_car.brake(5)  # 刹车5次 -> 40 - 50 = 0 (不低于0)


    # 创建电动汽车类
    class ElectricCar(Car):
        def __init__(self, brand, speed=0, battery=0):
            """初始化电动汽车
            :param battery: 初始电量，默认为0
            """
            super().__init__(brand, speed)
            self.battery = battery

        def charge(self):
            """充电方法，电量增加20，不超过100"""
            self.battery = min(100, self.battery + 20)
            print(f"{self.brand} 充电后电量: {self.battery}%")


    # 测试电动汽车
    print("\n电动汽车测试:")
    tesla = ElectricCar("Tesla", battery=50)
    print(f"初始电量: {tesla.battery}%")

    # 充电测试
    tesla.charge()  # 50 + 20 = 70
    tesla.charge()  # 70 + 20 = 90
    tesla.charge()  # 90 + 20 = 100
    tesla.charge()  # 仍然是100 (不超过100)

    # 测试电动汽车的加速和刹车
    tesla.accelerate(3)  # 0 + 30 = 30
    tesla.brake(2)  # 30 - 20 = 10