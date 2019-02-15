# -*- coding:utf-8 -*-


"""
This module provides format and functionality to interact with the
tagging system of this git repository in a programmatical way, using gitpython.
"""

import argparse
import git


THIS_REPO = git.Repo(search_parent_directories=True)


def encode_repo_tagname(major_version, minor_version, bugfix):
    """
    Expects three non-negative integers a,b,c like (0, 13,234) and returns a
    string in the form 'v0.13.234'
    """
    assert isinstance(major_version, int),\
        "[add_tag]: inputs must be non-negative ints!"
    assert isinstance(minor_version, int),\
        "[add_tag]: inputs must be non-negative ints!"
    assert isinstance(bugfix, int),\
        "[add_tag]: inputs must be non-negative ints!"
    #
    assert major_version >= 0, "[add_tag]: inputs must be non-negative ints!"
    assert minor_version >= 0, "[add_tag]: inputs must be non-negative ints!"
    assert bugfix >= 0, "[add_tag]: inputs must be non-negative ints!"
    #
    tag_string = "v%d.%d.%d" % (major_version, minor_version, bugfix)
    return tag_string


def decode_repo_tagname(tag_string):
    """
    Expects a string in the form 'v0.13.234' and returns the three
    corresponding integers as a tuple like (0, 13, 234).
    """
    processed_tag = tag_string[1:].split(".")
    major_version = int(processed_tag[0])
    minor_version = int(processed_tag[1])
    bugfix = int(processed_tag[2])
    return (major_version, minor_version, bugfix)


def get_repo_tags(chronologically_sorted=False):
    """
    Returns a collection of pointers to this repo's tags. If the flag
    is true, they will be sorted by the datetime of the commits they point to.
    """
    t = THIS_REPO.tags
    if chronologically_sorted:
        return sorted(t, key=lambda x: x.commit.committed_datetime)
    else:
        return t


def create_repo_tag(major_version, minor_version, bugfix,
                    message=None, ref="HEAD"):
    """
    This function prints current repo's tags and adds a new one to the
    commit signaled by 'ref', with the given message. The version and
    bugfix numbers have to be non-negative integers (see encode_repo_tagname).
    It returns a reference to the added tag object.
    """
    tags = get_repo_tags(True)
    if tags:
        print("This repo has the following tags:")
        for t in tags:
            print(t.name, "--", t.commit.committed_datetime, "--",
                  t.tag.message)
    else:
        print("This repo has no previous tags.")
    new_tagname = encode_repo_tagname(major_version, minor_version, bugfix)
    print("Adding new tag to", ref, "with name:", new_tagname, end="")
    if message is None:
        print()
    else:
        print(" and message:", message)
    #
    new_tagref = THIS_REPO.create_tag(new_tagname, message=message, ref=ref)
    #
    return new_tagref


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--major_version", required=True,
                        type=int,
                        help="int>=0 representing the release's major version")
    parser.add_argument("-b", "--minor_version", required=True,
                        type=int,
                        help="int>=0 representing the release's minor version")
    parser.add_argument("-c", "--bugfix", required=True,
                        type=int,
                        help="int>=0 representing the release's bugfix number")
    parser.add_argument("-m", "--tag_message",
                        type=str, default=None,
                        help="Optional message for the git tag")
    args = parser.parse_args()
    #
    MAJOR_VERSION = args.major_version
    MINOR_VERSION = args.minor_version
    BUGFIX = args.bugfix
    TAG_MESSAGE = args.tag_message
    tag = create_repo_tag(MAJOR_VERSION, MINOR_VERSION, BUGFIX,
                          TAG_MESSAGE, "HEAD")
    #
    with open("README.md", "r") as f:
        long_description = f.read()
