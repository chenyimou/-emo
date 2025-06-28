# 练习题1: 输出1到100之间的所有素数
def is_prime(n):
    """检查一个数是否为素数"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# 练习题2: 计算斐波那契数列的前20项
def fibonacci(n):
    fib = [0, 1]  # 初始化前两项
    for i in range(2, n):
        next_term = fib[i - 1] + fib[i - 2]
        fib.append(next_term)
    return fib


# 练习题3: 使用while循环计算1-10000之间满足条件的数的和
def calculate_special_sum():
    total = 0
    num = 1
    while num <= 10000:
        if num % 3 == 0 or (num % 5 == 0 and num % 15 != 0):
            total += num
        num += 1
    return total


# 主程序
if __name__ == "__main__":
    # 题目1
    print("1. 1到100之间的素数:")
    primes = [num for num in range(1, 101) if is_prime(num)]
    for i in range(0, len(primes), 10):  # 每行输出10个素数
        print(' '.join(map(str, primes[i:i + 10])))

    # 题目2
    print("\n2. 斐波那契数列前20项:")
    fib_sequence = fibonacci(20)
    print(fib_sequence)

    # 题目3
    print("\n3. 1-10000之间满足条件的数的和:")
    special_sum = calculate_special_sum()
    print(special_sum)