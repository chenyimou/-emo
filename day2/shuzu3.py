import numpy as np

# 创建数组
A = np.arange(1, 7).reshape(3, 2)  # 3x2数组
B = np.array([10, 20])             # 一维数组

print("数组A:\n", A)
print("数组B:\n", B)

# 1. 逐元素相加（广播机制）
add_result = A + B
print("\n1. A + B:\n", add_result)

# 2. 逐元素相乘（广播机制）
mul_result = A * B
print("\n2. A * B:\n", mul_result)

# 3. 计算A的每一行与B的点积
dot_result = np.dot(A, B)
print("\n3. A每行与B的点积:", dot_result)