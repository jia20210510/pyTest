"""
@version: python3.8
@project:socketAuto
@file:   file_methods.py
@date:   2021/6/3 11:52
@Author: jia
@Desc: 文件的增删读写
"""

import yaml
import os
import shutil

"""
# body = resp.json()
# json.loads():str转dict;
# json.dumps():dict转str;
# json.load(file):将file读取出来
# json.dump(obj,file):将json信息写入文件
"""


class FileMethod:

    # 清除文件夹
    @classmethod
    def clean_dir(cls, dir_path):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        else:
            shutil.rmtree(dir_path)
            os.mkdir(dir_path)

    # 取项目根目录
    @classmethod
    def get_project_path(cls, project_name):
        base_dir = os.getcwd()
        root_path = base_dir[:base_dir.find(project_name+"\\") + len(project_name+"\\")]
        project_path = root_path.replace("\\", '/')
        print('project_path:', project_path)
        return project_path

    # 向文件写入
    @classmethod
    def write_file(cls, file_path, write_text):
        with open(file_path, 'w', encoding='utf-8') as wf:
            wf.write(write_text)

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

    # 取根目录中extract文件的值
    @classmethod
    def read_extract_yaml(cls, project_name, one_name):
        with open(str(cls.get_project_path(project_name)+'extract.yaml.yaml.yml'), mode='r', encoding='utf-8') as rf:
            extract = yaml.load(rf.read(), Loader=yaml.FullLoader)
            return extract[one_name]
        
    # 修改yaml数据
    @classmethod
    def test_modify(cls, f_path, in_para, one_name, two_name):
        """
        修改YAML文件参数
        f_path: 打开文件的路径
        in_para: 输入的参数
        one_name: 字典第一个key
        two_name: 字典第二个kdy
        """
        with open(f_path) as f:
            doc = yaml.safe_load(f)
            doc[one_name][two_name] = in_para
        with open(f_path, 'w') as wf:
            yaml.safe_dump(doc, wf, allow_unicode=True)


if __name__ == '__main__':
    p_name = 'pyTest'
    FileMethod.get_project_path(p_name)

    # d_path = 'E:/PycharmProject/pyTest/Report/temp'
    # FilesMethod.clean_dir(d_path)

    # writ = "systems = WIN10\npython = 3.8.8"
    # f_path = 'E:/PycharmProject/pyTest/Report/temp/environment.properties'
    # FilesMethod.write_file(f_path, writ)
