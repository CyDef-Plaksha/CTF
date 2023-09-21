# Written by Pranjal Rastogi

if __name__ == "__main__":

    file_name = "manysounds.txt"
    output_name = "output.wav"

    # Read the input file in TEXT format
    with open(file_name, "r") as fb:
        # Write the output file in BINARY format
        with open(output_name, "wb") as f:
            # Create bytes from hexadecimal representation in the input file
            towrite = bytes.fromhex(fb.read())
            # Write the bytes to the output file
            f.write(towrite)

