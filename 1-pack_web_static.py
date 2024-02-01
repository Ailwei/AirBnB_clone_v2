#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once, settings

@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    date_time = datetime.now()
    out_put = os.path.join("versions", "web_static_{}{}{}{}{}{}.tgz".format(
        date_time.year,
        date_time.month,
        date_time.day,
        date_time.hour,
        date_time.minute,
        date_time.second
    ))
    try:
        print("Packing web_static to {}".format(out_put))
        with settings(warn_only=True):
            local("tar -cvzf {} web_static".format(out_put))
        size = os.stat(out_put).st_size
        print("web_static packed: {} -> {} Bytes".format(out_put, size))
    except Exception as e:
        print("Error: {}".format(e))
        out_put = None
    return out_put
