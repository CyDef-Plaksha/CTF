# Solution to "soundbytes.txt"

To solve this question, one needs to understand that a "dump" of a file in binary or hexadecimal can be read and saved as a binary file to be used as it was intended.

The file given, `manysounds.txt` is a hexadecimal dump of a `.wav` file. It is up to you to figure out how it is a dump of a `.wav` file. To figure this out, a trick is to "look" for the Header of a particular file type. Many hints point you towards this file being a "sound" file, and hit-and-trial can be applied from that point onwards. Further, gaining on our knowledge from Puzzle 3, the header of a `.wav` file has the word "RIFF" in it, which is easy to find.

The code then just reads this file and saves it in the correct format. The code to do so is given in `solution.py`.

FLAG: Any variation of **`Rick Roll`** or **`Never Give You Up`**

P.S. Yes, we just rick rolled you.
