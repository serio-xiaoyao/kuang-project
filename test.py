import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 解决中文乱码
from matplotlib import font_manager
def set_chinese_font2():
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

my_arr = np.random.randint(low= 1, high= 100, size = (5, 3))
# print(my_arr)

df = pd.DataFrame(my_arr, index=['张三','李四','王五','赵六','田七'], columns=['语文','英语','数学'])
print(df)

print('--------------------')
# 获取各个学科的总成绩
print('语文', df['语文'].sum())
print('英语', df['英语'].sum())
print('数学', df['数学'].sum())

print(df.sum(axis=0))

# 获取各个同学的总成绩
print(df.sum(axis=1))

print('--------------------')
# matplotlib可视化数据
set_chinese_font2()

fig, ax = plt.subpl ots()
ax.scatter(x=df['语文'], y=df['数学'])
ax.set_title('综合案例')

plt.show()