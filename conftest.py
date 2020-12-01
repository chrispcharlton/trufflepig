import pytest
import json


@pytest.fixture()
def dir_list():
    return {'contents': [{'type': 'directory',
                          'name': 'truffles',
                          'contents': [{'type': 'file', 'name': 'trufflecount.txt'},
                                       {'type': 'file', 'name': 'trufflepic.png'}]},
                         {'type': 'file', 'name': 'README.txt'}]}


def load_dir_list(file):
    return json.loads(open(file, 'r').read())


def tree_builder(path, path_list):
    for item in path_list:
        if item["type"] == "file":
            path.join(item["name"]).write('CONTENT')
        elif item["type"] == "directory":
            new_dir_path = path.mkdir(item["name"])
            if "contents" in item.keys() and isinstance(item["contents"], list):
                subdir = new_dir_path
                tree_builder(subdir, item["contents"])


@pytest.fixture()
def testing_directory(tmpdir, dir_list):
    tree_builder(tmpdir, dir_list["contents"])
    return tmpdir
