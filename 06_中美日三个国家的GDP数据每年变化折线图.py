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

