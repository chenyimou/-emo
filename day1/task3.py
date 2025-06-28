# 1. 使用列表推导式存储1-100的整数，然后输出其中所有偶数
print("1. 1-100之间的所有偶数:")
even_numbers = [num for num in range(1, 101) if num % 2 == 0]
print(even_numbers)

# 2. 给定一个列表，删除其中的重复元素并保持顺序不变
print("\n2. 删除重复元素保持顺序:")
original_list = [3, 5, 2, 5, 7, 3, 8, 2, 9, 5]
unique_list = []
[unique_list.append(item) for item in original_list if item not in unique_list]
print(f"原始列表: {original_list}")
print(f"去重后列表: {unique_list}")

# 3. 合并两个列表为字典
print("\n3. 合并列表为字典:")
keys = ["a", "b", "c"]
values = [1, 2, 3]
merged_dict = dict(zip(keys, values))
print(f"键列表: {keys}")
print(f"值列表: {values}")
print(f"合并字典: {merged_dict}")

# 4. 定义学生信息元组并解包
print("\n4. 学生信息元组解包:")
student = ("张三", 18, 92)
name, age, score = student
print(f"完整元组: {student}")
print(f"解包结果: 姓名={name}, 年龄={age}, 成绩={score}")