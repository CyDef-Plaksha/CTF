# Written by Arbaaz Shafiq, Pranjal Rastogi

# A different way to write the header mentioned in the file
PNG_HEADER: bytes = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])

def reHead(filename: str, output: str) -> None:
    """Adds the header in the beginning of the file"""

    # Read the file in BINARY format
    with open(filename, "rb") as f:
        data = f.read()

    # Check if the file is already reheaded
    if data[:8] == PNG_HEADER:
        print("Error: Input file is not Beheaded")
    else:
        # Write the file in BINARY format, adding the PNG_HEADER in the front
        with open(output, "wb") as f:
            f.write(PNG_HEADER + data) # Concatenation of bytes
            print("File has been Reheaded")


def main():
    input_file_name = input("Enter the name of the file to be reheaded: ")
    output_file_name = input("Enter the name of the output file: ")
    reHead(input_file_name, output_file_name)


if __name__ == "__main__":
    main()
