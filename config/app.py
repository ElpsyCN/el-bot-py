import os
import yaml
import json


class Config:
    """
    配置读取类 \\
    :var        data[dict]:     包含配置信息的字典 \\
    :method     parse_yaml:     读取配置文件并返回包含配置信息的字典 \\
    :method     print_json:     以JSON形式打印配置文件信息 \\
    :method     merge:          读取目录下所有的配置将其合并并返回包含配置信息的字典
    """

    data = {}

    def parse_yaml(self, file):
        """
        读取配置文件并返回包含配置信息的字典
        :param file[str]:   配置文件的绝对路径或相对路径 \\
        :return[dict]:       包含配置信息的字典，如果没有配置则返回空字典
        """
        return yaml.safe_load(open(file, mode='r', encoding='UTF-8')) or {}

    def print_json(self):
        """
        以JSON形式打印配置文件信息 \\
        :return: None
        """
        print(json.dumps(self.data, ensure_ascii=False, sort_keys=True,
                         indent=2, separators=(',', ': ')))

    def merge(self, folder):
        """
        读取目录下所有的配置将其合并并返回包含配置信息的字典
        :param folder[str]:    配置文件所在目录且不以‘/’结尾 \\
        :return[dict]:   包含配置信息的字典，如果没有配置则返回为空字典
        """
        config = {}
        files = os.listdir(folder)
        for file in files:
            config.update(self.parse_yaml(f'{folder}/{file}'))
        return config

    def __init__(self, path):
        """
        :param path[str]:  配置目录或配置文件路径，目录不以‘/’结尾
        """
        if not os.path.exists(path):
            raise ValueError(f'[{path}]是不存在的路径或文件')
        if os.path.isdir(path):
            self.data = self.merge(path)
        else:
            self.data = self.parse_yaml(path)
