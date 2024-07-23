# AVR signature reader

The aim of this project is to static analyze an old AVR RS-232 programmer (called serialdoodad) written in C, understand how it works and  rewrite the function that reads the AVR signature in python

> [!NOTE]
> I am not the author of the C code
> The code was originally shared on [google sites](https://sites.google.com/site/sites/system/errors/WebspaceNotFound?path=%2Fdannychouinard%2FHome%2Fatmel-avr-stuff%2Fsd) but it appears that the site was taken down, so i will be sharing the code on this repo but the credits of the c code belongs to its original author Danny Chouinard

# Project Structure

- `_HTML`: index.html webpage containing steps I used in the explanation video below, worth checking 
- `callgraph.pdf`: functions call graph
- `sd.c`: serialdoodad c
- `serialcomm.py`: serialdoodad read signature in python
- `sig_table.py`: contains avr signatures and the corresponding avr
- `test123.py`: temp file to compare python with c system calls

# Explanation video

> Note: The video is in Arabic


# Video Demo

https://drive.google.com/file/d/15MgOZkJVs744xWA8A3-6U_RqFwg-9kVm/view
