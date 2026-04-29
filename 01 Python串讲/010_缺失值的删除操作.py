import pandas as pd

trian = pd.read_csv('./data/titanic_train.csv')

# trian.info()
new_train1 = trian.dropna()
new_train1.info()

new_train2 = trian.dropna(how='all')
new_train2.info()

new_train3 = trian.dropna(subset='Age') 
new_train3.info()

new_train4 = trian.drop('PassengerId', axis=1)  # 1按列删除
new_train4.info()