from tkinter import *
import pickle
from math import floor
from PIL import ImageTk, Image

root = Tk()
root.wm_title("Seal Clicker")
root.configure(relief=FLAT, bg="steelblue4")


class IntInformation:
    def __init__(self):
        self.seals = 0
        self.time_1 = 0
        self.time_2 = 0
        self.tick_rate = 50
        root.after(128, self.per_second_display)

    def seal_button(self):
        self.seals += click.unit_yield
        if self.seals == 1:
            seals_display.configure(text="You have: " + str(floor(self.seals)) + " seal")
        else:
            seals_display.configure(text="You have: " + str(floor(self.seals)) + " seals")

    def per_second_display(self):
        if self.time_1 == 0:
            self.time_1 = self.seals
        elif self.time_1 != 0:
            self.time_2 = self.seals
            per_second = (self.time_2 - self.time_1) // 1
            per_second_display.configure(text=str(per_second) + "SPS")
            self.time_1 = 0
            self.time_2 = 0
        self.tick_rate = tick_slider.get()
        root.after(1000, self.per_second_display)


class Unit:
    def __init__(self, name, cost, produce, buttony):
        self.name = name
        self.units = 0
        self.unit_cost = cost
        self.unit_yield = produce
        self.variable_2 = 0
        self.buttony = buttony

        self.buy_unit_button = Button(root,
                                      text="Buy " + self.name + " (" + str(self.units) + ")\n" + str(
                                          self.unit_cost) + " seals needed", command=self.unit_buy,
                                      font=("Georgia", 15), bg="steelblue3", activebackground="steelblue4",
                                      foreground="lightsteelblue1", activeforeground="lightsteelblue1")
        self.buy_unit_button.place(relheight=0.15, relwidth=0.4, relx=0.45, rely=self.buttony)

        self.max_buy_unit_button = Button(root, text="x0", command=self.max_buy_cost,
                                          font=("Georgia", 15), bg="steelblue3", activebackground="steelblue4",
                                          foreground="lightsteelblue1", activeforeground="lightsteelblue1")
        self.max_buy_unit_button.place(relheight=0.15, relwidth=0.1, relx=0.85, rely=self.buttony)
        root.after(50, self.max_buy_display)
        if self.name != "Click":
            root.after(50, self.seals_update)
        else:
            root.after(50, self.click_update)

    def click_update(self):
        self.unit_yield = 1 * (2 ** self.units)
        root.after(100, self.click_update)

    def unit_buy(self):
        if intinfo.seals >= self.unit_cost:
            self.units += 1
            intinfo.seals -= self.unit_cost
            self.unit_cost = self.unit_cost * 1.3
            self.buy_unit_button.configure(
                text="Buy " + self.name + " (" + str(self.units) + ")\n" + str(floor(self.unit_cost)) + " seals needed")
            seals_display.configure(text="You have: " + str(floor(intinfo.seals)) + " seals")

    def max_buy_display(self):  # Definition maximum buys display
        unit_cost = self.unit_cost
        max_buy_cost = 0  # Figuring out the cost one buy more than maximum buys
        max_buy_units = 0  # Amount of buys for the maximum
        while True:
            max_buy_cost = max_buy_cost + unit_cost
            if max_buy_cost > intinfo.seals:
                max_buy_cost -= unit_cost
                break
            unit_cost = unit_cost * 1.3
            max_buy_units = max_buy_units + 1
        self.max_buy_unit_button.configure(text=str(max_buy_units) + "x")
        root.after(128, self.max_buy_display)
        return max_buy_units

    def max_buy_cost(self):
        max_buy_units = self.max_buy_display()
        max_cost = 0
        for i in range(0, max_buy_units):
            variable_1 = self.unit_cost * (1.3 ** i)
            max_cost = max_cost + variable_1
            self.variable_2 = variable_1
        intinfo.seals = intinfo.seals - max_cost
        self.unit_cost = self.unit_cost * (1.3 ** max_buy_units)
        self.units += max_buy_units
        seals_display.configure(text="You have: " + str(floor(intinfo.seals)) + " seals")
        self.buy_unit_button.configure(
            text="Buy " + self.name + " (" + str(self.units) + ")\n" + str(floor(self.unit_cost)) + " seals needed")
        return self.variable_2

    def seals_update(self):
        intinfo.seals += self.units * self.unit_yield
        seals_display.configure(text="You have: " + str(floor(intinfo.seals)) + " seals")
        root.after(intinfo.tick_rate, self.seals_update)


seal_image = ImageTk.PhotoImage(Image.open("Resources/seal.png"))

intinfo = IntInformation()
click = Unit("Click", 10, 1, 0.08)
collector = Unit("Collector", 15, 1, 0.23)
radar = Unit("Radar", 100, 10, 0.38)
factory = Unit("Factory", 2000, 50, 0.53)
astolfo_bean = Unit("Astolfo Bean", 50000, 250, 0.68)

seals_display = Label(root, text="You have no seals", font=("Georgia", 20), bg="steelblue4",
                      foreground="lightsteelblue1")
seals_display.place(relx=0.05, rely=0.01)

seal_button = Button(root, text="Seal", command=intinfo.seal_button, image=seal_image, bg="steelblue2",
                     activebackground="steelblue3")
seal_button.place(relheight=0.84, relwidth=0.4, relx=0.05, rely=0.08)

per_second_display = Label(root, text="0 SPS", font=("Georgia", 20), bg="steelblue4", foreground="lightsteelblue1")
per_second_display.place(relx=0.05, rely=0.93)

tick_slider = Scale(root, from_=1, to=1000, orient=HORIZONTAL)
tick_slider.place(relwidth=0.5, relx=0.45, rely=0.93)

root.geometry("1000x800")
root.mainloop()
