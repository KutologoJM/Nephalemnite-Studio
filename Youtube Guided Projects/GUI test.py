import tkinter as tk
from tkinter import messagebox

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Large Tkinter App")

        # Create a menu bar
        menubar = tk.Menu(self.master)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.master.config(menu=menubar)

        # Create buttons
        self.open_button = tk.Button(self.master, text="Open Window 1", command=self.open_window1)
        self.open_button.pack(pady=10)

        self.open_button2 = tk.Button(self.master, text="Open Window 2", command=self.open_window2)
        self.open_button2.pack(pady=10)

    def open_window1(self):
        window1 = tk.Toplevel(self.master)
        window1.title("Window 1")

        label = tk.Label(window1, text="This is Window 1")
        label.pack(pady=10)

        button = tk.Button(window1, text="Close", command=window1.destroy)
        button.pack(pady=10)

    def open_window2(self):
        window2 = tk.Toplevel(self.master)
        window2.title("Window 2")

        entry = tk.Entry(window2)
        entry.pack(pady=10)

        button = tk.Button(window2, text="Submit", command=lambda: self.show_message(entry.get()))
        button.pack(pady=10)

    def show_message(self, text):
        messagebox.showinfo("Message", f"Entered text: {text}")

    def open_file(self):
        messagebox.showinfo("Open", "File opened")

    def save_file(self):
        messagebox.showinfo("Save", "File saved")

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
