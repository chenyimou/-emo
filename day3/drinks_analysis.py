import pandas as pd

# 读取数据
df = pd.read_csv('../shujv/drinks.csv')

# 1. 哪个大陆平均消耗的啤酒更多
beer_by_continent = df.groupby('continent')['beer_servings'].mean().sort_values(ascending=False)
print('1. 大陆平均啤酒消耗排名:')
print(beer_by_continent)
print(f'\n最高平均啤酒消耗的大陆是: {beer_by_continent.idxmax()} ({beer_by_continent.max():.1f})')

# 2. 每个大陆红酒消耗的描述性统计
print('\n2. 每个大陆红酒消耗的描述性统计:')
print(df.groupby('continent')['wine_servings'].describe())

# 3. 每个大陆每种酒类别的消耗平均值
print('\n3. 每个大陆每种酒类别的消耗平均值:')
print(df.groupby('continent').mean(numeric_only=True))

# 4. 每个大陆每种酒类别的消耗中位数
print('\n4. 每个大陆每种酒类别的消耗中位数:')
print(df.groupby('continent').median(numeric_only=True))

# 将结果保存到文件
with open('drinks_analysis_results.txt', 'w') as f:
    pd.set_option('display.float_format', '{:.1f}'.format)

    f.write('1. 大陆平均啤酒消耗排名:\n')
    beer_by_continent.to_string(f)
    f.write(f'\n\n最高平均啤酒消耗的大陆是: {beer_by_continent.idxmax()} ({beer_by_continent.max():.1f})')

    f.write('\n\n2. 每个大陆红酒消耗的描述性统计:\n')
    df.groupby('continent')['wine_servings'].describe().to_string(f)

    f.write('\n\n3. 每个大陆每种酒类别的消耗平均值:\n')
    df.groupby('continent').mean(numeric_only=True).to_string(float_format='%.1f')

    f.write('\n\n4. 每个大陆每种酒类别的消耗中位数:\n')
    df.groupby('continent').median(numeric_only=True).to_string(float_format='%.1f')

print("分析结果已保存到 drinks_analysis_results.txt")