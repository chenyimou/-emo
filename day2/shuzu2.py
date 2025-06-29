import numpy as np

# 创建给定数组
array = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]])

# 1. 提取第2行所有元素
row_2 = array[1, :]  # 行索引1（第2行），所有列
print("1. 第2行所有元素:", row_2)

# 2. 提取第3列所有元素
col_3 = array[:, 2]  # 所有行，列索引2（第3列）
print("\n2. 第3列所有元素:", col_3)

# 3. 提取子数组（第1、2行和第2、3列）
sub_array = array[0:2, 1:3]  # 行切片0:2（第1-2行），列切片1:3（第2-3列）
print("\n3. 子数组:\n", sub_array)

# 4. 将大于10的元素替换为0
modified_array = array.copy()  # 创建副本避免修改原数组
modified_array[modified_array > 10] = 0  # 布尔索引筛选
print("\n4. 修改后的数组:\n", modified_array)