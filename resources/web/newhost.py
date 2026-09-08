import argparse
from pathlib import Path


def appFN(config_file, friendly_name):
    config_file.write("\nHost {0}".format(friendly_name))


def appHN(config_file, hostname):
    config_file.write("\n\tHostName {0}".format(hostname))


def appUSR(config_file, user):
    config_file.write("\n\tUser {0}".format(user))


def appPort(config_file, port):
    config_file.write("\n\tPort {0}".format(port))


def appIF(config_file, identity_file):
    config_file.write("\n\tIdentityFile {0}".format(identity_file))


def newhost(hostname, name=None, user=None, port=22, idFile=None):
    # configPath = "./test.txt"  # for test purposes
    configPath = "{0}/.ssh/config".format(Path.home())
    with open(configPath, "a") as config_file:
        if name is None:
            appFN(config_file, hostname)
        else:
            appFN(config_file, name)

        appHN(config_file, hostname)

        if user is not None:
            appUSR(config_file, user)

        if port is not None:
            appPort(config_file, port)

        if idFile is not None:
            appIF(config_file, idFile)
        config_file.write("\n")
