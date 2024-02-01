#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["100.26.9.108", "34.207.57.168"]
env.user = "ubuntu"


def do_pack():
    """
    Create a compressed archive of the web_static directory.
    Returns the path of the generated archive if successful, or None otherwise.
    """
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_file_path = "versions/web_static_{}.tgz".format(date)
    result = local(
            "tar -cvzf {} web_static".format(archived_file_path), capture=True
            )
    if result.succeeded:
        return archived_file_path
    else:
        return None


def do_deploy(archive_path):
    """
    Deploy the web_static archive to the web servers.
    """
    if not archive_path or not os.path.exists(archive_path):
        print("Error: Archive file does not exist.")
        return False

    try:
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file, newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(
                    newest_version,
                    newest_version
                    ))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed successfully!")
        return True

    except Exception as e:
        print("Error during deployment: {}".format(e))
        return False
