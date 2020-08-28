from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.wm_title("Seal Clicker")


class IntInformation:
    def __init__(self):
        self.click = 1
        self.seals = 0
        self.collectors = 0
        self.collectors_cost = 15
        self.collectors_yield = 1
        self.seal_radars = 0
        self.seal_radars_cost = 100
        self.seal_radars_yield = 3
        self.upgrades = [0, 0, 0]
        self.upgrades_cost = [10, 100, 1000]

    def seal_button(self):
        self.seals += self.click
        seals_display.configure(
            text="You have: " + str(intinfo.seals) + " seals")

    def click_upgrade(self):
        if self.seals >= self.upgrades_cost[self.upgrades[0]]:
            self.click = round(self.click * 1.5)
            self.seals -= self.upgrades_cost[0]
            self.upgrades_cost[0] *= 3
            seals_display.configure(
                text="You have: " + str(self.seals) + " seals")
            click_upgrade_button.configure(
                text="Upgrade click \n" + str(self.upgrades_cost[0]) + " seals needed")

    def collector_buy(self):
        if self.seals >= self.collectors_cost:
            self.collectors += 1
            self.seals -= self.collectors_cost
            self.collectors_cost = round(self.collectors_cost * 1.3)
            buy_collector_button.configure(
                text="Buy Collector \n" + str(self.collectors_cost) + " seals needed")
            if self.collectors == 1:
                self.seals_update()

    def seals_update(self):
        if self.collectors > 0:
            self.seals += self.collectors_yield * self.collectors
        if self.seal_radars > 0:
            self.seals += self.seal_radars_yield * self.seal_radars
        seals_display.configure(text="You have: " + str(self.seals) + " seals")
        root.after(50, self.seals_update)

    def seal_radars_buy(self):
        if self.seals >= self.seal_radars_cost:
            self.seal_radars += 1
            self.seals -= self.seal_radars_cost
            self.seal_radars_cost = round(self.seal_radars_cost * 1.3)
            buy_seal_radar_button.configure(
                text="Buy Seal Radar \n" + str(self.seal_radars_cost) + " seals needed")


seal_image = ImageTk.PhotoImage(Image.open("Resources/seal.png"))

intinfo = IntInformation()

seals_display = Label(root, text="You have: " +
                      str(intinfo.seals) + " seals", font=("Comic Sans MS", 20))
seals_display.place(relx=0.05, rely=0.05)

seal_button = Button(
    root, text="Seal", command=intinfo.seal_button, image=seal_image)
seal_button.place(relheight=0.8, relwidth=0.4, relx=0.05, rely=0.15)

click_upgrade_button = Button(root, text="Upgrade Click \n" + str(intinfo.upgrades_cost[0]) + " seals needed",
                              command=intinfo.click_upgrade, font=("Comic Sans MS", 15))
click_upgrade_button.place(relheight=0.15, relwidth=0.5, relx=0.45, rely=0.15)

buy_collector_button = Button(root, text="Buy Collector \n" + str(intinfo.collectors_cost) + " seals needed",
                              command=intinfo.collector_buy, font=("Comic Sans MS", 15))
buy_collector_button.place(relheight=0.15, relwidth=0.5, relx=0.45, rely=0.3)

buy_seal_radar_button = Button(root, text="Buy Seal Radar \n" + str(intinfo.seal_radars_cost) + " seals needed",
                               command=intinfo.seal_radars_buy, font=("Comic Sans MS", 15))
buy_seal_radar_button.place(relheight=0.15, relwidth=0.5, relx=0.45, rely=0.45)

root.geometry("800x800")
root.mainloop()
