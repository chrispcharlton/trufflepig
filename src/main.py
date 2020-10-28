import os
import pathlib
import re

def walk_files(target, topdown=False):
    """Returns Path objects of all files in a directory and it's subdirectories."""
    for root, _, files in os.walk(target, topdown=topdown):
       for name in files:
            yield pathlib.Path(os.path.sep.join([root, name]))

def search(dir, regex=None, ext=None):
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
    return [file for file in walk_files(dir) if matches_ext(file, ext) and matches_regex(file, regex)]



