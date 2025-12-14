## Experiment 1: header scan

This experiment tries to establish if the save files have a header.
The save-files used are from `samples-snapshot`.

### Steps

1. Run scan.py from the repository root (Python3 required)

### Results

1. All save-files seem to share the same 8 bytes
2. `gear_sys.dat` has the same 8 byte header
3. The header barely contains any valid ASCII-characters (only last 2 are ASCII)

```
a1 df d3 19 da d3 47 3a
```
