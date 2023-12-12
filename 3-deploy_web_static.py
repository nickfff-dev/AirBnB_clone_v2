#!/usr/bin/python3
"""
Fabric script that creates and distributes an
archive to your web servers, using the function deploy.
"""
from fabric.api import local, env, put, run
from datetime import datetime
from os.path import exists

env.hosts = ['52.3.245.73', '18.204.20.55']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """

    # create a versions directory if not exists
    local("mkdir -p versions")

    # create a tgz archive of the web_static directory
    tgz_file = 'versions/web_static_{}.tgz'.format(datetime.now()
                                                   .strftime('%Y%m%d%H%M%S'))
    result = local("tar -cvzf {} web_static".format(tgz_file))

    # return the archive path if the archive has been correctly generated.
    # Otherwise, it should return None
    if result.failed:
        return None
    else:
        return tgz_file


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


def deploy():
    """ Creates and distributes an archive to your web servers,
    using the function deploy.
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
