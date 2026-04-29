import pandas as pd
import numpy as np

df=pd.read_csv('./data/survey_visited.csv')
print(df)
df = pd.read_csv('data/survey_visited.csv', keep_default_na=False)
print(df)
df = pd.read_csv('data/survey_visited.csv', keep_default_na=False, na_values=[None, np.nan, pd.NA])
print(df)

