from tkinter import *
import pickle
from math import floor
from PIL import ImageTk, Image

root = Tk()
root.wm_title("Seal Clicker")

# opens the seal image used for the seal button
seal_image = ImageTk.PhotoImage(Image.open("Resources/seal.png"))
# opens the images used for the page 1 units
cursor_image = ImageTk.PhotoImage(Image.open("Resources/cursor.png"))
trash_image = ImageTk.PhotoImage(Image.open("Resources/trash.png"))
radar_image = ImageTk.PhotoImage(Image.open("Resources/radar.png"))
factory_image = ImageTk.PhotoImage(Image.open("Resources/factory.png"))
bean_image = ImageTk.PhotoImage(Image.open("Resources/bean.png"))
# opens the images used for the page 2 units
collector_image = ImageTk.PhotoImage(Image.open("Resources/collector.png"))
fire_image = ImageTk.PhotoImage(Image.open("Resources/fire.png"))
riot_image = ImageTk.PhotoImage(Image.open("Resources/riot.png"))
plush_seal_image = ImageTk.PhotoImage(Image.open("Resources/plush_seal.png"))
hell_seal_image = ImageTk.PhotoImage(Image.open("Resources/hell_seal.png"))


# this class contains values used by other objects and other misc variables
class UniversalValues:
    def __init__(self):
        self.seals = 0
        self.time_1 = 0
        self.time_2 = 0
        self.tick_rate = 50
        self.background_color = "#36558B"
        self.text_color = "#F2EDD7"
        self.disabled_text_color = "#242B63"
        self.seal_button_color = "#639EFF"
        self.seal_button_active_color = "#5A90E8"
        self.unit_button_color = "#5A8EE6"
        self.unit_button_active_color = "#5282D2"
        self.page_button_color = "#5D80D5"
        root.after(128, self.per_second_display)

    # this method is executed when the seal button is clicked, it adds the click yield to seals, and updates the seal label
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


# This class is for units, contains the buttons to buy the unit, and to buy max units
class Unit:
    def __init__(self, name, cost, produce, y_button, page_number, frame, image):
        self.name = name
        self.units = 0
        self.unit_cost = cost
        self.unit_yield = produce
        self.variable_2 = 0
        self.y_button = y_button
        if page_number == 1:
            self.frame = page_1_frame
        elif page_number == 2:
            self.frame = page_2_frame
        self.buy_unit_button = Button(frame,
                                      text="Buy " + self.name + " (" + str(self.units) + ")\n" + str(
                                          self.unit_cost) + " seals needed", command=self.unit_buy,
                                      font=("Georgia", 15), bg=uni_values.unit_button_color, activebackground=uni_values.unit_button_active_color,
                                      foreground=uni_values.text_color, activeforeground=uni_values.text_color, image=image,
                                      compound="left", justify=CENTER)
        self.max_buy_unit_button = Button(frame, text="x0", command=self.max_buy_cost,
                                          font=("Georgia", 15), bg=uni_values.unit_button_color, activebackground=uni_values.unit_button_active_color,
                                          foreground=uni_values.text_color, activeforeground=uni_values.text_color)

        self.buy_unit_button.place(relheight=0.18, relwidth=0.8, rely=self.y_button)
        self.max_buy_unit_button.place(relheight=0.18, relwidth=0.2, relx=0.8, rely=self.y_button)
        root.after(50, self.max_buy_display)
        if self.name != "Click":
            root.after(50, self.seals_update)
        else:
            root.after(50, self.click_update)

    # This method is used only for the click unit, makes the yield exponential different to other units
    def click_update(self):
        self.unit_yield = 1 * (2 ** self.units)
        root.after(100, self.click_update)

    # This method adds one unit, takes away the cost, and updates the cost of the next unit
    def unit_buy(self):
        if uni_values.seals >= self.unit_cost:
            self.units += 1
            uni_values.seals -= self.unit_cost
            self.unit_cost = self.unit_cost * 1.3
            self.buy_unit_button.configure(
                text="Buy " + self.name + " (" + str(self.units) + ")\n" + str(floor(self.unit_cost)) + " seals needed")
            seals_display.configure(text="You have: " + str(floor(uni_values.seals)) + " seals")

    # This method updates the max buy button's text to be the max amount the player can buy at a time as num + 'x',
    # it also passes the amount of units the player can buy as an argument to the 'max_buy_cost' function
    def max_buy_display(self):  # Definition maximum buys display
        unit_cost = self.unit_cost
        max_buy_cost = 0  # Figuring out the cost one buy more than maximum buys
        max_buy_units = 0  # Amount of buys for the maximum
        while True:
            max_buy_cost = max_buy_cost + unit_cost
            if max_buy_cost > uni_values.seals:
                max_buy_cost -= unit_cost
                break
            unit_cost = unit_cost * 1.3
            max_buy_units = max_buy_units + 1
        self.max_buy_unit_button.configure(text=str(max_buy_units) + "x")
        root.after(128, self.max_buy_display)
        return max_buy_units

    # This method is executed when the max buy button is pressed and gets deducts the cost from the seals amount, as
    # well as updating both the seal label and the buy unit button
    def max_buy_cost(self):
        max_buy_units = self.max_buy_display()
        max_cost = 0
        for i in range(0, max_buy_units):
            variable_1 = self.unit_cost * (1.3 ** i)
            max_cost = max_cost + variable_1
            self.variable_2 = variable_1
        uni_values.seals = uni_values.seals - max_cost
        self.unit_cost = self.unit_cost * (1.3 ** max_buy_units)
        self.units += max_buy_units
        seals_display.configure(text="You have: " + str(floor(uni_values.seals)) + " seals")
        self.buy_unit_button.configure(
            text="Buy " + self.name + " (" + str(self.units) + ")\n" + str(floor(self.unit_cost)) + " seals needed")
        return self.variable_2

    # This method is for the unit to update the seals amount by the units * yield
    def seals_update(self):
        uni_values.seals += self.units * self.unit_yield
        seals_display.configure(text="You have: " + str(floor(uni_values.seals)) + " seals")
        root.after(uni_values.tick_rate, self.seals_update)


