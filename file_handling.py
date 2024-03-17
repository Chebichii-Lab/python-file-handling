# File handling assignment

# Constants
FILE_NAME = "my_file.txt"

# Create a new text file in write mode ('w')
try:
    with open(FILE_NAME, 'w') as file:
        file.write("This is the first line.\n")
        file.write("This is the second line with a number: 42.\n")
        file.write("This is the third line with a string and a number: Hello, 3.\n")
except FileNotFoundError:
    print(f"File {FILE_NAME} not found.")
except PermissionError:
    print(f"Permission denied for file {FILE_NAME}.")
finally:
    print("File creation completed.")

