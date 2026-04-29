# 1.导包
import random

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
# 需求：绘制每个月销量曲线图
# 2.准备测试数据
a = [i for i in range(1, 13)]
nums = [random.randint(0, 100) for n in a]

# 3.绘图

plt.plot(a, nums)
plt.title('matplotlib')

plt.xlabel('月份')
plt.ylabel('销量')
plt.show()