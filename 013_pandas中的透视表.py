import numpy as np
import pandas as pd

df = pd.read_csv('./data/gapminder.txt', sep='\t')
# print(df)

# 需求1：求每个年份的平均寿命--方式：原生聚合函数
print(df.groupby('year').lifeExp.mean())  
print('-----------------------------')
# 方式二：透视表
print(df.pivot_table(index='year', values='lifeExp', aggfunc=np.mean))