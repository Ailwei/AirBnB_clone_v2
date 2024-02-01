#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives.
"""

from fabric.api import env, run, local, put
from datetime import datetime
import os

env.hosts = ['100.26.9.108', '34.207.57.168']


def do_clean(number=0):
    """Deletes out-of-date archives."""
    number = int(number)
    if number < 1:
        number = 1
    number += 1

    # Delete unnecessary archives in the versions folder
    local("ls -1t versions/ | tail -n +{} | xargs -I {{}} rm versions/{{}}".format(number))

    # Delete unnecessary archives in the /data/web_static/releases folder
    run("ls -1t /data/web_static/releases/ | tail -n +{} | xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number))

    print("Cleaned up archives")


def do_deploy(archive_path):
    """Distributes an archive to a web server."""
    if not os.path.exists(archive_path):
        return False

    archive_name = os.path.basename(archive_path)
    archive_folder = "/data/web_static/releases/{}".format(archive_name[:-4])

    # Upload the archive to the server
    put(archive_path, "/tmp/")
    run("sudo mkdir -p {}".format(archive_folder))
    run("sudo tar -xzf /tmp/{} -C {}/".format(archive_name, archive_folder))
    run("sudo rm /tmp/{}".format(archive_name))
    run("sudo mv {}/web_static/* {}".format(archive_folder, archive_folder))
    run("sudo rm -rf {}/web_static".format(archive_folder))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(archive_folder))

    print("New version deployed!")

    return True


def deploy():
    """Creates and distributes an archive to a web server."""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_pack():
    """Generates a .tgz archive."""
    if not os.path.exists("versions"):
        local("mkdir -p versions")

    current_time = datetime.utcnow()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        current_time.year,
        current_time.month,
        current_time.day,
        current_time.hour,
        current_time.minute,
        current_time.second
    )

    try:
        local("tar -cvzf {} web_static".format(archive_path))
        size = os.path.getsize(archive_path)
        print("web_static packed: {} -> {} Bytes".format(archive_path, size))
        return archive_path
    except Exception as e:
        print("Error packing web_static: {}".format(e))
        return None


if __name__ == "__main__":
    do_clean()
    deploy()
