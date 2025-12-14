#!/usr/bin/env python3
# General purpose tool for dumping chunks

import sys

default = bytes.fromhex("eae9276a2cb9e086")
chunksOff=0x68

gearsys=sys.argv[1]

verbose = False
with open(gearsys, "rb") as file:
    file.seek(chunksOff)
    chunkN = 0
    while (data := file.read(len(default))):
        off = chunksOff + chunkN*len(default)
        if verbose or data != default:
            print(f"chunkN:{chunkN:04d} off:{off:04X} {data.hex()} {data==default}")
        chunkN += 1
