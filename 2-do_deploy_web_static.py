#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,
using the function do_deploy.
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ['52.3.245.73', '18.204.20.55']
env.user = 'ubuntu'
env.path = '~/.ssh/school'


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
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
