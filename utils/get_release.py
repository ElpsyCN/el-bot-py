import os
import requests
import urllib


class LatestRelease:
    owner = ''
    repo = ''
    data = ''
    path = ''
    browser_download_url = ''

    def display_status(self):
        print(f'{self.owner}/{self.repo} 最新版本：{self.get_latest_version()}')

    def get_latest_version(self):
        return self.data['tag_name']

    def get_latest_filename(self):
        arr = self.browser_download_url.split('/')
        return arr[-1]

    def is_latest_version_exist(self):
        return os.path.exists(f'{self.path}/{self.get_latest_filename()}')

    def download(self):
        def reporthook(blocks, block_size, total_size):
            """
            显示下载进度
            :param blocks: 已经下载的数据块
            :param block_size: 数据块的大小
            :param total_size: 远程文件大小
            :return: None
            """
            print("下载中: %5.1f%%" % (blocks * block_size * 100.0 / total_size))
        urllib.request.urlretrieve(
            self.browser_download_url, f'{self.path}/{self.get_latest_filename()}', reporthook)

    def __init__(self, origin, owner, repo, path='.'):
        """https://developer.github.com/v3/repos/releases/#get-the-latest-release"""
        url = ''
        if origin == 'github':
            url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
        else:
            raise ValueError(f'[{origin}]不受支持的依赖来源')

        self.owner = owner
        self.repo = repo
        self.data = requests.get(url).json()
        self.path = path
        self.browser_download_url = self.data['assets'][0]['browser_download_url']
