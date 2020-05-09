import os
import requests
import urllib


class LatestRelease:
    """
    :var        target[str]:                    依赖目标 \\
    :var        path[str]:                      依赖下载目录 \\
    :var        browser_download_url[str]:      依赖下载链接 \\
    :method     display_status:                 打印最新版本信息 \\
    :method     get_latest_version:             获取最新的依赖的版本号 \\
    :method     get_latest_filename:            获取最新的依赖文件名 \\
    :method     is_latest_version_exist:        检查本地是否存在最新的依赖 \\
    :method     download:                       下载最新的依赖到本地
    """

    target = ''
    _data = ''
    path = ''
    browser_download_url = ''

    def display_status(self):
        """
        打印最新版本信息\\
        :return: None
        """
        print(f'{self.target} 最新版本：{self.get_latest_version()}')

    def get_latest_version(self):
        """
        获取最新的依赖的版本号 \\
        :return[str]: 最新的版本号
        """
        return self._data['tag_name']

    def get_latest_filename(self):
        """
        获取最新的依赖文件名 \\
        :return[str]: 最新版本的文件名
        """
        arr = self.browser_download_url.split('/')
        return arr[-1]

    def is_latest_version_exist(self):
        """
        检查本地是否存在最新的依赖 \\
        :return[bool]: 本地是否存在最新的依赖版本
        """
        return os.path.exists(f'{self.path}/{self.get_latest_filename()}')

    def download(self):
        """
        下载最新的依赖到本地 \\
        :return: None
        """
        def reporthook(blocks, block_size, total_size):
            """
            显示下载进度 \\
            :param blocks:          已经下载的数据块 \\
            :param block_size:      数据块的大小 \\
            :param total_size:      远程文件大小 \\
            :return: None
            """
            print("下载中: %5.1f%%" % (blocks * block_size * 100.0 / total_size))
        urllib.request.urlretrieve(
            self.browser_download_url, f'{self.path}/{self.get_latest_filename()}', reporthook)

    def __init__(self, origin, target, path='.'):
        """
        https://developer.github.com/v3/repos/releases/#get-the-latest-release \\
        :param origin[str]:    依赖来源，目前支持github \\
        :param target[str]:    依赖目标，对于来源为github的依赖，格式为{owner}/{repo} \\
        :param path[str]:      下载路径，不包含文件名且不以‘/’结尾 
        """
        url = ''
        if origin == 'github':
            url = f'https://api.github.com/repos/{target}/releases/latest'
        else:
            raise ValueError(f'[{origin}]是不受支持的依赖来源')

        self.target = target
        self._data = requests.get(url).json()
        self.path = path
        self.browser_download_url = self._data['assets'][0]['browser_download_url']
