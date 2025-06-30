import pandas as pd

# 读取三个年份的数据
df_2015 = pd.read_csv('../shujv/2015年国内主要城市年度数据.csv')
df_2016 = pd.read_csv('../shujv/2016年国内主要城市年度数据.csv')
df_2017 = pd.read_csv('../shujv/2017年国内主要城市年度数据.csv')

# 1. 纵向合并数据
merged_df = pd.concat([df_2015, df_2016, df_2017], ignore_index=True)

# 2. 处理缺失值，填充为0
merged_df = merged_df.fillna(0)

# 3. 按年份聚合计算国内生产总值
yearly_gdp = merged_df.groupby('年份')['国内生产总值'].sum().reset_index()
yearly_gdp.columns = ['年份', '国内生产总值总和']


# 5. 计算年均GDP增长率
def calculate_growth_rate(df):
    city_growth = []
    for city in df['地区'].unique():
        city_data = df[df['地区'] == city].sort_values('年份')
        if len(city_data) == 3:  # 确保有3年数据
            gdp_2015 = city_data[city_data['年份'] == 2015]['国内生产总值'].values[0]
            gdp_2017 = city_data[city_data['年份'] == 2017]['国内生产总值'].values[0]
            if gdp_2015 > 0:  # 避免除零错误
                cagr = ((gdp_2017 / gdp_2015) ** (1/2) - 1) * 100
                city_growth.append({'城市': city, '年均增长率(%)': cagr})

    growth_df = pd.DataFrame(city_growth)
    top5 = growth_df.nlargest(5, '年均增长率(%)')
    bottom5 = growth_df.nsmallest(5, '年均增长率(%)')
    return growth_df, top5, bottom5

# 6. 医院数归一化处理
def normalize_hospital_data(df):
    df['医院数归一化'] = (df['医院、卫生院数'] - df['医院、卫生院数'].min()) / \
                     (df['医院、卫生院数'].max() - df['医院、卫生院数'].min())
    return df.groupby(['地区', '年份'])['医院数归一化'].mean().unstack()

# 7. 提取四大城市数据
def extract_major_cities(df):
    cities = ['北京', '上海', '广州', '深圳']
    return df[df['地区'].isin(cities)][['地区', '年份', '国内生产总值', '社会商品零售总额']]

# 执行分析
growth_df, top5, bottom5 = calculate_growth_rate(merged_df)
normalized_hospitals = normalize_hospital_data(merged_df)
major_cities_data = extract_major_cities(merged_df)

# 保存结果
growth_df.to_csv('city_growth_rates.csv', index=False)
top5.to_csv('top5_growth_cities.csv', index=False)
bottom5.to_csv('bottom5_growth_cities.csv', index=False)
normalized_hospitals.to_csv('normalized_hospitals.csv')
major_cities_data.to_csv('major_cities_gdp_retail.csv', index=False)

print("分析完成，已保存以下文件：")
print("1. 各城市GDP年均增长率: city_growth_rates.csv")
print("2. 增长率最高5个城市: top5_growth_cities.csv")
print("3. 增长率最低5个城市: bottom5_growth_cities.csv")
print("4. 医院数归一化结果: normalized_hospitals.csv")
print("5. 四大城市GDP和零售数据: major_cities_gdp_retail.csv")