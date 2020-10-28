import os
import pathlib


def walk_files(target, topdown=False):
    """Returns Path objects of all files in a directory and it's subdirectories."""
    for root, _, files in os.walk(target, topdown=topdown):
       for name in files:
            yield pathlib.Path(os.path.sep.join([root, name]))