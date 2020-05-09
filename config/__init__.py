from . import app

# plugins/MiraiAPIHTTP setting
mirai_setting = app.Config('./plugins/MiraiAPIHTTP/setting.yml')
# mirai_setting.print_json()
setting = mirai_setting.data

# default config
default = app.Config('./config/default/')
# default.print_json()

# custom config
custom = app.Config('./config/custom/')
# custom .print_json()

data = default.data.copy()
data.update(custom.data)
