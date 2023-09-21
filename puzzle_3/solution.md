# Solution to "Be-head-ed"

This problem required a more involved solution.

In this problem, you are given a file `ancientfile.png` which does not open in standard Image processing software. It is your job to make it open, i.e. *restore* the file.

To do this, it is important to understand how files work. Files always start with a **HEADER** which contains information about what kind of file it is, and sometimes about what kind of content the file contains. In the file we have given to you, the header is absent. This is visible if you open the file in a **Hex Editor**.

The trick to restore this file is adding it's ***header***. To do this, you must write a small Python script that adds a PNG Header to the given file.

This can be found via a google search, which should land you at the official specification [location](http://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html). You will find that the signature is of the form `137 80 78 71 13 10 26 10`. This can be written in hexadecimal as `0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A`.

A Python program to add this "header" to the PNG file is given in the file `solution.py`.

FLAG: **`guillotine`**
