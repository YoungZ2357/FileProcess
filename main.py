# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 下午3:44
# @Author  :
# @File    : main.py
# @Project : FileProcess

import functions as f


if __name__ == '__main__':
    src = "tests/testfiles"
    dst = "tests/dst"
    f.copy_all(src, dst)

