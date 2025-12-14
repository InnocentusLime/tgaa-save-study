## Experiment 3: options

This experiment tries to capture how the game saves settings.

### Steps

1. Make sure Steam cloud backup is turned off for TGAA: Chronicles
2. Delete all save files and `gear_sys.dat` from the save-file directory
3. Copy `gear_sys_attempt1.dat` into the save-file directory and rename it
   into `gear_sys.dat`
4. Run the game
5. Capture the new `gear_sys.dat`
6. Open settings, turn off music and exit
7. Capture the new `gear_sys.dat`
8. Reopen the game
9. Turn the music back on
10. Capture the new `gear_sys.dat`
11. Repeat the same experiment for `gear_sys_attempt2.dat`
12. Run `patterncheck.py`
13. Run `extract.py`
14. Run `optcheck.py`

### Results

1. `gear_sys.dat` keeps updating the time-stamp based parts (`0x08` and `0x03FB0`)
2. Changing settings filled up various other chunks
3. Changing music affected chunk `2007` (at `0x3F20`). Music being on corresponds to
   value to `99 6c 8f 37 03 c8 08 99`. Turning the music back on sets the chunk back
   to the filler value `ea e9 27 6a 2c b9 e0 86`.
4. Chunk changes were the same for both `gear_sys` files. From now on we assume each
   save file does not have unique encryption and each file is just using some odd format
