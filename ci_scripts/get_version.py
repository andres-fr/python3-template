# -*- coding:utf-8 -*-


"""
Get version information from the bumpversion config file
"""

from os.path import join
import sys
from os.path import abspath, dirname


MODULE_ROOT_DIR = dirname(dirname(abspath(__file__)))
# append module root directory to sys.path
if MODULE_ROOT_DIR not in sys.path:
    sys.path.append(MODULE_ROOT_DIR)


__author__ = "Andres FR"


BUMPVERSION_FILENAME = ".bumpversion.cfg"
BUMPVERSION_ABSPATH = join(MODULE_ROOT_DIR, BUMPVERSION_FILENAME)


def get_version_string(filepath):
    """
    This function expects the file in the given path to contain
    a line in the exact form 'current_version = <THE VERSION>'
    (which is currently satisfied by bump2version).
    It returns whatever is after the '=' assignment as a stripped
    string. For multiple matches, it returns the first one.
    """
    with open(filepath, "r") as f:
        for line in f:
            if "current_version" in line:
                return line.split("=")[1].strip()


def decompose_version_string(version_string):
    """
    Given a string in the form 'x.y.z', this function
    returns a tuple of strings (x, y, z)
    """
    x, y, z = version_string.split(".")
    return (x, y, z)


def gvs(decomposed=False):
    """
    An alias for
      get_version_string(REPO_ROOT/BUMPVERSION_FILENAME)
    if decomposed is true, the output is as well passed through
      decompose_version_string
    """
    out = get_version_string(BUMPVERSION_ABSPATH)
    if decomposed:
        out = decompose_version_string(out)
    return out


if __name__ == "__main__":
    print(gvs(False))
