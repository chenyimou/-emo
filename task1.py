# 练习1: 数据类型判断
print("练习1结果:")
x, y, z = 10, "10", True
print(f"x: {x} → {type(x)}")
print(f"y: '{y}' → {type(y)}")
print(f"z: {z} → {type(z)}")

# 练习2: 圆面积计算（改进版）
print("\n练习2:")
try:
    # 更清晰的输入提示，不需要在提示中包含示例值
    radius = float(input("请输入圆的半径: "))
    pi = 3.14
    area = pi * radius**2
    print(f"半径为 {radius} 的圆面积是: {area:.2f}")
except ValueError:
    print("错误：请输入有效的数字！")
except KeyboardInterrupt:
    print("\n操作已取消")
# 类型转换实验
print("\n练习3:")
str_value = "3.14"
float_value = float(str_value)  # 字符串 → 浮点数
int_value = int(float_value)    # 浮点数 → 整数

# 输出结果及差异分析
print(f"原始字符串: '{str_value}' (类型: {type(str_value)})")
print(f"转浮点数后: {float_value} (类型: {type(float_value)})")
print(f"再转整数后: {int_value} (类型: {type(int_value)})")
print("\n差异分析: 浮点数转换会保留小数部分 (3.14 → 3.14)，但转换为整数时会直接截断小数部分 (3.14 → 3)")

