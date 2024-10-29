# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 下午4:23
# @Author  : Qingyang Zhang
# @File    : move_file_core.py
# @Project : FileProcess

import os
import shutil


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


def generate_path_pair(file_paths: list, dst_dir: str) -> list[list]:
    """生成 [原始文件路径, 初始目标文件路径]列表
    注：仅用于进一步封装

    :param file_paths: 路径列表
    :param dst_dir: 目标路径
    :return:
    """
    path_pairs = []

    for src_path in file_paths:
        file_name = os.path.basename(src_path)

        dst_file_path = os.path.join(dst_dir, file_name)
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


def copy_file(path_pairs, verbose: bool = True) -> None:
    """根据[原始文件路径, 初始目标文件路径] 执行复制操作


    :param path_pairs: [原始文件路径, 初始目标文件路径] 列表
    :param verbose: 显示复制的执行信息
    :return:
    """
    for src_path, dst_path in path_pairs:
        shutil.copy2(src_path, dst_path)
        if verbose:
            print(f"[{f'{src_path}':<50}] ---COPIED---> [{f'{dst_path}':<50}]")
