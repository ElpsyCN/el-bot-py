# el-bot-py 已停止开发。相同功能替代者见 [el-bot-js](https://github.com/ElpsyCN/el-bot-py)

一个基于 [mirai](https://github.com/mamoe/mirai) 开箱即用的 QQ 机器人

## 基础环境

- [java](https://www.java.com/zh_CN/)
- [python (>=3.7)](https://www.python.org/)

## 安装

### 安装 mirai 相关包

```sh
sh install.sh
```

### 初始化虚拟环境

为避免 Python 其他环境包影响，您可以初始化本地虚拟环境。

> [虚拟环境和包](https://docs.python.org/zh-cn/3/tutorial/venv.html)

```sh
python3 -m venv el-env
source el-env/bin/activate
```

#### 设置国内镜像源

```sh
# 阿里云
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

#### Windows

```sh
tutorial-env\Scripts\activate.bat
```

#### Unix Or MacOS

```sh
source tutorial-env/bin/activate
```

### 运行

```py
python3 start.py
# 默认端口 4859
# 1.048596%
```

## Thanks

- [mirai](https://github.com/mamoe/mirai)
- [mirai-console](https://github.com/mamoe/mirai-console)
- [mirai-api-http](https://github.com/mamoe/mirai-api-http)
- [python-mirai](https://github.com/NatriumLab/python-mirai)
- [pyyaml](https://pyyaml.org/)
