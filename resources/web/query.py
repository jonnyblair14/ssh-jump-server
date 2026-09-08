import json
from pathlib import Path

# TODO: Swap to dictionary method/create alternative method?


def config_to_json():
    configPath = "{0}/.ssh/config".format(Path.home())
    json_str = ""
    first = True
    with open(configPath, "rt") as configFile:
        lines = configFile.readlines()

        for line in lines:

            if line.startswith("Host "):
                if first != True:
                    json_str += "}\n{\n"
                else:
                    json_str += "{\n"
                    first = False
                json_str += '\t"name": '
            if line.startswith("\tHostName "):
                json_str += '\t"hostname": '
            if line.startswith("\tUser "):
                json_str += '\t"user": '
            if line.startswith("\tPort "):
                json_str += '\t"port": '
            if line.startswith("\tIdentityFile "):
                json_str += '\t"identity_file": '
            json_str += '"{0}"'.format(line.split(" ")[1].strip())
            json_str += "\n"
        json_str += "}\n"

    configFile.close()

    jsonFile = open("query.json", "w")
    jsonFile.write(json_str)
