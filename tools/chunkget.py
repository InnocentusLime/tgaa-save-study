#!/usr/bin/env python3
# General-purpose tool for getting a chunk from gear_sys.dat

import sys
import typing

default = bytes.fromhex("eae9276a2cb9e086")

def getchunk(file: typing.BinaryIO, chunkN: int) -> bytes:
    chunksize=8
    chunksOff=0x68
    file.seek(chunkN*chunksize+chunksOff)
    return file.read(chunksize)

gearsys=sys.argv[1]

veroff=0x08
headersize=24
with open(gearsys, "rb") as file:
    file.seek(veroff)
    data=file.read(headersize)
    print(f"version header and chunk: {data.hex()} {getchunk(file,2025).hex()}")
    if len(sys.argv) > 2:
        chunkN=int(sys.argv[2])
        chunk=getchunk(file, chunkN)
        print(f"data: {chunk.hex()} isdef:{chunk==default}")
