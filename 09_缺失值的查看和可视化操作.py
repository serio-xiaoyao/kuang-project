# 1.导包
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

# 2.读取数据
train = pd.read_csv('./data/titanic_train.csv')
test = pd.read_csv('./data/titanic_test.csv')
# 3.了解数据
print('train.shape:' , train.shape)  # (892, 12)
print('1==================================================')
train.info()  # 每列不为空的个数
print('train.count():' , train.count())
print('2==================================================')

print(train.isna())
print('3==================================================')
print(train.isna().sum())
print('4==================================================')
result = train['Survived'].value_counts()
print(result, type(result))
# 可视化展示
result.plot(kind='pie')  
plt.grid()
# 展示
plt.show()