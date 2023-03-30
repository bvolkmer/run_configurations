from setuptools import setup

VERSION = "0.1"

setup(
    name="run_configurations",
    version=VERSION,
    author="Benedikt Volkmer",
    description=(
        "A small script that allows quickly executing run configurations from "
        "the command line including shell completions "
    ),
    license="MIT",
    long_description=open("README.md").read(),
    url="https://github.com/bvolkmer/run_configurations",
    py_modules=["run_configurations"],
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "rc = run_configurations:cli",
        ]
    },
)
