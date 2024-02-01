#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives
"""

from fabric.api import env, local, run
import os

env.hosts = ['100.26.9.108', '34.207.57.168']
env.user = 'ubuntu'  # Change this to 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.
                      If 0 or 1, keeps only the most recent archive.
                      If 2, keeps the most and second-most recent archives, etc.
    """
    number = max(1, int(number))

    # Delete unnecessary archives in the versions folder
    with lcd("versions"):
        archives = sorted(os.listdir("."))
        [local("rm {}".format(archive)) for archive in archives[:-number]]

    # Delete unnecessary archives in /data/web_static/releases on both servers
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [archive for archive in archives if "web_static_" in archive]
        [run("sudo rm -rf {}".format(archive)) for archive in archives[:-number]]
