import requests
import pathlib
import sys
import json

data = requests.get("https://raw.githubusercontent.com/w1n4a/gl-py/refs/heads/main/data.json").json()

def main():
    try:
        p = pathlib.Path(sys.argv[1])
        if p.exists and p.is_dir:
            print(f"Choose:")
            for (i, v) in enumerate(data):
                print(f"   {i+1}. {data[v]["name"]}")
            inp = int(input(">> "))
            if inp <= len(data) and inp > 0:
                with open(file=f"{p}/LICENSE", mode="w", encoding="utf-8") as f:
                    f.write(requests.get(url=data[inp]["url"]).text())
                    print(f"License added! Path: {f.name}")
    except:
        return

main()
