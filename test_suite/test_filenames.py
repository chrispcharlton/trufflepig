import os
import pytest

@pytest.fixture()
def testing_directory(tmpdir):
    #Writing two .xlsx files with diferent dates in the string in the parent dir
    tmpdir.join('letterofresignation_2020_10_04.xlsx').write('CONTENT')
    tmpdir.join('letterofresignation_2020_10_31.xlsx').write('CONTENT')

    #Writing subdirectories organized by financial years
    subdir_fys = tmpdir.mkdir('FY_subdir')
    subdirs_fys_a = subdir_fys.mkdir('FY20')
    subdirs_fys_a.join('LameTextFile20200831.csv').write('CONTENT')
    subdirs_fys_a.join('LameTextFile20200801.csv').write('CONTENT')
    subdir_fys.mkdir('FY21').join('LameTextFile20200801.csv').write('CONTENT')
    subdir_fys.mkdir('FY22').join('LameTextFile20200801.csv').write('CONTENT')
    subdir_fys.mkdir('F25').join('LameTextFile20200801.csv').write('CONTENT')

    #Writing subdirectories organized by date
    subdir_fys = tmpdir.mkdir('datemonth_subdir')
    subdirs_fys_a = subdir_fys.mkdir('Aug 21')
    subdirs_fys_a.join('LameTextFile20200831.csv').write('CONTENT')
    subdirs_fys_a.join('LameTextFile20200801.csv').write('CONTENT')
    subdir_fys.mkdir('Sep 21').join('LameTextFile20200801.csv').write('CONTENT')
    subdir_fys.mkdir('Jan22').join('LameTextFile20200801.csv').write('CONTENT')
    subdir_fys.mkdir('Feb22').join('LameTextFile20200801.csv').write('CONTENT')
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