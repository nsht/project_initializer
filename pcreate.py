#!/usr/bin/env python

import os
import sys
import subprocess
import time

import colorama


CHECK = f"{colorama.Fore.GREEN}✔{colorama.Style.RESET_ALL}"
CROSS = f"{colorama.Fore.RED}✘{colorama.Style.RESET_ALL}"
ERASE_LINE = '\033[2K'

dir_name = sys.argv[1]
if not dir_name:
    dir_name = input("Enter directory name ")
path = f"{os.getcwd()}/{dir_name}"
print(f"Creating directory {dir_name}",end="\r",flush=True)
try:
    os.mkdir(path)
except Exception as e:
    print(f"{CROSS} error creating directory")
    print("Check if directory already exists")
    print("Exiting")
    sys.exit(1)

time.sleep(1)

print(ERASE_LINE, end="\r", flush=True)
print(f"{CHECK} {dir_name} created")

print("Initializing git",end="\r",flush=True)
time.sleep(1)
try:
    result = subprocess.run(["git", "init"],cwd=path,check=True,capture_output=True)
except Exception as e:
    print(f"{CROSS} error initializing git. Exiting...")
    print(result.stderr)
    sys.exit(1)

# print(result.stdout)
print(f"{CHECK} Initialized git")

try:
    print(f"Opening vscode",end="\r",flush=True)
    result = subprocess.run(["code", "."],cwd=path,check=True,capture_output=True)
except Exception as e:
    print(f"{CROSS} error opening vscode. Exiting...")
    print(result.stderr)
    sys.exit(1)



