import os
import time
import pytest

from src.main import search


class TestSearch():
    """This class tests the basic functionality of the trufflepig.search function."""

    def test_base_walk(self, testing_directory):
        """Test that the base case for trufflepig.search returns all files in the directory tree.

        This is equivalent to the results of os.walk (converted to filepaths).
        """
        s = [f.__str__() for f in search(testing_directory)]
        w = list()
        for path, _, files in os.walk(testing_directory):
            for f in files:
                w.append(os.path.join(path, f))
        assert sorted(s) == sorted(w)

    def test_search_for_ext(self, testing_directory):
        """Test that search by suffix works as expected."""
        assert [f.name for f in search(testing_directory, ext='.txt')] == ['trufflecount.txt', 'README.txt']
        assert [f.name for f in search(testing_directory, ext='.png')] == ['trufflepic.png']

    def test_search_for_pattern(self, testing_directory):
        """Test that searching by regex works as expected.

        Note that this also tests that regex can be equivalent to searching by suffix.
        """
        assert [f.name for f in search(testing_directory, regex='^truffle')] == ['trufflecount.txt', 'trufflepic.png']
        assert [f.name for f in search(testing_directory, regex='.+[txt]$')] == [f.name for f in search(testing_directory, ext='.txt')]

    def test_search_for_both(self, testing_directory):
        """Test that specifying a suffix and pattern together works as expected."""
        assert [f.name for f in search(testing_directory, regex='^truffle', ext='.txt')] == ['trufflecount.txt']

    def test_search_subdir(self, testing_directory):
        """Test that searching a subdirectory works as expected."""
        assert [f.name for f in search(os.path.join(testing_directory, 'truffles'), ext='.txt')] == ['trufflecount.txt']

    @pytest.mark.parametrize('sort', ['mtime', 'ctime', 'atime', 'name', 'ext', 'size'])
    def test_sort_mtime(self, testing_directory, sort):
        time.sleep(0.1)
        testing_directory.join('znewfile.z').write('there are many truffles here')
        assert search(testing_directory, sort=sort)[0].name == 'znewfile.z'
        assert search(testing_directory, sort=sort, descending=False)[-1].name == 'znewfile.z'
