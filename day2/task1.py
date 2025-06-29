# 练习1: 判断回文数
def is_palindrome(n):
    """判断一个数字是否为回文数"""
    return str(n) == str(n)[::-1]


# 练习2: 计算任意数量参数的平均值
def average(*args):
    """计算任意数量参数的平均值"""
    return sum(args) / len(args) if args else 0


# 练习3: 返回最长字符串
def longest_string(*strings):
    """返回传入的最长字符串（如有多个相同长度，返回第一个）"""
    return max(strings, key=len, default=None)


# 练习4: 矩形计算模块
class Rectangle:
    """模拟矩形计算模块"""

    @staticmethod
    def area(length, width):
        """计算矩形面积"""
        return length * width

    @staticmethod
    def perimeter(length, width):
        """计算矩形周长"""
        return 2 * (length + width)


# ============= 测试所有函数 =============
if __name__ == "__main__":
    # 测试练习1
    print("回文数测试:")
    print(f"121 是回文数吗? {is_palindrome(121)}")  # True
    print(f"123 是回文数吗? {is_palindrome(123)}")  # False
    print(f"12321 是回文数吗? {is_palindrome(12321)}")  # True
    print()

    # 测试练习2
    print("平均值测试:")
    print(f"(1, 2, 3) 的平均值: {average(1, 2, 3):.1f}")  # 2.0
    print(f"(10, 20, 30, 40) 的平均值: {average(10, 20, 30, 40):.1f}")  # 25.0
    print(f"(5) 的平均值: {average(5):.1f}")  # 5.0
    print()

    # 测试练习3
    print("最长字符串测试:")
    words = ("apple", "banana", "cherry")
    print(f"在 {words} 中最长的字符串: {longest_string(*words)}")  # banana
    animals = ("cat", "dog", "elephant", "bird")
    print(f"在 {animals} 中最长的字符串: {longest_string(*animals)}")  # elephant
    print()

    # 测试练习4 - 模拟模块导入
    print("矩形计算测试:")
    # 模拟导入模块
    rect = Rectangle()

    length, width = 5, 3
    print(f"矩形 ({length}x{width}) 面积: {rect.area(length, width)}")  # 15
    print(f"矩形 ({length}x{width}) 周长: {rect.perimeter(length, width)}")  # 16

    length, width = 7, 4
    print(f"矩形 ({length}x{width}) 面积: {Rectangle.area(length, width)}")  # 28
    print(f"矩形 ({length}x{width}) 周长: {Rectangle.perimeter(length, width)}")  # 22