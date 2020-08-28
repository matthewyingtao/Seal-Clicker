from tkinter import *
import pickle
from math import floor
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
        self.radars = 0
        self.radars_cost = 100
        self.radars_yield = 3
        self.click_cost = 10

    def seal_button(self):
        self.seals += self.click
        if self.seals == 1:
            seals_display.configure(text="You have " + str(floor(self.seals)) + " seal")
        else:
            seals_display.configure(text="You have " + str(floor(self.seals)) + " seals")

    def click_upgrade(self):
        if self.seals >= self.click_cost:
            self.click = round(self.click * 2)
            self.seals -= self.click_cost
            self.click_cost = self.click_cost * 1.5
            seals_display.configure(text="You have: " + str(floor(self.seals)) + " seals")
            click_upgrade_button.configure(text="upgrade click \n" + str(floor(self.click_cost)) + " seals needed")

    def collector_buy(self):
        if self.seals >= self.collectors_cost:
            self.collectors += 1
            self.seals -= self.collectors_cost
            self.collectors_cost = self.collectors_cost * 1.3
            buy_collector_button.configure(text="Buy Collector \n" + str(floor(self.collectors_cost)) + " seals needed")

    def radars_buy(self):
        if self.seals >= self.radars_cost:
            self.radars += 1
            self.seals -= self.radars_cost
            self.radars_cost = self.radars_cost * 1.3
            buy_seal_radar_button.configure(
                text="Buy Seal Radar \n" + str(floor(self.radars_cost)) + " seals needed")

    def seals_update(self):
        if self.collectors > 0:
            self.seals += self.collectors_yield * self.collectors
        if self.radars > 0:
            self.seals += self.radars_yield * self.radars
        seals_display.configure(text="You have: " + str(floor(self.seals)) + " seals")
        root.after(1, self.seals_update)

    def max_buy(self, unit_cost, unit):
        unit_max_buy_cost = 0
        unit_max_buy = 0
        if unit_cost < self.seals:
            while True:
                unit_max_buy_cost = unit_max_buy_cost + unit_cost
                unit_cost = unit_cost * 1.3
                unit_max_buy += 1
                if unit_max_buy_cost > self.seals:
                    break
            unit_max_buy_cost = unit_max_buy_cost - unit_cost / 1.3
            self.seals -= unit_max_buy_cost
            if unit == 0:
                self.collectors += unit_max_buy
                self.collectors_cost = self.collectors_cost * (1.3 ** unit_max_buy)
            elif unit == 1:
                self.radars += unit_max_buy
                self.radars_cost = self.radars_cost * (1.3 ** unit_max_buy)
            elif unit == 2:
                self.click = self.click * (2 ** unit_max_buy)
                self.click_cost = self.click_cost * (1.5 ** unit_max_buy)

    def max_buy_collectors(self):
        self.max_buy(self.collectors_cost, 0)

    def max_buy_radars(self):
        self.max_buy(self.radars_cost, 1)

    def max_buy_click_upgrade(self):
        self.max_buy(self.click_cost, 2)

    def max_buy_display(self, unit_cost):  # Definition maximum buys display
        variable_1 = 0  # Figuring out the cost one buy more than maximum buys
        max_buy_variable = -1  # Amount of buys for the maximum
        while True:
            variable_1 = variable_1 + unit_cost
            unit_cost = unit_cost * 1.3
            max_buy_variable = max_buy_variable + 1
            if variable_1 > self.seals:
                break
        max_buy_str = str(max_buy_variable)
        return max_buy_str

    def max_buy_update(self):
        update_max_buy_collectors = self.max_buy_display(self.collectors_cost)
        max_buy_collectors_button.configure(text="x" + update_max_buy_collectors)
        root.after(64, self.max_buy_update)
        update_max_buy_radars = self.max_buy_display(self.radars_cost)
        max_buy_radars_button.configure(text="x" + update_max_buy_radars)
        update_max_buy_click_upgrade = self.max_buy_display(self.click_cost)
        max_buy_click_upgrade_button.configure(text="x" + update_max_buy_click_upgrade)


seal_image = ImageTk.PhotoImage(Image.open("Resources/seal.png"))
intinfo = IntInformation()

seals_display = Label(root, text="You have no seals", font=("Comic Sans MS", 20))
seals_display.place(relx=0.05)

seal_button = Button(root, text="Seal", command=intinfo.seal_button, image=seal_image)
seal_button.place(relheight=0.9, relwidth=0.4, relx=0.05, rely=0.06)

click_upgrade_button = Button(root, text="Upgrade Click \n" + str(intinfo.click_cost) + " seals needed",
                              command=intinfo.click_upgrade, font=("Comic Sans MS", 15))
click_upgrade_button.place(relheight=0.15, relwidth=0.4, relx=0.45, rely=0.06)

buy_collector_button = Button(root, text="Buy Collector \n" + str(intinfo.collectors_cost) + " seals needed",
                              command=intinfo.collector_buy, font=("Comic Sans MS", 15))
buy_collector_button.place(relheight=0.15, relwidth=0.4, relx=0.45, rely=0.21)

buy_seal_radar_button = Button(root, text="Buy Seal Radar \n" + str(intinfo.radars_cost) + " seals needed",
                               command=intinfo.radars_buy, font=("Comic Sans MS", 15))
buy_seal_radar_button.place(relheight=0.15, relwidth=0.4, relx=0.45, rely=0.36)

max_buy_click_upgrade_button = Button(root, text="buy max Upgrade Click", command=intinfo.max_buy_click_upgrade,
                                      font=("Comic Sans MS", 15))
max_buy_click_upgrade_button.place(relheight=0.15, relwidth=0.1, relx=0.85, rely=0.06)

max_buy_collectors_button = Button(root, text="buy max collectors", command=intinfo.max_buy_collectors,
                                   font=("Comic Sans MS", 15))
max_buy_collectors_button.place(relheight=0.15, relwidth=0.1, relx=0.85, rely=0.21)

max_buy_radars_button = Button(root, text="buy max radars", command=intinfo.max_buy_radars,
                               font=("Comic Sans MS", 15))
max_buy_radars_button.place(relheight=0.15, relwidth=0.1, relx=0.85, rely=0.36)

intinfo.seals_update()
intinfo.max_buy_update()

root.geometry("1000x800")
root.mainloop()
