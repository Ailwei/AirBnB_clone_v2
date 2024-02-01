#!/usr/bin/python3
"""
Fbaric script to generate a .tg archieve from fromthe contents of web_satic
folder of your AirbNb CLONE REPO, USING THE FUNCTION DO_PACK
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    create a .tg achive from contents of the web_static
    The archieve is stored in the versions folder with a timestamp
    returns the archieve path if successfuk or else return None
    """
    try:
        # Create the versions directory if it does not exists
        local("mkdir -p versions")

        # Generate timestamp for the archiebve
        timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')

        # Create the archieve
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvf {} web_static".format(archive_path))

        print("web_static packed: {} -> {}Bytes".format(
                    archive_path,
                    local("wc -c < {}".format(archive_path), capture=True)))
        return archive_path
    except Exception as e:
        return None
