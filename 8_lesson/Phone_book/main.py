from os import path

file_base = "base.txt"

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass