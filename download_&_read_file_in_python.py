# Download Data
# Reading Text Files
# A Better Way to Open a File

# Download Data ///////////////////////////////////////////

from pyodide.http import pyfetch # type: ignore

import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

async def download(url, filename):

    response = await pyfetch(url)

    if response.status == 200:

        with open(filename, "wb") as f:

            f.write(await response.bytes())

    await download(filename, "example1.txt")

print("done")


# Reading Text Files ///////////////////////////////////////////

# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")

# Print the path of file

file1.name 

# Print the mode of file, either 'r' or 'w'

file1.mode 

# Read the file

FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line

print(FileContent)

# Type of file content

type(FileContent)

# Close file after finish

file1.close()

# A Better Way to Open a File ///////////////////////////////////////////

# Open file using with

with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed

file1.closed

# See the content of file

print(FileContent)

# Read first four characters

with open(example1, "r") as file1:
    print(file1.read(4))

# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())

with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# Iterate through the lines

with open(example1,"r") as file1:
        i = 0
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1

# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()
    FileasList[0]
    FileasList[1]
    FileasList[2]