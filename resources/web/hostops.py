from pathlib import Path

import query


def newhost(hostname, name=None, user=None, port=22, idFile=None):
    temp_dict = {}
    if name is not None:
        current_host = name
    else:
        current_host = hostname
    temp_dict.update({current_host: {}})
    temp_dict[current_host].update({"hostname": hostname})
    if user is not None:
        temp_dict[current_host].update({"user": user})
    if port is not None:
        temp_dict[current_host].update({"port": port})
    if idFile is not None:
        temp_dict[current_host].update({"identity_file": idFile})

    query.dict_to_config(temp_dict, "a")


def remove_host(friendly_name):
    temp_dict = query.config_to_dict()
    temp_dict.pop(friendly_name)
    query.dict_to_config(temp_dict, "o")


def return_hosts_dict():
    return query.config_to_dict()
