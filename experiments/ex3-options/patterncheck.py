#!/usr/bin/env python3
# Checks the byte-pattern in the save files.
# Run from ex3-options directory.

files = [
    "gear_sys_attempt1_musoff.dat",
    "gear_sys_attempt2_musoff.dat",
]

verbose = False
patternoff = 0x68
pattern = bytes.fromhex("eae9276a2cb9e086")

for filename in files:
    with open(filename, "rb") as file:
        file.seek(patternoff)
        offsetn = 0
        while (data := file.read(len(pattern))):
            off = patternoff + offsetn*len(pattern)
            if verbose or data != pattern:
                print(f"{filename}: {off:04X} {data.hex()} {data==pattern}")
            offsetn += 1
