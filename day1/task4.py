# 问题1
s1 = "Python is a powerful programming language"

# (1) 提取单词"language"
print("1(1) 提取的单词:", s1.split()[-1])

# (2) 用一句print重复输出3次
print("1(2) 重复输出:", s1.split()[-1] * 3)  # 使用字符串乘法

# (3) 输出所有以p或P开头的单词
p_words = [word for word in s1.split() if word.lower().startswith('p')]
print("1(3) 以p/P开头的单词:", p_words)

# 问题2
s3 = "Hello, World! This is a test string. "

# (1) 去除前后空格
s3_stripped = s3.strip()
print("\n2(1) 去除前后空格:", s3_stripped)

# (2) 转换为大写
s3_upper = s3_stripped.upper()
print("2(2) 转换为大写:", s3_upper)

# (3) 查找"test"下标
test_index = s3_stripped.find("test")
print("2(3) 'test'起始下标:", test_index)

# (4) 替换"test"为"practice"
s3_replaced = s3_stripped.replace("test", "practice")
print("2(4) 替换后字符串:", s3_replaced)

# (5) 分割并连接
s3_split = s3_stripped.split()
s3_joined = "n-n".join(s3_split)  # 使用"n-n"作为连接符
print("2(5) 分割并连接:", s3_joined)