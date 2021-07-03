"""
@version: python3.8
@project:socketAuto
@file:   yaml_methods.py
@date:   2021/6/3 11:52
@Author: jia
@Desc: yaml文件的增删改查
"""

import yaml

"""
# body = resp.json()
# json.loads():str转dict;
# json.dumps():dict转str;
# json.load(file):将file读取出来
# json.dump(obj,file):将json信息写入文件
"""

# 未实现
def get_project_path():
    path = ''
    return path


class YamlMethod:

    # def get_project_path(self):
    #     path = ''
    #     return path

    # 读取yaml文件数据
    @classmethod
    def read_yaml(cls, f_path):
        with open(f_path, encoding='utf-8', mode='r') as f:
            ff = yaml.load(f, Loader=yaml.FullLoader)
            return ff

    # 向YAML文件写入数据
    @classmethod
    def write_yaml(cls, f_path, f_data):
        with open(f_path, encoding='utf-8', mode='w') as wf:
            yaml.dump(f_data, stream=wf)

    # 将yaml文件内容清除
    @classmethod
    def clear_yaml(cls, f_path):
        with open(f_path, encoding='utf-8', mode='r+') as cf:
            cf.truncate()

    @classmethod
    def read_config_yaml(cls, one_name, two_name):
        with open(str(get_project_path()+'config.yaml.yml.yaml.yml'), encoding='utf-8', mode='r') as rf:
            cfg = yaml.load(rf.read(), Loader=yaml.FullLoader)
            return cfg[one_name][two_name]

    @classmethod
    def read_extract_yaml(cls, one_name):
        with open(str(get_project_path()+'extract.yaml.yaml.yml'), mode='r', encoding='utf-8') as rf:
            extract = yaml.load(rf.read(), Loader=yaml.FullLoader)
            return extract[one_name]


if __name__ == '__main__':
    # fp = '../data/testcase.yaml.yml'
    # YamlMethod.read_yaml(fp)

    f_data = {'name': 'xiao', 'age': 18}
    file_path = '../data/yaml88'
    YamlMethod.write_yaml(file_path, f_data)
    # YamlMethod.clear_yaml(file_path)
