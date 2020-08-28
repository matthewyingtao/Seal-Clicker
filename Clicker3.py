from tkinter import *
import pickle
from PIL import ImageTk, Image

root = Tk()
root.wm_title("Seal Clicker")


class IntInformation:
    def __init__(self):
        self.click = 1
        self.seals = 0
        self.worker = 0
        self.upgrades = [0, 0, 0]
        self.upgrades_cost = [10, 100, 1000]

    def seal_button(self):
        self.seals += self.click
        seals_display.configure(
            text="You have: " + str(intinfo.seals) + " seals")

    def click_upgrade(self):
        if self.seals >= self.upgrades_cost[self.upgrades[0]]:
            self.click *= 1.5
            self.seals -= self.upgrades_cost[0]
            self.upgrades_cost[0] *= 3
            seals_display.configure(
                text="You have: " + str(intinfo.seals) + " seals")
            click_upgrade_button.configure(
                text="Upgrade click \n" + str(intinfo.upgrades_cost[0]) + " seals needed")


seal_image = ImageTk.PhotoImage(Image.open("resources/seal.png"))

intinfo = IntInformation()

seals_display = Label(root, text="You have: " +
                      str(intinfo.seals) + " seals", font=("Comic Sans MS", 20))
seals_display.place(relx=0.05, rely=0.05)

seal_button = Button(
    root, text="Seal", command=intinfo.seal_button, image=seal_image)
seal_button.place(relheight=0.8, relwidth=0.4, relx=0.05, rely=0.15)

click_upgrade_button = Button(root, text="Upgrade click \n" + str(intinfo.upgrades_cost[0]) + " seals needed",
                              command=intinfo.click_upgrade, font=("Comic Sans MS", 15))
click_upgrade_button.place(relheight=0.15, relwidth=0.4, relx=0.45, rely=0.15)


root.geometry("800x800")
root.mainloop()
