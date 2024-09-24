# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# 设置全局字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
# 加载CSV文件
file_path = 'C:/Users/Dell/Desktop/python practice/python练习/利用高德绘制北京市以及武汉市地铁路线图/wuhansubway.csv'  # CSV文件路径
subway_data = pd.read_csv(file_path, encoding='gbk')  # 假设文件使用GBK编码

# 检查并修正颜色代码
def is_valid_hex_color(s):
    try:
        int(s, 16)
        return len(s) == 6
    except ValueError:
        return False

default_color = '#000000'  # 默认颜色：黑色
subway_data['color'] = ['#' + c if is_valid_hex_color(c) else default_color for c in subway_data['color']]

# 按线路分组数据
grouped = subway_data.groupby('line')

# 初始化绘图
plt.figure(figsize=(10, 10))

# 绘制每条线路
for name, group in grouped:
    plt.plot(group['longitude'], group['latitude'], color=group.iloc[0]['color'], label=name)

# 添加标签和标题
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Beijing Subway Map')
plt.legend()
plt.savefig('C:/Users/Dell/Desktop/python practice/python练习/利用高德绘制北京市以及武汉市地铁路线图/wuhan地铁图.png')

# 显示地图
plt.show()
