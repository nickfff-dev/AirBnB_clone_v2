#!/usr/bin/python3
"""
Fabric script that cleans up old versions of the web_static folder
"""
from fabric.api import *
import os

env.hosts = ['52.3.245.73', '18.204.20.55']


def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = 1 if int(number) == 0 else int(number)

    # Delete all unnecessary archives in the versions folder
    archives = sorted(os.listdir("versions"))
    [archives.pop() for _ in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    # Delete all unnecessary archives in the
    # /data/web_static/releases folder of both of your web servers
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for _ in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
