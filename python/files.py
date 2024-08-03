file = open('filename', 'mode')

# 'r': Read (default mode). Opens a file for reading.
# 'w': Write. Opens a file for writing (creates a new file or truncates an existing file).
# 'a': Append. Opens a file for appending (creates a new file if it does not exist).


# Opening and Reading from a File

# Open a file for reading
with open('example.txt', 'r') as file:
    # Read the entire file
    content = file.read()
    print("File Content (Read):")
    print(content)
    
    # Read a single line
    file.seek(0)  # Move the cursor to the beginning of the file
    line = file.readline()
    print("\nFirst Line (Readline):")
    print(line)
    
    # Read all lines into a list
    file.seek(0)  # Move the cursor to the beginning of the file
    lines = file.readlines()
    print("\nAll Lines (Readlines):")
    print(lines)

# Writing to a File

# Open a file for writing (creates a new file or truncates an existing file)
with open('example.txt', 'w') as file:
    # Write a string to the file
    file.write('Hello, world!\n')
    # Write multiple lines to the file
    file.writelines(['Line 1\n', 'Line 2\n'])

# Verify the content by reading it again
with open('example.txt', 'r') as file:
    print("\nFile Content After Writing:")
    print(file.read())

# Appending to a File

# Open a file for appending
with open('example.txt', 'a') as file:
    # Append a string to the file
    file.write('Appending a new line.\n')

# Verify the content by reading it again
with open('example.txt', 'r') as file:
    print("\nFile Content After Appending:")
    print(file.read())

# Demonstrate file closing (not explicitly needed with 'with' statement)

# Open a file for writing
file = open('example.txt', 'w')
file.write('This will overwrite previous content.\n')
file.close()  # Explicitly close the file

# Verify the content by reading it again
with open('example.txt', 'r') as file:
    print("\nFile Content After Explicit Close and Overwrite:")
    print(file.read())
