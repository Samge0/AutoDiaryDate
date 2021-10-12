#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 上午11:28
# @Author  : Samge
import templates
from utils import TaskUtil

if __name__ == '__main__':
    TaskUtil.create_diary_date(template=templates.TEMPLATE_DEFAULT3)
    # TaskUtil.create_diary_date(template=templates.TEMPLATE_DEFAULT)
