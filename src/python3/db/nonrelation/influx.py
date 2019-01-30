# -* - coding: UTF-8 -* -

import time

from influxdb import InfluxDBClient


def read_info():
    data_list = [{
        'measurement': 'cpu_usage_average',
        'tags': {'resId': '3231'},
        'fields': {
            'time': resId_time_info[0],
            'agentId': resId_time_info[1],
            'name': resId_time_info[5],
            'value': resId_time_info[10,
        }
    }]
    return data_list


if __name__ == '__main__':
    client = InfluxDBClient("10.200.132.160", 8086, "admin", "admin", "c0e5bfa8487e432ea17554db684aedea")
    counts = 0  # 计数,也就是数据上传20次
    while counts <= 20:  #
        counts += 1
        client.write_points(read_info())
        time.sleep(5)
