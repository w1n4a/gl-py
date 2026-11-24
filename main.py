import requests
import pathlib
import sys
import json

data = requests.get("https://opensource.org/api/license").json()
print(data)

def main():
    try:
        p = pathlib.Path(path=sys.argv[1])
        if p.exists and p.is_dir:
            pass
    except:
        return

main()
