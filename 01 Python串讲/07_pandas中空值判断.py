# 1. 导包
import pandas as pd
import numpy as np

# 2.先认识空值
print(None, type(None))  # 原生Python中的空值
print(np.nan, type(np.nan))  # numpy中的空值
print(pd.NA, type(pd.NA))  # pandas中的空值

print(pd.isna(None))  # True
print(pd.isna(np.nan))  # True
print(pd.isna(pd.NA))  # True
