# Author: VintellX
# Date created: 24/01/2024

# Just importing my old project's file for working with MongoDB
# As I'll be hosting this on my own server, I'll be using those files

import os
import sys
patho = sys.path
import importlib

def importo(VinDir):
    patho.insert(0, VinDir) 
    for xDtrash in os.listdir(VinDir):
        if xDtrash.endswith(".py") and not xDtrash.startswith("__"):
            trashModule = xDtrash[:-3]

            try:
                trasho = importlib.import_module(trashModule)
                print(f"+ {trashModule}")
            except Exception as e:
                print(f"- {trashModule}: {e}")
    patho.pop(0)
if __name__ == "__main__":
    xDir = "/home/VintellX/xDrag/Xanthe/pythonDocket/xDmongo/scripts"
    # importo(xDir) # Uncomment this to import
