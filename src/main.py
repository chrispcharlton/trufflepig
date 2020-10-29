import os
import pathlib
import re

def walk_files(target, topdown=False):
    """Returns Path objects of all files in a directory and it's subdirectories."""
    for root, _, files in os.walk(target, topdown=topdown):
       for name in files:
            yield pathlib.Path(os.path.sep.join([root, name]))

def sort_paths(paths, sort, descending):
    """Sort a list of file paths by a range of criteria.

    Each invocation of this function allows for an iterable of paths to be sorted by a single criteria, specified by
    a string.

    Note: for Unix users there is currently no way to sort by file creation time, ctime only gives creation time in
    Windows.

    :param paths: a list of pathlib.Path objects.
    :param sort: string denoting the sort key. Can be one of 'ctime', 'mtime', 'atime', 'name', 'ext' or 'size'.
    :param descending: if True, sort in descending order, otherwise sort in ascending order.
    :return: A list of pathlib.Path objects
    """
    if sort == 'ctime':
        paths = sorted(paths, key=lambda f: f.stat().st_ctime_ns, reverse=descending)
    if sort == 'mtime':
        paths = sorted(paths, key=lambda f: f.stat().st_mtime_ns, reverse=descending)
    if sort == 'atime':
        paths = sorted(paths, key=lambda f: f.stat().st_atime_ns, reverse=descending)
    if sort == 'name':
        paths = sorted(paths, key=lambda f: f.name, reverse=descending)
    if sort == 'ext':
        paths = sorted(paths, key=lambda f: f.suffix, reverse=descending)
    if sort == 'size':
        paths = sorted(paths, key=lambda f: f.stat().st_size, reverse=descending)
    return paths

def search(dir, regex=None, ext=None, sort=None, descending=True):
    """Walk through a directory tree and return a list of files matching a given criteria.

    Criteria can be file type and/or a regular expression to match. If no criteria is passed, then all files in the
    directory are returned.

    :param dir: string or pathlib.Path object specifying the directory to begin the search in. All subdirectories will
        also be searched.
    :param regex: a regular expression to match against.
    :param ext: string specifying a specific file type to return. Should include the period.
    :param sort: string denoting the sort key. Can be one of 'ctime', 'mtime', 'atime', 'name', 'ext' or 'size'.
    :param descending: if True, sort in descending order, otherwise sort in ascending order.
    :return: A list of pathlib.Path objects
    """
    def matches_ext(file, ext):
        if ext is None:
            return True
        else:
            return file.suffix == ext

    def matches_regex(file, regex):
        if regex is None:
            return True
        else:
            return bool(re.match(regex, file.name))

    files = [file for file in walk_files(dir) if matches_ext(file, ext) and matches_regex(file, regex)]
    if sort is not None:
        files = sort_paths(files, sort, descending)

    return files
