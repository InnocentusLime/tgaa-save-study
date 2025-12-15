## Experiment 4: more option messing

### Steps 1

1. Replace `gear_sys.dat` with the one in this folder
2. Run `chunkdump.py` against it. Only the following chunks should be set
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 6fdeadd96982509f False
```
3. Turn off music and capture chunks
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2007 off:3F20 996c8f3703c80899 False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 d6cdb7921f95977d False
```
5. Turn on music and capture chunks
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 f92be42e5a187b05 False
```
7. Turn off effects and capture chunks
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2007 off:3F20 c06a40f93bfe88cc False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 77e25ae802f256b0 False
```
8. Turn on effects and capture chunks
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 5020a509f93c70fd False
```
9. Turn off both effects and music and capture chunks
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2007 off:3F20 8336003488768d67 False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 9bc8b6074c255171 False
```
10. Turn on both effects and music on and capture chunks
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 bfecb7f6f0de223b False
```
10. Turn off voices
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2007 off:3F20 fa80bce495ac683d False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 ed462d0c4ddf247c False
```
11. Turn off also music
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2007 off:3F20 77171bfbeb806c61 False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 c13335ba3fff58e9 False
```
12. Turn music back on, but turn off effects
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2007 off:3F20 7b3949ce4fb22e94 False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 d4ed6d5068147297 False
```
13. Turn off all audio
```
chunkN:0000 off:0068 348bd0c3c6072d33 False
chunkN:1989 off:3E90 996c8f3703c80899 False
chunkN:2007 off:3F20 a41ffe708e0bf27b False
chunkN:2010 off:3F38 8336003488768d67 False
chunkN:2013 off:3F50 98b6b0e644b2aa7f False
chunkN:2014 off:3F58 893a8395c58ee41d False
chunkN:2015 off:3F60 8f59f70f16f1269e False
chunkN:2016 off:3F68 d2ca5c869afb55d4 False
chunkN:2025 off:3FB0 d1ebae169f958378 False
```