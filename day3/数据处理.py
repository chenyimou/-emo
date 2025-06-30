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

# 保存处理后的数据
merged_df.to_csv('merged_city_data_2015-2017_processed.csv', index=False, encoding='utf_8_sig')
yearly_gdp.to_csv('yearly_gdp_totals.csv', index=False, encoding='utf_8_sig')

print("数据处理完成，已保存以下文件：")
print("1. 合并且处理缺失值后的数据: merged_city_data_2015-2017_processed.csv")
print("2. 年度GDP总和: yearly_gdp_totals.csv")
print("\n各年度国内生产总值总和:")
print(yearly_gdp)