import os
import requests
import pathlib
import sys

data = requests.get("https://raw.githubusercontent.com/w1n4a/gl-py/refs/heads/main/data.json").json()
alias = [x for x in data]

def main():
    p = pathlib.Path(os.getcwd()) if len(sys.argv) == 1 else pathlib.Path(sys.argv[1])

    if p.exists and p.is_dir:
        print(f"Choose:")
        for (i, v) in enumerate(alias):
            print(f"   {i+1}. {v}")
        inp = int(input(">> ")) - 1
        if inp < len(alias) and inp > -1:
            with open(file=f"{p}/LICENSE", mode="w", encoding="utf-8") as f:
                f.write(requests.get(url=data[alias[inp]]).text)
                print(f"License added! Path: {f.name}")

main()
