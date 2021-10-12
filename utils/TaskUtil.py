#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 下午2:28
# @Author  : Samge
import os
import shutil
import warnings

from utils import FileUtil, DateUtil
import settings
import templates


def create_diary_date(template=templates.TEMPLATE_DEFAULT):
    """
    生成日志的日期信息
    :param template: 内容模板
    :return:
    """
    # 当前年份
    curr_year = None

    if settings.AUTO_CLEAN and os.path.exists(settings.SAVE_DIR):
        shutil.rmtree(settings.SAVE_DIR)  # 清空结果目录

    date_list: [str] = DateUtil.date_interval_list(settings.DATE_START, settings.DATE_END)  # 日期列表
    save_temp_list: [str] = []  # 要保存的文本
    for i in range(len(date_list)):
        curr_date = get_list_item(date_list, i)
        if not curr_date:
            continue

        # 判断是否按【年份】拆分
        if not curr_year:
            curr_year = curr_date[:4]
        elif settings.SPLIT_BY_YEAR and is_year_end(date_list, i, curr_year):
            append_week_info(curr_date, save_temp_list, template=template)
            save_temp_list = save_file(curr_date, save_temp_list)
            curr_year = f'{int(curr_year) + 1}'
            continue

        # 判断是否按【月份】拆分
        if settings.SPLIT_BY_MONTH and is_month_end(date_list, i):
            append_week_info(curr_date, save_temp_list, template=template)
            save_temp_list = save_file(curr_date, save_temp_list)
            continue

        append_week_info(curr_date, save_temp_list, template=template)

    if len(save_temp_list) > 0:
        save_file(curr_date, save_temp_list)  # 将列表剩余数据写入文件


def append_week_info(curr_date, save_temp_list, template=templates.TEMPLATE_DEFAULT):
    """
    解析星期信息并拼接
    :param curr_date: 当前日期
    :param save_temp_list:
    :param template: 内容模板
    :return:
    """
    week = DateUtil.get_week_day_by_str(curr_date) if settings.NEED_WEEK else ''
    week_info = f'【{week}】' if settings.NEED_WEEK else ''
    save_temp_list.append(template.format(DATE=curr_date, WEEK=week_info))
    if settings.SPLIT_LINE_FOR_WEEK and week == DateUtil.Week.Sun.value:
        save_temp_list.append(templates.TEMPLATE_SPLIT_LINE)


def save_file(curr_date, save_temp_list):
    """
    将临时列表中的数据写入文件，
        然后清空已写入的数据并返回空的临时列表
    :param curr_date:
    :param save_temp_list:
    :return:
    """
    if not os.path.exists(settings.SAVE_DIR):
        os.mkdir(settings.SAVE_DIR)

    # 根据配置生成对应的目标文件路径
    parent_dir = create_year_dir(curr_date) if settings.SPLIT_BY_YEAR else settings.SAVE_DIR
    if settings.SPLIT_BY_MONTH:
        file_name = f'{parent_dir}/{curr_date[:7]}.txt'
    elif settings.SPLIT_BY_YEAR:
        file_name = f'{parent_dir}/{curr_date[:4]}.txt'
    else:
        file_name = f'{settings.SAVE_DIR}/{settings.DATE_START}-{settings.DATE_END}.txt'

    # 保存文件
    save_txt = ''.join(save_temp_list)
    FileUtil.save_txt_file(save_txt, file_name)
    print(f'已生成：{file_name}')

    # 保存完毕后清空临时数据
    save_temp_list = []
    return save_temp_list


def create_year_dir(curr_date):
    """
    创建年份目录
    :param curr_date:
    :return:
    """
    dir_year = f"{settings.SAVE_DIR}/{curr_date[:4]}"
    if not os.path.exists(dir_year):
        os.mkdir(dir_year)
    return dir_year


def get_list_item(lst, i):
    """
    获取列表某一下标的值
        如果列表为空或者索引越界，则返回None
    :param lst: 列表
    :param i: 下标
    :return:
    """
    if not lst \
            or i < 0 \
            or i >= len(lst):
        return None
    return lst[i]


def is_month_end(save_temp_list, i):
    """
    判断是否某月最后一天
    :param save_temp_list: 日期连续列表，正序
    :param i: 日期下标
    :return:
    """
    next_date = get_list_item(save_temp_list, i + 1)
    return next_date and next_date.split('-')[-1] == '01'


def is_year_end(save_temp_list, i, curr_year):
    """
    判断是否某年最后一天
    :param save_temp_list: 日期连续列表，正序
    :param i: 日期下标
    :param curr_year: 当前记录的年份
    :return:
    """
    next_date = get_list_item(save_temp_list, i + 1)
    return next_date and next_date.split('-')[0] != curr_year


def group_file_by_year():
    """
    按照年份拆分目录

        【当前弃用该方法】
        原先是打算先生成文件再移动位置，后面改为在 save_file 方法中生成文件时直接根据配置生成对应的年份目录，故弃用；

    :return:
    """
    warnings.warn("some_old_function is deprecated", DeprecationWarning)

    for path in os.listdir(settings.SAVE_DIR):
        srcfile = f'{settings.SAVE_DIR}/{path}'  # 源文件路径
        if os.path.isdir(srcfile):
            continue

        # 生成年份目录
        dir_year = f"{settings.SAVE_DIR}/{path.split('-')[0]}" if '-' in path else f"{settings.SAVE_DIR}/{path.split('.')[0]}"
        if not os.path.exists(dir_year):
            os.mkdir(dir_year)

        dstfile = f'{dir_year}/{path}'  # 目标文件路径
        shutil.move(srcfile, dstfile)
        print(f'文件移动成功：{srcfile} -> {dstfile}')
