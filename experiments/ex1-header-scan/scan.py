#!/usr/bin/env python3
# Checks the headers of samples in samples-snapshot.
# Run this script from the repository root.

from pathlib import Path

nametogame = {
    "gear_game00.dat": "TGAA2",
    "gear_game01.dat": "TGAA2",    
    "gear_game02.dat": "TGAA2",    
    "gear_game03.dat": "TGAA2",    
    "gear_game04.dat": "TGAA2",    
    "gear_game05.dat": "TGAA1",    
    "gear_game06.dat": "TGAA1",    
    "gear_game07.dat": "TGAA1",    
    "gear_game20.dat": "TGAA1",    
}

samplesdir = Path('samples-snapshot')
files = list(samplesdir.glob("gear_game*.dat"))

# Finding 1: all save files have the same first 8 bytes
print(f"{'='*10} First 8 bytes")
shared = None
for file in files:
    filename = str(file.name)
    game = nametogame[filename]
    with file.open("rb") as file:
        data = file.read(8)
        if shared is None: shared = data
        print(f"{filename} ({game}): {data.hex()} {shared==data}")

# Finding 2: all next 8 bytes do not match 
print(f"{'='*10} Next 8 bytes")
shared = None
for file in files:
    filename = str(file.name)
    game = nametogame[filename]
    with file.open("rb") as file:
        file.seek(8)
        data = file.read(8)
        if shared is None: shared = data
        print(f"{filename} ({game}): {data.hex()} {shared==data}")
