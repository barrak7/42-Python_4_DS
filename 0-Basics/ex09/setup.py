from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='simple_package',
    version='0.0.1',
    description="A simple package which only has one function that prints a useless message",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/barrak7/42-Python_4_DS/tree/main/0-Basics/ex09",
    author='hbarrak',
    author_email='hbarrak@student.1337.ma',
    license='MIT',
    classifiers=[
                "License :: OSI Approved :: MIT License",
                "Programming Language :: Python :: 3.9",
                "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
