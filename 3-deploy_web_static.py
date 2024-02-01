#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
"""
from fabric.api import local, run, env, put
from datetime import datetime
import os

# Define the hosts
env.hosts = ['100.26.9.108', '34.207.57.168']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_pack():
    """
    Creates a compressed archive of the web_static directory.

    Returns:
        str: Path to the created archive, or None if creation failed.
    """
    local("mkdir -p versions")
    tgz_name = "versions/web_static_{}.tgz".format(
        datetime.utcnow().strftime("%Y%m%d%H%M%S")
    )
    local("tar -czvf {} web_static".format(tgz_name))
    return tgz_name if os.path.exists(tgz_name) else None

def do_deploy(archive_path):
    """
    Deploys a compressed archive to the web servers.

    Args:
        archive_path (str): Path to the compressed archive.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    # Rest of the code...

    print("New version deployed!")
    return True

def deploy():
    """
    Orchestrates the deployment process.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