# This class is for the page buttons at the bottom of the screen for page navigation and their functionality
class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.button_length = 0.5 / 2
        self.clicked = 1
        self.page_button = Button(root, text="page " + str(self.page_number), command=self.page_change,
                                  font=("Georgia", 15), bg=uni_values.page_button_color, activebackground=uni_values.background_color,
                                  foreground=uni_values.text_color, activeforeground=uni_values.text_color, disabledforeground=uni_values.disabled_text_color)
        self.page_button.place(relheight=0.09, relwidth=self.button_length,
                               relx=(0.45 + ((self.page_number - 1) * self.button_length)), rely=0.83)
        if self.page_number == 1:
            self.page_button.configure(state=DISABLED)

    # This method places the page frame onto the canvas, and "hides" all other page frames, then disables the button
    def page_change(self):
        if self.page_number == 1:
            page_1_frame.place(relheight=0.84, relwidth=0.5, relx=0.45, rely=0.08)
            page_2_frame.place_forget()
            page_2.page_button.configure(state=NORMAL)
            self.page_button.configure(state=DISABLED)
        elif self.page_number == 2:
            page_2_frame.place(relheight=0.84, relwidth=0.5, relx=0.45, rely=0.08)
            page_1_frame.place_forget()
            self.page_button.configure(state=DISABLED)
            page_1.page_button.configure(state=NORMAL)


uni_values = UniversalValues()
root.configure(bg=uni_values.background_color)

page_1_frame = Frame(root)
page_1_frame.place(relheight=0.84, relwidth=0.5, relx=0.45, rely=0.08)

click = Unit("Click", 10, 1, 0, 1, page_1_frame, cursor_image)
osu_player = Unit("Osu Player", 15, 1, 0.18, 1, page_1_frame, trash_image)
radar = Unit("Radar", 100, 10, 0.36, 1, page_1_frame, radar_image)
factory = Unit("Factory", 2000, 50, 0.54, 1, page_1_frame, factory_image)
astolfo_bean = Unit("Astolfo Bean", 50000, 250, 0.72, 1, page_1_frame, bean_image)

page_2_frame = Frame()

collector = Unit("Collector", 50000, 250, 0, 2, page_2_frame, collector_image)
hell = Unit("Hell", 50000, 250, 0.18, 2, page_2_frame, fire_image)
certainlyt = Unit("CertainlyT", 50000, -250, 0.36, 2, page_2_frame, riot_image)
beeg_seal = Unit("Beeg Seal", 50000, 250, 0.54, 2, page_2_frame, plush_seal_image)
hell_seal = Unit("Seal of Hell", 50000, 250, 0.72, 2, page_2_frame, hell_seal_image)

page_1 = Page(1)
page_2 = Page(2)

seals_display = Label(root, font=("Georgia", 20), bg=uni_values.background_color,
                      foreground=uni_values.text_color)
seals_display.place(relx=0.05, rely=0.01)

seal_button = Button(root, command=uni_values.seal_button, image=seal_image, bg=uni_values.seal_button_color,
                     activebackground=uni_values.seal_button_active_color)
seal_button.place(relheight=0.84, relwidth=0.4, relx=0.05, rely=0.08)

per_second_display = Label(root, text="0 SPS", font=("Georgia", 20), bg=uni_values.background_color, foreground=uni_values.text_color)
per_second_display.place(relx=0.05, rely=0.93)

tick_slider = Scale(root, from_=1, to=1000, orient=HORIZONTAL)
tick_slider.place(relwidth=0.5, relx=0.45, rely=0.93)

root.geometry("1000x800")
root.mainloop()
