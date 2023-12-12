#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['52.3.245.73', '18.204.20.55']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """

    # Return False if the file at the path archive_path doesn’t exist
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        # on the web server
        file_name = archive_path.split("/")[-1]
        no_ext, ext = file_name.split(".")
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, no_ext))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(file_name))

        # Move the files
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(no_ext, no_ext))

        # Delete the symbolic link /data/web_static/current from
        # the web server
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(no_ext))
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link /data/web_static/current
        # on the web server, linked to the new version of your code
        # (/data/web_static/releases/<archive filename without extension>)
        run("ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(no_ext))
        return True
    except Exception:
        return False
