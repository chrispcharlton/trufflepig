import os
import pytest
import shutil

@pytest.fixture(scope='session')
def testing_directory(tmpdir_factory):
    root_a = tmpdir_factory.mktemp('A')
    root_a.join('wow.txt').write('h')
    root_a.join('A1.csv').write('h')

    root_b = tmpdir_factory.mktemp('B')
    root_b.join('hey.txt').write('h')
    return tmpdir_factory

def test_delete_files(testing_directory):
    for root, _, files in os.walk(testing_directory.getbasetemp().strpath):
        for name in files:
            print(os.path.join(root, name))
    assert len(files)