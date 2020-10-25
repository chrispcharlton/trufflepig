import os
import pytest
from pathlib import Path

dir_list = [{
    "type": "directory",
    "name": "FYs",
    "children": [
        {
        "type": "directory",
        "name": "FY20",
        "children": [
            {
            "type": "file",
            "name": "letterofresignation_2020_10_04.docx"
            },
            {
            "type": "file",
            "name": "letterofresignation_2020_10_31.docx"
            }
        ]
        },
        {
        "type": "file",
        "name": "README.txt"
        }
    ]
    }
]

def tree_builder(path, path_list):
    for item in path_list:
        if item["type"] == "file":
            path.join(item["name"]).write('CONTENT')
        elif item["type"] == "directory":
            new_dir_path = path.mkdir(item["name"])
            if "children" in item.keys() and isinstance(item["children"], list):
                subdir = new_dir_path
                recursive_tree_builder(subdir, item["children"])

@pytest.fixture()
def testing_directory(tmpdir):
    tree_builder(tmpdir, dir_list)
    return tmpdir

def test_files_presence(testing_directory):
    i = 0
    for root, dirs, files in os.walk(testing_directory):
        print(f"Found {len(files)} files")
        for name in files:
            i += 1
            print(os.path.join(root, name))
    print(f"Found {i} files in total")
    assert len(files)
