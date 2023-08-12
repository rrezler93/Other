import os
import tkinter as tk
import tkinter.filedialog
import PyInstaller.__main__

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x75")  # set the window size to 500x200
        self.master.title("PY to EXE converter")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create label for the file path
        self.filepath_label = tk.Label(self)
        self.filepath_label.pack(side="top")

        # Create button to choose file
        self.choose_file_button = tk.Button(self)
        self.choose_file_button["text"] = "Choose Python file"
        self.choose_file_button["command"] = self.choose_file
        self.choose_file_button.pack(side="top")

        # Create button to convert file to exe
        self.convert_button = tk.Button(self)
        self.convert_button["text"] = "Convert to exe"
        self.convert_button["command"] = self.convert_to_exe
        self.convert_button.pack(side="top")

    def choose_file(self):
        # Open file dialog to choose file
        filetypes = (("Python files", "*.py"), ("All files", "*.*"))
        filepath = tk.filedialog.askopenfilename(filetypes=filetypes)

        # Update filepath label with chosen file path
        self.filepath_label.config(text=filepath)

    def convert_to_exe(self):
        # Get file path from filepath label
        filepath = self.filepath_label.cget("text")

        # Check if the file path exists
        if not os.path.isfile(filepath):
            tk.messagebox.showerror("Error", "File not found.")
        else:
            # Use PyInstaller to convert the Python script to a standalone executable file
            PyInstaller.__main__.run([
                filepath,
                "--onefile",
                "--name={}".format(os.path.splitext(os.path.basename(filepath))[0]),
                "--clean",
                "--distpath={}".format(os.path.dirname(filepath)),
                # "--noconsole",
                # "--icon={}".format(os.path.join(os.path.dirname(filepath), "Logo/Logo_Icon.ico"))
            ])
            tk.messagebox.showinfo("Conversion complete", "The Python file has been successfully converted to an executable.")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

