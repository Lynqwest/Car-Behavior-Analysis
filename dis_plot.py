'''
    @比赛
    @Author:Y
    @2019/3/18 0018 13:12
'''
'''
画图函数
对distance做时间序列画图
'''
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import datetime
import time

def dis_plot(data,start,end,name):  #每间隔x个作图
    plt.figure()
    fig, ax = plt.subplots(figsize=(18,10))
    x = data.loc[start:end,'location_time']
    y = data.loc[start:end,'distance']

# 设置横轴日期显示格式
    fmt = mdate.DateFormatter('%Y-%m-%d %H h')
    timeArray = [datetime.datetime.strptime(i, '%Y-%m-%d %H:%M:%S') for i in x]

    plt.plot(timeArray, y, 'b')
    ax.xaxis.set_major_formatter(fmt)
    plt.xticks(rotation=45)
    plt.yticks([0,0.1])
    plt.tight_layout()
    print('%s 作图已完成'%name)
    plt.savefig(name)

    # plt.show()

# 时间戳转换为 字符串
def timestamp_to_date(time_stamp, ):
    format_string = "%Y-%m-%d %H:%M:%S"
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date


data = pd.read_csv('AA00002_normal.csv')
length = data.shape[0]
data['location_time'] = data['location_time'].apply(timestamp_to_date)
name = 'AA00002_normal'
dis_plot(data,0,length,name)
