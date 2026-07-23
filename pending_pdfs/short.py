#!/usr/bin/env python3

from pathlib import Path

MAX_LEN = 35

for p in Path(".").glob("*.pdf"):

    if len(p.name) <= MAX_LEN:
        continue

    if "_" not in p.name:
        continue

    prefix = p.stem.split("_")[0]
    new_name = prefix + p.suffix

    new_path = p.with_name(new_name)

    print(f"{p.name}")
    print(f" -> {new_name}")

    p.rename(new_path)

print("Done")

