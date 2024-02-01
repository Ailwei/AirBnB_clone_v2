#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.26.9.108', '34.207.57.168']

def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = max(1, int(number))

    with lcd("versions"):
        archives = sorted(os.listdir("."))
        [local("rm {}".format(os.path.join(".", a))) for a in archives[:-number]]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [run("rm -rf {}".format(os.path.join(".", a))) for a in archives[:-number]]
