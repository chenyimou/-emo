import numpy as np

# 1. 创建3×4数组（元素为1-12）
arr = np.arange(1, 13).reshape(3, 4)
print("原始数组:\n", arr)

# 2. 打印数组属性
print("\n1. 数组属性:")
print(f"形状: {arr.shape}")     # 输出: (3, 4)
print(f"维度: {arr.ndim}")      # 输出: 2
print(f"数据类型: {arr.dtype}") # 输出: int32/int64

# 3. 元素乘以2
arr_doubled = arr * 2
print("\n2. 元素乘以2:\n", arr_doubled)

# 4. 重塑为4×3
arr_reshaped = arr.reshape(4, 3)
print("\n3. 重塑为4×3:\n", arr_reshaped)