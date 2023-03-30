from setuptools import setup

VERSION = "0.1.1"

setup(
    name="run_configurations",
    version=VERSION,
    author="Benedikt Volkmer",
    description=(
        "A small script that allows quickly executing run configurations from "
        "the command line including shell completions "
    ),
    license="MIT",
    long_description="""\
A small script that allows quickly executing run configurations from the
command line including shell completions.

A run configurations can be any executable placed in a ``.run_configs``
directory in any parent of the current working directory. Configurations
are always executed in the directory containing the ``.run_configs``
folder to get the same behavior independent of the current working
directory.

::

   Usage: rc [OPTIONS] RUN_CONFIG [ARGS]...


     Run a run config

     A run config can be any executable file in the .run_configs directory.

   Options:
     --make-executable     Make run config executable if it isn't already.
     --base-dir DIRECTORY  Base directory to run from. Defaults to the first
                           directory containing a .run_configs directory. Should
                           contain a .run_configs directory with executable run
                           configs.
     --list                List available run configs.
     --zsh-completion      Print zsh completion script.
     --version             Show the version and exit.
     --help                Show this message and exit.
""",
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
