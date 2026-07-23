#!/usr/bin/env python3

from pathlib import Path
import os

ROOT_DIR = "."  # 要掃描的目錄

for root, dirs, files in os.walk(ROOT_DIR):
    for filename in files:
        old_path = Path(root) / filename

        stem = old_path.stem      # 不含副檔名
        suffix = old_path.suffix  # .txt .rpm .ipk ...

        if len(filename) > 50:
            new_name = stem[-25:] + suffix
            new_path = old_path.with_name(new_name)

            # 避免檔名衝突
            counter = 1
            while new_path.exists():
                new_name = f"{stem[-50:]}_{counter}{suffix}"
                new_path = old_path.with_name(new_name)
                counter += 1

            print(f"Rename:")
            print(f"  OLD: {old_path}")
            print(f"  NEW: {new_path}")

            #old_path.rename(new_path)

print("Done.")
