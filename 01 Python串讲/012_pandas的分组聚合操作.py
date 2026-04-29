import pandas as pd
import numpy as np

# 读取文件
# csv:具有固定分隔符的结构化数据，都是CSV格式，不用关注后缀名是不是csv
df = pd.read_csv('./data/gapminder.txt', sep='\t')
# print(df)

# 数据分析（分组聚合操作）
# 需求1：求每个年份的平均寿命
# print(df.groupby('year').lifeExp.mean())  

# print(df.groupby('year')['lifeExp'].mean())  

# print(df['year'])
# print(df[['lifeExp', 'year']])

# print(df.groupby('year')[['lifeExp']].mean()) 

# print(df.groupby('year').agg({"lifeExp": 'mean'})) 

# print(df.groupby('year').agg({"lifeExp": np.mean}))

# 需求2：求每个年份，每个大洲的的平均寿命和最高GDP
# print(df.groupby(['year', 'continent']).agg({"lifeExp": np.mean, "gdpPercap": np.max}))

# print('-----------------------------')

# print(df.groupby(['year', 'continent']).agg({"lifeExp": 'mean', "gdpPercap": 'max'}))

# 练习1：求每年各个国家的平均年龄
# print(df.groupby(['year', 'country']).agg({"lifeExp": np.mean}))

# 练习2：求每年各个国家的平均年龄和最高GDP
# print(df.groupby(['year', 'country']).agg({"lifeExp": np.mean, "gdpPercap": np.max}))

# 练习3：单独计算1952年的平均寿命
print(df[df['year'] == 1952].groupby('year').agg({"lifeExp": np.mean}))
