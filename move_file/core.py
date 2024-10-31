# -*- coding: utf-8 -*-
# @Time    : 2024/10/30 下午10:54
# @Author  : Qingyang Zhang
# @File    : core.py
# @Project : FileProcess
import os
import move_file.utils as utils
from typing import Union


class CopyMission:

    def __init__(self, src_dir: str, dst_dir: str):
        """

        :param src_dir: 文件所在目录
        :param dst_dir: 目标路径
        """
        self.src_dir = src_dir
        self.dst_dir = dst_dir
        assert isinstance(src_dir, str) and isinstance(src_dir, str)
        assert src_dir is not None and dst_dir is not None
        self.path_pairs = self.__scan()

    def __str__(self):
        template = f"{f'MISSION INFOS':=^80}\n"
        template += f'{f"NUMBER OF COPY ACTIONS:{len(self.path_pairs)}":<80}\n'
        template += f'{f"SOURCE DIRECTORY: {self.src_dir}":<80}\n'
        template += f'{f"DESTINATION DIRECTORY: {self.dst_dir}":<80}\n'
        return template

    def show_copylink(self) -> None:
        for elem in self.path_pairs:
            print(elem)

    def run(self, verbose: bool = True) -> None:
        flag = input("COPY THE FILES NOW?(insert q to quit)")
        if flag.lower() == 'q':
            return None
        else:
            assert self.path_pairs is not None
            utils.copy_file(self.path_pairs, verbose=verbose)

    def __scan(self):
        """ 用于直接生成所有的 [原始文件路径, 初始目标文件路径] 列表
        注：仅用于CopyMission类的构造器，不可外部调用

        :return: [原始文件路径, 初始目标文件路径] 列表
        """
        paths = []
        for root, _, files in os.walk(self.src_dir):
            for file in files:
                paths.append(os.path.join(root, file))

        return paths

    @staticmethod
    def __sort_by_suffix(path_pairs) -> list:
        """按照后缀名重新定位目标路径
        具体表现为：属于同一种后缀名的文件会被归类到 {目标路径}/{后缀名} 的目录下
        注：该方法只允许内部调用
        :param path_pairs:
        :return:
        """
        new_pairs = []
        for src_path, dst_path in path_pairs:
            file_extension = os.path.splitext(src_path)[1][1:]
            if not file_extension:
                file_extension = "no_extension"
            dst_dir = os.path.join(os.path.dirname(dst_path), file_extension)
            os.makedirs(dst_dir, exist_ok=True)
            dst_file_path = os.path.join(dst_dir, os.path.basename(dst_path))
            new_pairs.append([src_path, dst_file_path])
        return new_pairs

    def sort_by_suffix(self) -> None:
        """按照后缀名重新定位目标路径
        具体表现为：属于同一种后缀名的文件会被归类到 {目标路径}/{后缀名} 的目录下
        该方法是暴露给用户的实际调用方法
        :return: 无返回值
        """
        self.path_pairs = self.__sort_by_suffix(self.path_pairs)

    @staticmethod
    def __filter_by_name(path_pairs, kw: Union[str, list]) -> list:
        new_path_pairs = []
        assert isinstance(kw, str) and isinstance(kw, list)
        if isinstance(kw, str):
            for elem in path_pairs:
                if os.path.basename(elem[1]) == kw:
                    new_path_pairs.append(elem)
                else:
                    continue
        elif isinstance(kw, list):
            for elem in path_pairs:
                if os.path.basename(elem[1]) in kw:
                    new_path_pairs.append(elem)
                else:
                    continue
        else:
            raise "Wrong key word type"
        return new_path_pairs

        pass

    def filter_by_name(self, kw: Union[str, list]) -> None:
        self.path_pairs = self.__filter_by_name(self.path_pairs, kw)
