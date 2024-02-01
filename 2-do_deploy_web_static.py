#!/usr/bin/python3
"""
Fabric script to distribute an archieve to your sdervers
using tthe function do_deploy
"""

from fabric.api import env, put, run, sudo
from os.path import exists
from datetime import datetime

env.hosts = ['100.26.9.108', '34.207.57.168']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distrubutes an archive to the web servers and deploy code
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web servers
        put(archive_path, "/tmp/")

        # extract the archive to /data/web_static/releases/<archieve file
        archive_filename = archive_path.split('/')[-1]
        archive_folder = archive_filename[:-4]
        releases_path = "/data/web_static/release/"

        run("mkdir -p {}/{}".format(releases_path, archive_folder))
        run("tar xf /tmp/{} -C {}/{}".format(archive_filename,
                                             releases_path, archive_folder))
        # Delete the archive from web the web servers
        run("rm /tmp/{}".format(archive_filename))

        # Move the contents of extracted folder to the main folder
        run(
                "mv {}/{}/web_static/* {}/{}".format(
                    releases_path, archive_folder,
                    releases_path, archive_folder)
                )

        run("rm -rf {}/web_static".format(releases_path, archive_folder))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run(
                "ln -s {}/{}/ /data/web_static/current".format(
                    releases_path, archive_folder)
                )

        print("New version deployed!")
        return True
    except Exception as e:
        return False
