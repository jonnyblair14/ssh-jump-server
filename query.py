from pathlib import Path

configPath = "% s/.ssh/config" % Path.home()
configFile = open(configPath, "a")
configFile.close()
