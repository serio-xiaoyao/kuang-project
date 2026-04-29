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

# 分别计算RFM的分数
F_score = pd.cut(F_data, 5, labels=[1, 2, 3, 4, 5])
M_score = pd.cut(M_data, 5, labels=[1, 2, 3, 4, 5]) 
print('6-----------------------------')
print(F_score)
print(M_score)

# 基于一个基础时间，计算R分数
base_time = pd.to_datetime('2022-04-01')
R_days = (R_data - base_time).dt.days
R_score = pd.cut(R_days, 5, labels=[1, 2, 3, 4, 5])
print('7-----------------------------')
print(R_score)

# 合并分数
rfm_list = [R_score, F_score, M_score]
rfm_cols = ['R_score', 'F_score', 'M_score']
rfm_df = pd.DataFrame(np.array(rfm_list).transpose(), dtype=np.int32, columns=rfm_cols, index=F_data.index)
print('8-----------------------------')
print(rfm_df)

# 商家根据自己的需求：设置关注用户交易时间、次数、金额的权重
rfm_df['rfm_w_score'] = rfm_df['R_score'] * 0.2 + rfm_df['F_score'] * 0.3 + rfm_df['M_score'] * 0.5
print('9-----------------------------')
print(rfm_df)

# 分析结果可视化
# 自定义分层阈值，设置会员等级
bins = [0, 2, 3, 5]
labels = ['低', '中', '高']
# 打分
rfm_df['客户分类'] = pd.cut(rfm_df['rfm_w_score'], bins=bins, labels=labels)
print('10-----------------------------')  
print(rfm_df)

# 绘制柱状图
import matplotlib.pyplot as plt
from matplotlib import font_manager
def set_chinese_font():
    # 按常见系统顺序选择可用中文字体，避免写死单一字体导致告警。
    candidates = [
        "PingFang SC",
        "Hiragino Sans GB",
        "Heiti SC",
        "STHeiti",
        "Microsoft YaHei",
        "SimHei",
        "SimSun",
        "Noto Sans CJK SC",
        "Source Han Sans SC",
        "WenQuanYi Zen Hei",
        "Arial Unicode MS",
    ]
    available_fonts = {font.name for font in font_manager.fontManager.ttflist}

    for font_name in candidates:
        if font_name in available_fonts:
            plt.rcParams["font.family"] = "sans-serif"
            plt.rcParams["font.sans-serif"] = [font_name]
            break

    plt.rcParams["axes.unicode_minus"] = False


set_chinese_font()
rfm_df['客户分类'].value_counts().plot(kind='bar', color=['blue', 'orange', 'green'])
plt.title('RFM客户分群')
plt.xlabel('会员等级')
plt.ylabel('会员数量')
plt.grid()
plt.show()

# 分析结果保存到本地
rfm_df.to_csv('./data/sales_rfm_score.csv', sep='\t')