#-*- encoding: utf-8 -*-

from datetime import date, datetime, timedelta
import time


## 将标准时间"%Y-%m-%d %H:%M:%S" 转换为计算机时间
def str_to_time(strtime):
    t_tuple = time.strptime(strtime,"%Y-%m-%d %H:%M:%S")
    return time.mktime(t_tuple)
 
def str_to_time2(strtime):
    dt = datetime.strptime(strtime,"%Y-%m-%d %H:%M:%S")
    t_tuple = dt.timetuple()
    return time.mktime(t_tuple)

def format_time_YmdH(strtime):
    datestr = strtime.strftime("%Y-%m-%d %H:%M")
    return datestr

def format_time_Ymd(strtime):
    datestr = strtime.strftime("%Y-%m-%d")
    return datestr

def format_time_m(strtime):
    datestr = strtime.strftime("%Y")
    return datestr

def format_time_m(strtime):
    datestr = strtime.strftime("%m")
    return datestr


def datetime_now_diff(datetimestr):
    '''
        给入的时间字符串，如当前时刻的差值（秒）
    '''
    t_tuple = time.strptime(datetimestr,"%Y-%m-%d %H:%M:%S")
    diff = time.mktime(t_tuple) - time.time()
    return diff


def get_now_datestr():
    return _get_add_datetime(days = 0).strftime('%Y-%m-%d')

def get_now_datestr2():
    return _get_add_datetime(days = 0).strftime('%Y%m%d')

def get_now_datestr3():
    return _get_add_datetime(days = 0).strftime('%Y%m%d%H')

def get_now_datetimestr():
    return _get_add_datetime(days = 0).strftime('%Y-%m-%d %H:%M:%S')

def get_datetimestr_by_time(t):
    return datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

def get_now_datetimestr2():
    return datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

def get_now_datetimestr3():
    return datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')

def get_add_datest(days):
    return _get_add_datetime(days = days).strftime('%Y-%m-%d')

def get_add_datest2(days):
    return _get_add_datetime(days = days).strftime('%Y%m%d')


def get_add_datest3(hours):
    return _get_add_datetime_hours(hours = hours).strftime('%Y%m%d')

def get_add_hourst2(hours):
    return _get_add_datetime_hours(hours = hours).strftime('%H')

def get_add_hourst3(hours):
    return _get_add_datetime_hours(hours = hours).strftime('%Y%m%d%H')


def get_add_datehstr(days):
    return _get_add_datetime(days = days).strftime('%Y%m%d%H')


'''
延迟对应的时间和提早对应的时间(已当前时间为基准)
'''
def _get_add_datetime(days):
    return datetime.now() + timedelta(days=days)

def _get_add_datetime_hours(hours):
    return datetime.now() + timedelta(hours=hours)



def date_string_to_datetime(string):
    return datetime.strptime(string, "%Y-%m-%d")

def str_is_date(string):
    '''判断是否是一个有效的日期字符串'''
    try:
        time.strptime(string, '%Y%m%d')
        return True
    except:
        return False


def sleep(second):
    time.sleep(second)


if __name__ == '__main__':
    print(get_now_datetimestr3())
