import minecraft_launcher_lib
import sys

latest_version = minecraft_launcher_lib.utils.get_latest_version()["release"]

minecraft_launcher_lib.install.install_minecraft_version(latest_version, sys.argv[1])
