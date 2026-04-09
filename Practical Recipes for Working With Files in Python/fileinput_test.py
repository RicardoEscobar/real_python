"""Example and basic use of the fileinput module"""

import fileinput

def main():
    """Print the contents of a file to the console"""
    files = ['example.txt', 'example2.txt', 'example3.txt']

    # Open the file for reading
    with fileinput.input(files=files) as f:
        # Iterate over each line in the file
        for line in f:
            # Print the line to the console
            print(line)

if __name__ == '__main__':
    main()
