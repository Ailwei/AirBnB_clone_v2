#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives
"""

from fabric.api import env, run, local
from fabric.operations import put, sudo
from datetime import datetime
import os

env.hosts = ['100.26.9.108', '34.207.57.168']
env.user = 'ubuntu'
env.key_filename = ['~/.ssh/id_rsa']  # replace with your private key path


def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    number = int(number)
    if number < 0:
        number = 0

    # Get a list of all archives in the versions folder
    archives_versions = sorted(os.listdir('versions'))

    # Delete archives in versions folder
    for archive in archives_versions[:-number]:
        local('rm -f versions/{}'.format(archive))

    # Get a list of all archives in /data/web_static/releases on remote server
    releases_path = '/data/web_static/releases'
    archives_releases_web_01 = run('ls -1t {}/'.format(releases_path)).split()
    archives_releases_web_02 = run('ls -1t {}/'.format(releases_path)).split()

    # Delete archives in /data/web_static/releases on both web servers
    for archive in archives_releases_web_01[:-number]:
        run('rm -f {}/{}'.format(releases_path, archive))
    for archive in archives_releases_web_02[:-number]:
        run('rm -f {}/{}'.format(releases_path, archive))
