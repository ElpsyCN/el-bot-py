import yaml
# plugins/MiraiAPIHTTP setting
stream = open('./plugins/MiraiAPIHTTP/setting.yml')
setting = yaml.safe_load(stream)

# custom config
stream = open('./config/config.yml')
data = yaml.safe_load(stream)
