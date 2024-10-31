# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 下午3:50
# @Author  :
# @File    : functional.py
# @Project : FileProcess

import os
import shutil

import move_file.utils as utils


def scan_all(src_dir) -> list:
    """ 获取一个目录下，所有文件的路径
    注：仅用于进一步封装

    :param src_dir: 源文件夹
    :return: 路径列表
    """
    paths = []
    for root, _, files in os.walk(src_dir):
        for file in files:
            paths.append(os.path.join(root, file))

    return paths


def generate_path_pair(file_paths: list, src_dir: str, dst_dir: str) -> list[list]:
    """生成 [原始文件路径, 初始目标文件路径]列表
    注：仅用于进一步封装


    :param file_paths: 路径列表
    :param src_dir: 文件所在目录
    :param dst_dir: 目标路径
    :return:
    """
    path_pairs = []
    for src_path in file_paths:
        relative_path = os.path.relpath(src_path, src_dir)
        sub_dir_name, file_name = os.path.split(relative_path)

        if sub_dir_name:
            new_file_name = f"{sub_dir_name.replace(os.sep, '_')}_{file_name}"
        else:
            new_file_name = f"root_{file_name}"

        dst_file_path = os.path.join(dst_dir, new_file_name)
        path_pairs.append([src_path, dst_file_path])
    return path_pairs


def change_dst_by_suffix(path_pairs: list[list]) -> list[list]:
    updated_pairs = []
    for src_path, dst_path in path_pairs:
        file_extension = os.path.splitext(src_path)[1][1:]
        if not file_extension:
            file_extension = "no_extension"

        dst_dir = os.path.join(os.path.dirname(dst_path), file_extension)
        os.makedirs(dst_dir, exist_ok=True)
        dst_file_path = os.path.join(dst_dir, os.path.basename(dst_path))
        updated_pairs.append([src_path, dst_file_path])
    return updated_pairs


def copy_all(src_dir, dst_dir, by_suffix: bool = False, verbose: bool = True):
    """已停止更新!!!

    执行文件移动的函数式调用，将一个目录下所有文件取到指定位置

    :param src_dir: 待提取文件所在路径
    :param dst_dir: 目标路径
    :param by_suffix: 是否按照后缀归类
    :param verbose: 是否显示复制信息
    :return: None
    """
    file_paths = scan_all(src_dir)
    path_pairs = generate_path_pair(file_paths, src_dir, dst_dir)

    if by_suffix:
        path_pairs = change_dst_by_suffix(path_pairs)

    utils.copy_file(path_pairs, verbose=verbose)
