'''
    @dis_plot.py
    @Author:Y
    @2019/4/22 0022 13:46
'''
from math import sin, asin, cos, radians, fabs, sqrt, pi, atan2, degrees, tan
import pandas as pd
import os
# 求解两个点距离
def hav(theta):
    s = sin(theta / 2)
    return s * s


def get_distance_hav(lat0, lng0, lat1, lng1):
    EARTH_RADIUS = 6371  # 地球平均半径，6371km
    "用haversine公式计算球面两点间的距离。"
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)

    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))

    return distance


# 判断是否为不正常
def isabnormal(data, threshold):
    abnormal_index = data[data['distance'] > threshold]

    return abnormal_index.index


def set_distance(data, info):
    data.loc[:, 'distance'] = 0
    length = data.shape[0]
    for i in range(1, length):
        lon1, lat1 = data.loc[i - 1, 'lng'], data.loc[i - 1, 'lat']
        lon2, lat2 = data.loc[i, 'lng'], data.loc[i, 'lat']
        d = get_distance_hav(lat1, lon1, lat2, lon2)
        data.loc[i, 'distance'] = d

    threshold = 0.040  # 0.033
    abnormal_index = isabnormal(data, threshold)
    data_normal = data.drop(abnormal_index)
    output = info.split('.')[0] + '_normal' + '.csv'  # 忘改输出。。。。。。。。。。。
    data_normal.to_csv(output, index=False)

def main():
    for info in os.listdir(r'C:\Users\Administrator\Desktop\13000123sgik\第七届泰迪杯赛题C题-全部数据\附件1-全部数据-450辆车'):
        if info.endswith('csv'):
            data = pd.read_csv(info)
            set_distance(data, info)

            print('%s 已完成' % info)

if __name__ =='__main__':
    main()