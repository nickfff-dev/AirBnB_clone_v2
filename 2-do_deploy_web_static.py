#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import *
from os.path import exists

env.hosts = ['52.3.245.73', '18.204.20.55']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ Distributes an archive to your web servers,
    using the function do_deploy.
    """
    if not exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        file_name = archive_path.split('/')[-1]
        no_ext = file_name.split('.')[0]
        path = '/data/web_static/releases/'
        run('sudo mkdir -p {}{}/'.format(path, no_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('sudo rm -rf {}{}/web_static'.format(path, no_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
