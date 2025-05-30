import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        # sets title of GUI window
        self.master.title("File Transfer")

        # creates button to select files from source derictory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # positions source button in GUI using tkinter grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        # creates entry for source directory selection
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        # creates button to select destination of files from destination derictory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        # creates entry for destination directory selection
        self.destenation_dir = Entry(width=75)
        self.destenation_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        # creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        # creates an exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # the .delete(0, END) will clear the content that is inserted in the Entry widget,
        # this allows the pass to be inserted into Entry widget properly.
        self.source_dir.delete(0, END)
        # the .insert() will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destenation_dir.delete(0, END)
        self.destenation_dir.insert(0, selectDestDir)

    # creates function to transfer files from on directory to another
    def transferFiles(self):
        source = self.source_dir.get()
        destination = self.destenation_dir.get()
        # gets a list of files in the source directory
        source_files = os.listdir(source)

        for i in source_files:
            # return date & time that was 24 hours ago
            # needed to execute the condition for files transfer
            time_condition = datetime.now() - timedelta(days=1)
            file_path = os.path.join(source, i)
            # return timestamp of when a file was last time modified
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))

            # checks if a file was modified not more thrn 24 hours ago
            if mod_time > time_condition:
                # moves each file from the source to the destination
                shutil.move(source + "/" + i, destination)
                print(i + " was succesfully transfered.")

    def exit_program(self):
        # root is the main GUI window, the Tkinter destrow method tells python
        # to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
