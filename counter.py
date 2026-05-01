#!/usr/bin/env python3
import sys, json, re
from pathlib import Path

if len(sys.argv) < 2:
    print("specify a path")
    exit(1)

base_path = Path(sys.argv[1]).resolve(strict = True).parent
manifest = json.loads(open(sys.argv[1]).read())

inline = None

if manifest["comments"]:
    if manifest["comments"]["match"]:
        manifest["comments"]["match"] = re.compile(manifest["comments"]["match"])
    if manifest["comments"]["inline"]:
        if not manifest["comments"]["inline"]["start"] or not manifest["comments"]["inline"]["end"]:
            print("inline comments must include both a start and end token")
            exit(1)
        inline = re.compile("{}.*{}".format(re.escape(manifest["comments"]["inline"]["start"]), re.escape(manifest["comments"]["inline"]["end"])))

total = 0

for file in manifest["files"]:
    path = base_path / file
    with open(path) as file:
        contents = file.read()
        if manifest["comments"]:
            if manifest["comments"]["match"]:
                contents = manifest["comments"]["match"].sub("", contents)
            if manifest["comments"]["line"]:
                new_contents = ""
                for line in contents.split("\n"):
                    if not line.strip().startswith(manifest["comments"]["line"]):
                        new_contents += line
                        new_contents += "\n"
                contents = new_contents
            if inline:
                contents = inline.sub("", contents)
        contents = re.compile(r"\s+").sub("", contents)
        total += len(contents)

print(f"Total score is {total}")
