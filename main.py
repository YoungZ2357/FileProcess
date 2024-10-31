# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 下午3:44
# @Author  :
# @File    : main.py
# @Project : FileProcess

import move_file as mvf


if __name__ == '__main__':
    src = r""
    dst = r""
    mvf.copy_all(src, dst, by_suffix=False)
    pass
