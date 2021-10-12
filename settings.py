#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 上午11:28
# @Author  : Samge

# 起始日期
DATE_START = '2021-01-01'

# 结束日期
DATE_END = '2099-12-31'

# 保存的目录，默认在当前项目路径下
# ！！【注意】！！如果修改这个路径，记得将 AUTO_CLEAN 设置为False，避免因误操作导致该目录下所有文件丢失！
SAVE_DIR = 'results'

# 是否在每次任务执行前自动清空 SAVE_DIR 目录下的文件，默认 True
AUTO_CLEAN = True

# 是否需要星期信息，如果这个为False，则 SPLIT_LINE_FOR_WEEK 会自动失效，默认 True
NEED_WEEK = True

# 是否用分割线区分每周，默认 True
SPLIT_LINE_FOR_WEEK = True

# 是否按【月份】生成单独文件，默认 True
SPLIT_BY_MONTH = True

# 是否按【年份】生成单独文件夹，默认 True
SPLIT_BY_YEAR = True

# 日期显示格式
FORMAT_DATE = '%Y-%m-%d'
