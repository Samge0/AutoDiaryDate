#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 上午11:28
# @Author  : Samge
import datetime
from enum import Enum, unique

import settings


@unique
class Week(Enum):
    Mon = '周一'
    Tues = '周二'
    Wed = '周三'
    Thur = '周四'
    Fri = '周五'
    Sat = '周六'
    Sun = '周日'


def date_interval_list(date_start=None, date_end=None, date_format=settings.FORMAT_DATE):
    """
        获取两个日期之间的 日期数组
    :param date_start: 起始日期，格式：
    :param date_end: 结束日期
    :param date_format: 日期格式
    :return: 日期字符串列表
    """
    if not date_start or not date_end:
        raise ValueError('起始日期跟结束日期不能为空')

    datetime_start = datetime.datetime.strptime(date_start, date_format)
    datetime_end = datetime.datetime.strptime(date_end, date_format)
    date_list = [datetime_start.strftime(date_format)]
    while datetime_start < datetime_end:
        datetime_start += datetime.timedelta(days=+1)  # 日期加一天
        date_list.append(datetime_start.strftime(settings.FORMAT_DATE))  # 日期存入列表
    return date_list


def str_to_datetime(date_str, date_format=settings.FORMAT_DATE):
    """
        字符串转datetime格式
    :param date_str: 日期字符
    :param date_format: 日期格式
    :return:
    """
    return datetime.datetime.strptime(date_str, date_format)


def get_week_day_by_str(date_str):
    """
        根据日期字符串获取对应的 星期
    :param date_str: 日期，datetime格式
    :return: 星期x
    """
    return get_week_day(str_to_datetime(date_str))


def get_week_day(date):
    """
        根据日期获取对应的 星期
    :param date: 日期，datetime格式
    :return: 星期x
    """
    week_day_dict = {
        0: Week.Mon.value,
        1: Week.Tues.value,
        2: Week.Wed.value,
        3: Week.Thur.value,
        4: Week.Fri.value,
        5: Week.Sat.value,
        6: Week.Sun.value,
    }
    day = date.weekday()
    return week_day_dict[day]


if __name__ == '__main__':
    data_now = datetime.datetime.now()
    print(get_week_day(data_now))

    print(Week.Mon.value)
    print(Week.Mon)
