import copy


class PlainHandler(src.core.Handler):
    """
    :var    config_list_hit[list]:       包含被命中的配置的列表
    """

    def __init__(self, message, config_list: list):
        self.message = copy.deepcopy(message)
        self.config_list = copy.deepcopy(config_list)
        self.config_list_hit = []

    def _is_hit(self, config):
        pass

    def _get_all_hit-config(self):
        pass
