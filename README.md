# ssh-jump-server
Dynamically populated menu for ssh connections.

`ssh-script.sh` dynamically creates a list of ssh endpoints for connection based on the contents of `server-list.txt`.

Populate `server-list.txt` with one host per line.

## Assumptions
This project assumes that your `~/.ssh/config` file contains the following information at a minimum:

```sshconfig
Host <serverName>
    HostName <endpoint hostname>
    User <remoteUser>
```

Where:
- `<serverName>` matches the relevant line in `server-list.txt`
- `<endpoint hostname>` is the ip or url for the endpoint you are connecting to
- `<remoteUser>` is the username of the remote user (can be omitted if the username on the local and remote machines are the same)


`keysetup.sh` can be used to generate ssh keys for the hosts in the `server-lists.txt` file. Remember to copy these across to the endpoints and add them into the ssh config file, `~/.ssh/config`, as below:

```sshconfig
Host <serverName>
    HostName <endpoint hostname>
    User <remoteUser>
    IdentityFile ~/.ssh/<relevant key name>
```
