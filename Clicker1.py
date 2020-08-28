from tkinter import *
import sys
from PIL import ImageTk, Image

root = Tk()
root.wm_title("Seal Clicker")


class IntInformation:
    def __init__(self):
        self.click = 1
        self.seals = 0
        self.worker = 0
        self.upgrades = [0, 0, 0]

    def seal_button(self):
        self.seals += self.click
        seals_display.configure(
            text="You have: " + str(intinfo.seals) + " seals")


seal_image = ImageTk.PhotoImage(Image.open("resources\seal.png"))

intinfo = IntInformation()

seals_display = Label(root, text="You have: " +
                      str(intinfo.seals) + " seals", font=("Everson Mono", 20))
seals_display.place(relx=0.1, rely=0.1)

button_start = Button(
    root, text="Seal", command=intinfo.seal_button, image=seal_image)
button_start.place(relheight=0.6, relwidth=0.4, relx=0.1, rely=0.3)

root.geometry("800x800")
root.mainloop()
