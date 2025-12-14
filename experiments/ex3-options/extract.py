#!/usr/bin/env python3
# Reads interesting data from both `gear_sys` files
# and displays it.
# Run from ex3-options directory.

files = [
    "gear_sys_attempt1.dat",
    "gear_sys_attempt1_musoff.dat",
    "gear_sys_attempt2.dat",
    "gear_sys_attempt2_musoff.dat",
]

headeroff=0x08
headersize=24
chunkoff=0x3FB0
chunksize=8

for filename in files:
    with open(filename, "rb") as file:
        file.seek(headeroff)
        header = file.read(headersize)

        file.seek(chunkoff)
        chunk = file.read(chunksize)

        print(f"{filename:30}: {header.hex()} {chunk.hex()}")
