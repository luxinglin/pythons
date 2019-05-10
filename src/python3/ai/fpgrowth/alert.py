import datetime

import main
import pymysql


class Alert:
    def __init__(self, _id, company_id, alert_time, alert_content):
        self._id = _id
        self._company_id = company_id
        self._alert_time = alert_time
        self._alert_content = alert_content
        self._index = None

    def get_id(self):
        return self._id

    def get_company_id(self):
        return self._company_id

    def get_alert_time(self):
        return self._alert_time

    def get_alert_content(self):
        return self._alert_content

    def get_index(self):
        return self._index

    def set_index(self, _index):
        if self._index is None:
            self._index = _index


conn = {
    'host': '10.200.132.160',
    'user': 'root',
    'password': 'Pioneer@2017',
    'database': 'dcim-saas-dev',
    'port': 3306
}


def __init__():
    # 打开数据库连接
    db = pymysql.connect(**conn)

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    return db, cursor


def select_alert_data():
    alert_sql = "select t1.ALERT_ID,t1.COMPANY_ID,t1.ALERT_START_TIME,t1.ALERT_CONTENT " \
                " from (" \
                " select alert_id,COMPANY_ID,ALERT_START_TIME,ALERT_CONTENT from alert " \
                " union ALL " \
                " select alert_id,COMPANY_ID,ALERT_START_TIME,ALERT_CONTENT from alert_history " \
                " ) as t1 where t1.COMPANY_ID=16 and t1.ALERT_START_TIME > '2019-05-01 00:00:00' order by COMPANY_ID asc, ALERT_START_TIME asc;"

    db, cursor = __init__()
    cursor.execute(alert_sql)
    results = cursor.fetchall()

    close_db(db, cursor)

    return results


def close_db(db, cursor):
    # 关闭数据库连接
    cursor.close()
    db.close()


def construct_alert_index(alert_rows):
    _alerts = []
    var_dict = {}
    idx = 1
    for row in alert_rows:
        key = row[3]
        _alert = Alert(row[0], row[1], row[2], row[3])
        if key in var_dict:
            _alert.set_index(var_dict.get(key))
        else:
            _alert.set_index(idx)
            # new index
            var_dict[key] = idx
            idx += 1

        _alerts.append(_alert)

    return _alerts, var_dict


def construct_fp_set(_time_window, _alerts):
    delta_time = 3 * 60
    first_time = _alerts[0].get_alert_time()
    last_time = _alerts[_alerts.__len__() - 1].get_alert_time()
    gap = last_time - first_time
    print("loop total count:", int((gap.seconds + gap.days * 24 * 60 * 60) / delta_time))

    _raw_data = []
    begin = first_time
    while begin < last_time:
        items = []
        _time_end = begin.__add__(datetime.timedelta(seconds=_time_window))
        for _alert in _alerts:
            if _alert.get_alert_time() <= _time_end:
                if _alert.get_index() not in items:
                    items.append(_alert.get_index())
            else:
                break

        if items.__len__() > 0:
            _raw_data.append(items)

        begin = begin.__add__(datetime.timedelta(seconds=delta_time))

    return _raw_data


if __name__ == '__main__':
    rows = select_alert_data()
    alerts, _dict = construct_alert_index(rows)
    for alert in alerts:
        print(" index:", alert.get_index(), ", alert_start_time:", alert.get_alert_time())

    # 时间窗口定位10分钟
    time_window = 5 * 60
    print("construct transactions")

    raw_data = construct_fp_set(time_window, alerts)
    for data in raw_data:
        print(data)

    # begin to compute result
    min_support = 2

    main.calculate_fp(raw_data, min_support)
