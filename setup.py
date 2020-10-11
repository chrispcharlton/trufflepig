import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trufflepig",
    version="0.0.1",
    author="Chris Charlton",
    author_email="chrispcharlton@gmail.com",
    description="A python package for rooting around your filesystem",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chrispcharlton/trufflepig",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
