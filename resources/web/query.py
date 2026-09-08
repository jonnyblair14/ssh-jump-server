from pathlib import Path


def get_value_from_line(line):
    if line.startswith("Host "):
        return ("friendly_name", line.split(" ")[1].strip())
    if line.startswith("\tHostName "):
        return ("hostname", line.split(" ")[1].strip())
    if line.startswith("\tUser "):
        return ("user", line.split(" ")[1].strip())
    if line.startswith("\tPort "):
        return ("port", line.split(" ")[1].strip())
    if line.startswith("\tIdentityFile "):
        return ("identity_file", line.split(" ")[1].strip())
    return (None, None)


def config_to_dict():
    configPath = "./test.txt"
    # configPath = "{0}/.ssh/config".format(Path.home())
    temp_dict = {}
    current_host = ""
    with open(configPath, "rt") as configFile:
        lines = configFile.readlines()

        for line in lines:
            key, value = get_value_from_line(line)

            if key == None:
                continue
            if key == "friendly_name":
                current_host = value
                temp_dict.update({value: {}})
            if key == "hostname":
                temp_dict[current_host].update({key: value})
            if key == "user":
                temp_dict[current_host].update({key: value})
            if key == "port":
                temp_dict[current_host].update({key: value})
            if key == "identity_file":
                temp_dict[current_host].update({key: value})

    configFile.close()
    return temp_dict


def dict_to_config(temp_dict, mode="a"):
    output = ""
    configPath = "./test.txt"
    match mode:
        case "a":
            config_file = open(configPath, "a")
        case "o":
            config_file = open(configPath, "w")

    for key in temp_dict:
        output += "\nHost {0}".format(key)
        for subKey in temp_dict[key]:
            if subKey == "hostame":
                output += "\n\tHostName {0}".format(temp_dict[key][subKey])
            if subKey == "user":
                output += "\n\tUser {0}".format(temp_dict[key][subKey])
            if subKey == "port":
                output += "\n\tPort {0}".format(temp_dict[key][subKey])
            if subKey == "identity_file":
                output += "\n\tIdentityFile {0}".format(temp_dict[key][subKey])
        output += "\n"

    config_file.write(output)
    config_file.close()
