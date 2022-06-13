from tkinter import *
from tkinter import messagebox
import pyautogui
import time

class AutoType:
    def __init__(self):
        self.x, self.y = 0, 0

        self.window = Tk()
        self.window.title("AutoType 1.0")
        self.window.config(padx=20, pady=30)

        self.file_label = Label(text="File name:", justify=LEFT)
        self.file_label.grid(column=0, row=0)
        self.file_entry = Entry()
        self.file_entry.grid(column=1, row=0, padx=15)
        self.file_entry.insert(0, "script.txt")
        self.file_button = Button(text="Print Text", command=self.get_text)
        self.file_button.grid(column=2, row=0)

        self.coords_label = Label(text="Select textbox:", justify=LEFT)
        self.coords_label.grid(column=0, row=1)
        self.coords_button = Button(text="Select", command=self.select_coords, width=20)
        self.coords_button.grid(column=1, row=1)
        self.xy_label = Label(text="x, y")
        self.xy_label.grid(column=2, row=1)

        self.time_label = Label(text="Time interval:", justify=LEFT)
        self.time_label.grid(column=0, row=2)
        self.time_entry = Entry()
        self.time_entry.grid(column=1, row=2, padx=15)
        self.time_entry.insert(0, "0")

        self.repeat_label = Label(text="Repeat (0 for infinite):")
        self.repeat_label.grid(column=0, row=3)
        self.repeat_entry = Entry()
        self.repeat_entry.grid(column=1, row=3)
        self.repeat_entry.insert(0, "0")

        self.spam_button = Button(text="Type!", command=self.type_text)
        self.spam_button.grid(column=0, row=4, columnspan=3)

        self.window.mainloop()

    def select_coords(self):
        time.sleep(2)
        self.x, self.y = pyautogui.position()
        print(self.x, self.y)
        self.window.lift()
        self.window.attributes("-topmost", True)
        # self.window.focus_force()
        self.xy_label.config(text=f"{self.x}, {self.y}")

    def get_text(self):
        try:
            with open(self.file_entry.get(), "r") as f:
                for sentence in f:
                    print(sentence.strip("\n"))
        except FileNotFoundError:
            messagebox.showinfo(title="File Not Found", message="The file was not found. Please a valid file name.")

    def type_text(self):
        try:
            if self.repeat_entry.get() == "0":
                while True:
                    with open(self.file_entry.get(), "r") as f:
                        pyautogui.click(self.x, self.y)

                        for sentence in f:
                            pyautogui.typewrite(sentence.strip("\n"))
                            pyautogui.press("enter")
                            if int(self.time_entry.get()) > 0:
                                time.sleep(int(self.time_entry.get()))
            else:
                temp = 0
                while int(self.repeat_entry.get()) > temp:
                    with open(self.file_entry.get(), "r") as f:
                        for sentence in f:
                            pyautogui.typewrite(sentence.strip("\n"))
                            pyautogui.press("enter")
                            if int(self.time_entry.get()) > 0:
                                time.sleep(int(self.time_entry.get()))
                        temp += 1
        except FileNotFoundError:
            messagebox.showinfo(title="File Not Found", message="The file was not found. Please a valid file name.")

if __name__ == "__main__":
    AutoType()
