import pandas as pd
import numpy as np

# 1. 创建包含数据的CSV文件
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eva'],
    'Score': [92, 85, np.nan, 78, 95],
    'Grade': ['A', 'B', 'C', 'C', 'A']
}

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)
print("students.csv 文件创建成功！\n")

# 2. 读取CSV文件并打印前3行
students_df = pd.read_csv('students.csv')
print("前3行数据：")
print(students_df.head(3))
print("\n原始数据统计：")
print(students_df.info())

# 3. 填充缺失值
# 计算Score列的平均分（排除NaN值）
score_mean = students_df['Score'].mean().round(1)

# 分别填充不同列的缺失值
students_df['Score'] = students_df['Score'].fillna(score_mean)
students_df['Name'] = students_df['Name'].fillna('Unknown')

# 4. 保存处理后的数据
students_df.to_csv('students_cleaned.csv', index=False)
print("\n处理后的数据：")
print(students_df)
print(f"\nScore列缺失值填充为: {score_mean}")
print("清洗后的数据已保存为 students_cleaned.csv")