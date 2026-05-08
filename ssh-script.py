import os
from pathlib import Path

home = Path.home()

print("Currently connected to {0}".format(os.uname()[1]))

while True:
    print("Select a host to connect to")

    listfile = "{0}/.ssh/config".format(home)
    hosts = []

    with open(listfile, "rt") as file:
        lines = file.readlines()

    index = 1

    for line in lines:
        if(line.startswith("Host ")):
            host = line.split(' ')[1].strip()
            hosts.append(host)
            print("    {0}. {1}".format(index, host))
            index += 1

    selection = input("Enter a selection digit (blank to exit): ")

    if(selection==""):
        raise SystemExit(0)

    os.system("ssh {0}".format(hosts[int(selection)-1]))
