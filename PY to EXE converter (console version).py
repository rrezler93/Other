import os
import PyInstaller.__main__

# Prompt the user to enter the file path of the Python script to convert
py_file = input("Enter the file path of the Python script to convert: ")

# Check if the file path exists
if not os.path.isfile(py_file):
    print("Error: File not found.")
else:
    # Use PyInstaller to convert the Python script to a standalone executable file
    PyInstaller.__main__.run([
        py_file,
        "--onefile",
        "--name={}".format(os.path.splitext(os.path.basename(py_file))[0]),
        "--clean",
        "--distpath={}".format(os.path.dirname(py_file)),

    ])
    print("Conversion complete!")
