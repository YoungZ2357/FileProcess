# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 下午3:50
# @Author  :
# @File    : move_file_core.py
# @Project : FileProcess


import core.move_file_core as mvf


def copy_all(src_dir, dst_dir, by_suffix: bool = False, verbose: bool = True):
    file_paths = mvf.scan_all(src_dir)
    path_pairs = mvf.generate_path_pair(file_paths, dst_dir)

    if by_suffix:
        path_pairs = mvf.change_dst_by_suffix(path_pairs)

    mvf.copy_file(path_pairs, verbose=verbose)

