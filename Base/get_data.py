import os, yaml


class GetData:

    @classmethod
    def get_yml_data(cls, file_name):
        with open('./Data' + os.sep + file_name, 'r', encoding='utf-8')as f:
            return yaml.safe_load(f)
