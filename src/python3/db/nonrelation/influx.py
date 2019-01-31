# -* - coding: UTF-8 -* -

from influxdb import InfluxDBClient
from excel.excelWrite import export_to_excel


def read_info():
    res_id_time_info = [1, 2, 3, 4]
    data_list = [{
        'measurement': 'cpu_usage_average',
        'tags': {'resId': '3231'},
        'fields': {
            'time': res_id_time_info[0],
            'agentId': res_id_time_info[1],
            'name': res_id_time_info[2],
            'value': res_id_time_info[3]
        }
    }]
    return data_list


if __name__ == '__main__':
    client = InfluxDBClient("10.200.132.160", 8086, "admin", "admin", "c0e5bfa8487e432ea17554db684aedea")
    # print(client.get_list_database())
    result = client.query('show measurements;')
    # 显示数据库中的表

    result = client.query("select * from cpu_usage_average where resId='3267' order by time desc limit 100; ")

    data_dic = {
        'time': '2019-01-23T08:24:20Z',
        'agentId': None,
        'agentId_1': '55',
        'instance': None,
        'metricCnName': 'CPU平均使用率（百分比）',
        'metricName': 'cpu_usage_average',
        'name': None,
        'name_1': '131.115 (prod-service115)',
        'pluginId': '1',
        'resCategoryCode': 'VC_VM',
        'resId': '3267',
        'resName': '131.115 (prod-service115)',
        'value': 32
    }

    data_list = []
    # column headers
    data_list.append(data_dic.keys())

    for items in result:
        for item in items:
            data = []
            for key in data_dic.keys():
                # 数据拆解
                data.append(item[key])

            # 追加数据
            data_list.append(data)

    export_to_excel(data_list, "cpu_usage_average.xls")
