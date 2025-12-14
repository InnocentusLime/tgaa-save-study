#!/usr/bin/env python3
# Reads interesting data from both `gear_sys` files
# and displays it.
# Run from ex3-options directory.

files = [
    "gear_sys_attempt1.dat",
    "gear_sys_attempt1_musoff.dat",
    "gear_sys_attempt1_muson.dat",
    "gear_sys_attempt2.dat",
    "gear_sys_attempt2_musoff.dat",
    "gear_sys_attempt2_muson.dat",
]

musoffdata={
    0x0068: bytes.fromhex("348bd0c3c6072d33"),
    0x3E90: bytes.fromhex("996c8f3703c80899"),
    0x3F20: bytes.fromhex("996c8f3703c80899"),
    0x3F38: bytes.fromhex("8336003488768d67"),
    0x3F50: bytes.fromhex("98b6b0e644b2aa7f"),
    0x3F58: bytes.fromhex("893a8395c58ee41d"),
    0x3F60: bytes.fromhex("8f59f70f16f1269e"),
    0x3F68: bytes.fromhex("d2ca5c869afb55d4"),
}
default = bytes.fromhex("eae9276a2cb9e086")

for filename in files:
    with open(filename, "rb") as file:
        for optoff, sample in musoffdata.items():
            file.seek(optoff)
            chunkN=(optoff-0x68)//8
            data=file.read(8)
            print(f"{filename:30}:{chunkN:04d}[{optoff:04X}]: {data.hex()} {sample==data} {default==data}")
