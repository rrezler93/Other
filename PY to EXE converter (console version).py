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

# - '--onefile': Specifies that the output should be a single executable file.
# - '--name={}': Sets the name of the output executable to the base name of the input script (without the file extension).
# - '--clean': Instructs PyInstaller to clean up any temporary files and folders after the conversion.
# - '--distpath={}': Specifies the directory where the output executable should be saved.

    ])
    print("Conversion complete!")
