#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/10/12 上午11:57
# @Author  : Samge
import os


def save_txt_file(_txt, _path, _type='w+'):
    """保存文件"""
    try:
        with open(_path, _type, encoding='utf-8') as f:
            f.write(_txt)
            f.flush()
            f.close()
        return True
    except:
        return False


def read_txt_file(_path):
    """读取文件"""
    if os.path.exists(_path) is False:
        return None
    with open(_path, "r", encoding='utf-8') as f:  # 打开文件
        data = f.read()
        f.close()
        if data == '':
            return None
        else:
            return data
