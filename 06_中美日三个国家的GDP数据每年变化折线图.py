import matplotlib.pyplot as plt
import pandas as pd

# 解决个别版本show()无法展示图的问题
import matplotlib
matplotlib.use('TkAgg')

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
set_chinese_font()  # 解决中文乱码问题

# 读取数据
df = pd.read_csv('data/1960-2019全球GDP数据.csv', encoding='gbk', sep=',')
# print(df)
# print(df['year'])
# print(df['country'])
# print('数据形状:', df.shape)  # 形状(9931, 3)
# print('维度：', df.ndim)
# print(df.head())
# print(df.tail())
# print('获取所有列名：', df.columns)
# print('获取所有行索引：', df.index)
# print('各个列的个数：', df.count())
# print('基本信息：', df.info())

# 数据预处理
df.dropna(inplace=True)
# print('数据形状:', df.shape)  # 形状(9930, 3)

# 数据分析 
# 查询中美日的GDP数据
df_usa = df[df['country'] == '美国']
df_china = df[df['country'] == '中国']
df_japan = df[df['country'] == '日本']
# print(df_usa)
# print(df_china)
# print(df_japan)


# 把年份作为索引列
df_usa.set_index('year', inplace=True)
df_china.set_index('year', inplace=True)
df_japan.set_index('year', inplace=True)


# 把GDP列名依次修改为中国、美国、日本
df_usa.rename(columns={'GDP': 'gdp_usa'}, inplace=True)
df_china.rename(columns={'GDP': 'gdp_china'}, inplace=True)
df_japan.rename(columns={'GDP': 'gdp_japan'}, inplace=True)

print(df_usa.head())
print(df_china.head())
print(df_japan.head())

# 可视化展示中美日GDP数据折线图
plt.title('中美日三个国家的GDP数据每年变化折线图')
plt.plot(df_usa.index, df_usa['gdp_usa'], label='美国', color = 'red')
# 在折线图上显示每个年份的美国 GDP 值
# for x, y in zip(df_usa.tail().index, df_usa['gdp_usa'].tail()):
#     plt.annotate(f'{y:.0f}', xy=(x, y), xytext=(0, 5), 
#                  textcoords='offset points', fontsize=7, ha='center')
    
plt.plot(df_china.index, df_china['gdp_china'], label='中国', color = 'green')
# 在折线图上显示每个年份的中国 GDP 值
# for x, y in zip(df_china.tail().index, df_china['gdp_china'].tail()):
#     plt.annotate(f'{y:.0f}', xy=(x, y), xytext=(0, 5), 
#                  textcoords='offset points', fontsize=7, ha='center')
    
plt.plot(df_japan.index, df_japan['gdp_japan'], label='日本', color = 'blue')
# 在折线图上显示每个年份的日本 GDP 值
# for x, y in zip(df_japan.tail().index, df_japan['gdp_japan'].tail()):
#     plt.annotate(f'{y:.0f}', xy=(x, y), xytext=(0, 5), 
#                  textcoords='offset points', fontsize=7, ha='center')


 
plt.legend()  # 添加图例
plt.grid()  # 添加网格线
plt.show()  # 显示图表