# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 下午4:23
# @Author  : Qingyang Zhang
# @File    : utils.py
# @Project : FileProcess
import shutil


def copy_file(path_pairs, verbose: bool = True) -> None:
    """根据[原始文件路径, 初始目标文件路径] 执行复制操作


    :param path_pairs: [原始文件路径, 初始目标文件路径] 列表
    :param verbose: 显示复制的执行信息
    :return:
    """
    for src_path, dst_path in path_pairs:
        shutil.copy2(src_path, dst_path)
        if verbose:
            print(f"[{f'{src_path}':<30}] ---COPIED---> [{f'{dst_path}':<30}]")
