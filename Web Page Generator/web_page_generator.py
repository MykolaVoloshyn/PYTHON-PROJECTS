import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.label_custom_txt = tk.Label(self.master, text="Enter custom text or click the Default page button")
        self.label_custom_txt.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky=N + W)

        self.custom_txt = tk.Entry(self.master, text="")
        self.custom_txt.grid(row=1, column=0, rowspan=1, columnspan=3, padx=(10, 10), pady=(10, 10), sticky=E + W)

        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.default_text)
        self.btn.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))

        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.custom_text)
        self.btn.grid(row=2, column=2, padx=(10, 10), pady=(10, 10))

    # decorator function that creates an HTML file with passed through a function text
    def create_html(function):
        def wrapper(self, *args, **kwargs):  # wrapper() takes self as a parameter to pass it to passed function
            html_text = function(self)
            # this block of code handles the creation of the HTML file
            html_file = open("index.html", "w")
            html_content = "<html>\n<body>\n<h1>" + html_text + "</h1>\n</body>\n</html>"
            html_file.write(html_content)
            html_file.close()

            # opens in the default browser created HTML file in a new tab
            webbrowser.open_new_tab("index.html")

        return wrapper

    @create_html  # Applying the decorator to a function
    def default_text(self):
        return "Stay for our amazing summer sale!"

    @create_html  # Applying the decorator to a function
    def custom_text(self):
        return self.custom_txt.get()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
