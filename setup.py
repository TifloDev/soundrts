#! .venv\Scripts\python.exe
"""
From the command-line, type: py setup.py build
Or activate the virtual environment and type: python setup.py build

Warning: the py launcher ignores the virtual environment if a "#!" line is specified!
(see PEP 486)
"""

import os
import platform
import shutil
import sys
from subprocess import Popen, check_output

from cx_Freeze import Executable, setup

import builddoc
import buildmultimapslist
import clean
from soundrts.version import VERSION

if platform.system() == "Windows" and ".venv" not in sys.executable:
    print(f"WARNING: {sys.executable} (not a virtual environment?)")
    input("[press Enter to continue; press Control+C to stop]")

try:
    full_version = check_output(["git", "describe", "--tags"]).strip().decode()
except FileNotFoundError:
    print("WARNING: couldn't get version from git.")
    full_version = f"{VERSION}-unknown"
destination = rf"./.build/{VERSION}"
build_exe_options = {
    "build_exe": destination,
    "optimize": 1,
    "silent": True,
    "packages": [],
    "excludes": ["Cython", "scipy", "numpy", "tkinter"],
    "include_files": ["res", "single", "multi", "mods", "cfg", "doc"],
    "replace_paths": [("*", f"{full_version}:")],
}
executables = [
    Executable("soundrts.py", base="Win32GUI"),
    Executable("server.py", base=None),
]

clean.clean()
buildmultimapslist.build()
builddoc.build()
if os.path.exists(destination):
    print(f"{destination} already exists. Deleting...")
    shutil.rmtree(destination)
setup(
    options={"build_exe": build_exe_options},
    executables=executables,
    name="SoundRTS",
    version=VERSION.replace("-dev", ".9999"),
)
print("Creating empty user folder...")
os.mkdir(rf"{destination}\user")
print(r"Resetting cfg\language.txt ...")
open(rf"{destination}\cfg\language.txt", "w").write("")
print("Adding full_version.txt ...")
with open(rf"{destination}\lib\full_version.txt", "w") as t:
    t.write(full_version)
