## Experiment 2: full reset

This experiment tries to capture what the game does on a clean save-less run.

### Steps

1. Make sure Steam cloud backup is turned off for TGAA: Chronicles
2. Delete all save files and `gear_sys.dat` from the save-file directory
3. Run the game
4. You should see the game show a message box saying "System Save Data saved"
5. Get into the main menu and exit
6. `gear_sys.dat` appears in the save directory
7. Repeat the same experiment from step 1 one more time
8. Compare the two `gear_sys.dat`
9. Run `patterncheck.py` 

```bash
cmp -l gear_sys_attempt1.dat gear_sys_attempt2.dat | gawk '{printf "%08X: %02X -> %02X\n", $1, strtonum(0$2), strtonum(0$3)}'
```

### Results

1. Both `gear_sys.dat` still have the same 8-byte header: `a1 df d3 19 da d3 47 3a`
2. `gear_sys.dat` is related to "System Save Data"
3. The two `gear_sys.dat` files differ
4. Starting from `0x0068` the `gear_sys.dat` files seem to be filled with a repeating
   8-byte pattern: `ea e9 27 6a 2c b9 e0 86`. We will assume that `gear_sys.dat`
   works with 8-byte **chunks**
5. The only place where both files have some data after `0x0068` is `0x3FB0`
6. It seems that **all** bytes up until `0x0068` may be the header
7. The chunk at `0x3FB0` can't be about anything game-related, because we exitted
   immediately. This and the different data in the "headers" must be something generated
   from the time-stamp.

```
Difference of the two files in hex (all offsets are off by 1)

CHUNK 1:
00000009: 11 -> 55
0000000A: 3C -> 13
0000000B: 2F -> 82
0000000C: BC -> 85
0000000D: 93 -> 12
0000000E: E1 -> EB
0000000F: 5B -> 1C
00000010: 80 -> 0D
00000011: 24 -> BD
00000012: 98 -> 8D
00000013: AC -> 9A
00000014: F3 -> 19
00000015: 93 -> 3C
00000016: 50 -> 60
00000017: 00 -> 59
00000018: 65 -> AF
00000019: C7 -> 2A
0000001A: 6D -> 68
0000001B: BB -> 60
0000001C: 35 -> 42
0000001D: 9C -> E6
0000001E: 2F -> 30
0000001F: 19 -> F2
00000020: DB -> DE

CHUNK 2:
00003FB1: 30 -> 24
00003FB2: C9 -> A2
00003FB3: CD -> 58
00003FB4: B1 -> 30
00003FB6: 45 -> 2A
00003FB7: 15 -> 07
00003FB8: 06 -> A9
```
