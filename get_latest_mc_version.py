import minecraft_launcher_lib
import sys

print(minecraft_launcher_lib.utils.get_latest_version()[sys.argv[1]], end="")