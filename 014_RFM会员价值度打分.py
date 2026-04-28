import numpy as np
import pandas as pd

df = pd.read_excel('./data/sales_test.xlsx', index_col = 'USERID')
print('1-----------------------------')
print(df)

# print(df.index)
# print(df.columns)
# print(df.shape)

# 删除全部为空值的行
sale_data = df.dropna(how='all')
# 数据分析
# 获取每个用户的购买时间、购买频率、购买金额
index_data = sale_data.groupby(sale_data.index)
print('2-----------------------------')
print(index_data)

F_data = sale_data.groupby(sale_data.index)['ORDERID'].count()
M_data = sale_data.groupby(sale_data.index)['AMOUNTINFO'].sum()
R_data = sale_data.groupby(sale_data.index)['ORDERDATE'].max()

print('3-----------------------------')
print(F_data)

print(M_data)
print('4-----------------------------')

print(M_data)
print('5-----------------------------')
print(R_data)
