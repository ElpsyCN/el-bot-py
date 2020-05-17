class Handler(object):
    def __init__(self, message, config_list: list):
        self.config_list_hit = []
        pass

    def _is_hit(self, message, config):
        """
        判断某个配置是否命中这条消息
        :param  message     对饮的消息
        :param  config      对应的配置
        :return[bool]       是否命中
        """
        pass

    def _get_all_hit_config(self):
        """
        填充 self.config_list_hit
        """
        pass
