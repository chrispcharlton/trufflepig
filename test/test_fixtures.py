import pytest
import os

dir_list = {
    "contents": [
        {
        "type": "directory",
        "name": "FY20",
        "contents": [
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

other_dir_list = {
    "contents": [
        {
        "type": "directory",
        "name": "FY21",
        "contents": [
            {
            "type": "file",
            "name": "dontquityet_2020_10_04.docx"
            },
            {
            "type": "file",
            "name": "dontquityet_2020_10_31.docx"
            }
        ]
        },
        {
        "type": "file",
        "name": "README.txt"
        }
    ]
    }


@pytest.mark.parametrize('dir_list', [dir_list, other_dir_list])
def test_fixture(testing_directory):
    print([f for f in os.walk(testing_directory)])