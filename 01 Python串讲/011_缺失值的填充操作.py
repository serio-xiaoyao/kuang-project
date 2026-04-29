import pandas as pd


df=pd.read_csv('./data/students.csv')
print(df)
new_df1 = df.fillna(0)
print(new_df1)

new_df2=df.fillna(df['age'].mean())
print(new_df2)

new_df3=df.fillna({'age':df['age'].mean()})
print(new_df3)

# 填充当前缺失值的后一个数据
new_df4 = df.bfill()
print(new_df4)

# 填充当前缺失值的前一个数据
new_df5 = df.ffill()
print(new_df5)
