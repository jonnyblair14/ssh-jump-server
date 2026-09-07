import argparse
import os
from pathlib import Path

# configPath = "./testfiles/test.txt" # for test purposes
configPath = "% s/.ssh/config" % Path.home()
configFile = open(configPath, "a")


def appFN(FN):
    global configFile
    configFile.write("\nHost {0}".format(FN))


def appHN(HN):
    global configFile
    configFile.write("\n\tHostName {0}".format(HN))


def appUSR(USR):
    global configFile
    configFile.write("\n\tUser {0}".format(USR))


def appPort(Port):
    global configFile
    configFile.write("\n\tPort {0}".format(Port))


def appIF(If):
    global configFile
    configFile.write("\n\tIdentityFile {0}".format(If))


def main():
    Parser = argparse.ArgumentParser(prog="newhost")
    Parser.add_argument(
        "-f", "--FriendlyName", help="Friendly name that appears in the jumpserver list"
    )
    Parser.add_argument(
        "-H", "--Hostname", help="Hostname of the machine used for the ssh connection"
    )
    Parser.add_argument(
        "-u", "--Username", help="Username to connect with during the ssh connection"
    )
    Parser.add_argument(
        "-p",
        "--Port",
        type=int,
        default=22,
        help="Port Number for ssh connection, assumes default 22",
    )
    Parser.add_argument(
        "-i",
        "--IdentityFile",
        help="Identity file path usually in ~/.ssh/<insert_filename>",
    )

    args = Parser.parse_args()

    if args.Hostname is None:
        print("Missing Hostname. Please provide hostname.")
        exit
    else:
        if args.FriendlyName is None:
            appFN(args.Hostname)
            appHN(args.Hostname)
        else:
            appFN(args.FriendlyName)
            appHN(args.Hostname)

        if args.Username is not None:
            appUSR(args.Username)

        if args.Port is not None:
            appPort(args.Port)

        if args.IdentityFile is not None:
            appIF(args.IdentityFile)
        configFile.write("\n")

    configFile.close()


main()
