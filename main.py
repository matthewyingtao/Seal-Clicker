from tkinter import *
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

# root.iconbitmap(default="resources/bean.ico")

# these arrays contain the hexadecimals used for color
blue_theme = ["#36558B", "#F2EDD7", "#242B63", "#639EFF",
              "#5A90E8", "#5A8EE6", "#5282D2", "#5D80D5"]
pink_theme = ["#8B3636", "#D7F2F0", "#632C24", "#FF6363",
              "#D25252", "#D76173", "#E85A63", "#D55D79"]
green_theme = ["#214F4B", "#FFE6FF", "#242B63",
               "#2ACC95", "#15C78B", "#11AD7E", "#109E73", "#16AD8F"]
dark_theme = ["#121212", "#E0E0E0", "#A0A0A0", "#393939",
              "#323232", "#292929", "#323232", "#202020"]
burn_eyes_theme = ["#00ff00", "#ffff66", "#00ff00",
                   "#ff00ff", "#ff00ff", "#00ff00", "#ff00ff", "#ff00ff"]

# these lists contain the buttons of a type, so that they can be easily configured to a theme
unit_buttons = []
labels = []
frames = []
pages = []

# this class is used to configure all objects to the theme color


class Theme:
    def __init__(self, font, init_theme):
        self.font = font
        self.theme = init_theme
        self.background_color = self.theme[0]
        self.text_color = self.theme[1]
        self.disabled_text_color = self.theme[2]
        self.seal_button_color = self.theme[3]
        self.seal_button_active_color = self.theme[4]
        self.unit_button_color = self.theme[5]
        self.unit_button_active_color = self.theme[6]
        self.page_button_color = self.theme[7]

    # this method is used when the theme is changed, and sets the color of all objects
    def theme_change(self):
        self.background_color = self.theme[0]
        self.text_color = self.theme[1]
        self.disabled_text_color = self.theme[2]
        self.seal_button_color = self.theme[3]
        self.seal_button_active_color = self.theme[4]
        self.unit_button_color = self.theme[5]
        self.unit_button_active_color = self.theme[6]
        self.page_button_color = self.theme[7]
        root.configure(bg=theme.background_color)
        seal_button.configure(bg=theme.seal_button_color,
                              activebackground=theme.seal_button_active_color)
        page_3_frame.configure(bg=theme.background_color)
        for label in labels:
            label.configure(bg=theme.background_color,
                            foreground=theme.text_color)
        for page in pages:
            page.configure(bg=theme.page_button_color,
                           activebackground=theme.unit_button_active_color,
                           foreground=theme.text_color, activeforeground=theme.text_color,
                           disabledforeground=theme.disabled_text_color)
        for button in unit_buttons:
            button.configure(bg=theme.unit_button_color,
                             activebackground=theme.unit_button_active_color,
                             foreground=theme.text_color, activeforeground=theme.text_color)


# this class contains values used by other objects and other misc variables
class UniversalValues:
    def __init__(self):
        self.seals = 0
        self.time_1 = 0
        self.time_2 = 0
        self.tick_rate = 50
        root.after(128, self.per_second_display)

    # this method is executed when the seal button is clicked, it adds the click yield to seals, and updates the seal label
    def seal_button(self):
        self.seals += click.unit_yield
        if self.seals == 1:
            seals_display.configure(
                text="You have: " + str(floor(self.seals)) + " seal")
        else:
            seals_display.configure(
                text="You have: " + str(floor(self.seals)) + " seals")

    # this method updates the Seals Per Second label
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
                                      font=(theme.font, 15), bg=theme.unit_button_color,
                                      activebackground=theme.unit_button_active_color,
                                      foreground=theme.text_color, activeforeground=theme.text_color,
                                      image=image, compound="left", justify=CENTER)
        self.max_buy_unit_button = Button(frame, text="x0", command=self.max_buy_cost,
                                          font=(theme.font, 15), bg=theme.unit_button_color,
                                          activebackground=theme.unit_button_active_color,
                                          foreground=theme.text_color, activeforeground=theme.text_color)
        self.buy_unit_button.place(
            relheight=0.18, relwidth=0.8, rely=self.y_button)
        self.max_buy_unit_button.place(
            relheight=0.18, relwidth=0.2, relx=0.8, rely=self.y_button)
        unit_buttons.append(self.buy_unit_button)
        unit_buttons.append(self.max_buy_unit_button)
        root.after(50, self.max_buy_display)
        if self.name != "Click":
            root.after(50, self.seals_update)
        else:
            root.after(50, self.click_update)

    # This method is used only for the click unit, makes the yield exponential different to other units
    def click_update(self):
        self.unit_yield = (1.1 ** self.units) + (self.units * 2)
        root.after(100, self.click_update)

    # This method adds one unit, takes away the cost, and updates the cost of the next unit
    def unit_buy(self):
        if uni_values.seals >= self.unit_cost:
            self.units += 1
            uni_values.seals -= self.unit_cost
            self.unit_cost = self.unit_cost * 1.1
            self.buy_unit_button.configure(
                text="Buy " + self.name + " (" + str(self.units) + ")\n" + str(floor(self.unit_cost)) + " seals needed")
            seals_display.configure(
                text="You have: " + str(floor(uni_values.seals)) + " seals")

    # This method updates the max buy button's text to be the max amount the player can buy at a time as num + 'x',
    # it also passes the amount of units the player can buy as an argument to the 'max_buy_cost' function
    def max_buy_display(self):
        unit_cost = self.unit_cost
        max_buy_cost = 0  # Figuring out the cost of one buy more than maximum buys
        max_buy_units = 0  # Amount of buys for the maximum
        while True:
            max_buy_cost = max_buy_cost + unit_cost
            if max_buy_cost > uni_values.seals:
                max_buy_cost -= unit_cost
                break
            unit_cost = unit_cost * 1.1
            max_buy_units = max_buy_units + 1
        self.max_buy_unit_button.configure(text=str(max_buy_units) + "x")
        root.after(128, self.max_buy_display)
        # passes the max buy units as an argument, used for the "max_buy_cost" function
        return max_buy_units

    # This method is executed when the max buy button is pressed and gets deducts the cost from the seals amount, as
    # well as updating both the seal label and the buy unit button
    def max_buy_cost(self):
        max_buy_units = self.max_buy_display()
        max_cost = 0
        for i in range(0, max_buy_units):
            variable_1 = self.unit_cost * (1.1 ** i)
            max_cost = max_cost + variable_1
            self.variable_2 = variable_1
        uni_values.seals = uni_values.seals - max_cost
        self.unit_cost = self.unit_cost * (1.1 ** max_buy_units)
        self.units += max_buy_units
        seals_display.configure(
            text="You have: " + str(floor(uni_values.seals)) + " seals")
        self.buy_unit_button.configure(
            text="Buy " + self.name + " (" + str(self.units) + ")\n" + str(floor(self.unit_cost)) + " seals needed")
        return self.variable_2

    # This method is for the unit to update the seals amount by the units * yield
    def seals_update(self):
        uni_values.seals += self.units * self.unit_yield
        seals_display.configure(
            text="You have: " + str(floor(uni_values.seals)) + " seals")
        root.after(uni_values.tick_rate, self.seals_update)


# This class is for the page buttons at the bottom of the screen for page navigation and their functionality
class Page:
    def __init__(self, page_number):
        self.page_number = page_number
        self.button_length = 0.5 / 3
        self.clicked = 1
        self.page_button = Button(root, text="Page " + str(self.page_number), command=self.page_change,
                                  font=(theme.font, 15), bg=theme.page_button_color,
                                  activebackground=theme.unit_button_active_color,
                                  foreground=theme.text_color, activeforeground=theme.text_color,
                                  disabledforeground=theme.disabled_text_color)
        self.page_button.place(relheight=0.09, relwidth=self.button_length,
                               relx=(0.45 + ((self.page_number - 1) * self.button_length)), rely=0.83)
        pages.append(self.page_button)
        if self.page_number == 1:
            self.page_button.configure(state=DISABLED)
        elif self.page_number == 3:
            self.page_button.configure(text="Settings")

    # This method places the page frame onto the canvas, and "hides" all other page frames, then disables the button
    def page_change(self):
        if self.page_number == 1:
            page_1_frame.place(relheight=0.84, relwidth=0.5,
                               relx=0.45, rely=0.08)
            page_2_frame.place_forget()
            page_3_frame.place_forget()
            page_2.page_button.configure(state=NORMAL)
            page_3.page_button.configure(state=NORMAL)
            self.page_button.configure(state=DISABLED)
        elif self.page_number == 2:
            page_2_frame.place(relheight=0.84, relwidth=0.5,
                               relx=0.45, rely=0.08)
            page_1_frame.place_forget()
            page_3_frame.place_forget()
            self.page_button.configure(state=DISABLED)
            page_3.page_button.configure(state=NORMAL)
            page_1.page_button.configure(state=NORMAL)
        elif self.page_number == 3:
            page_3_frame.place(relheight=0.84, relwidth=0.5,
                               relx=0.45, rely=0.08)
            page_1_frame.place_forget()
            page_2_frame.place_forget()
            self.page_button.configure(state=DISABLED)
            page_1.page_button.configure(state=NORMAL)
            page_2.page_button.configure(state=NORMAL)


# creates the theme object, arguments are: "font, initial theme"
theme = Theme("Georgia", blue_theme)
uni_values = UniversalValues()

# this function is called when any of the theme buttons are pressed


def theme_change(pressed_theme):
    theme.theme = pressed_theme
    theme.theme_change()


root.configure(bg=theme.background_color)

page_1_frame = Frame(root)
page_1_frame.place(relheight=0.84, relwidth=0.5, relx=0.45, rely=0.08)

# Creates the units of page 1, arguments for units are: "Name, initial cost, yield, which page frame, which image to use"
click = Unit("Click", 50, 1, 0, 1, page_1_frame, cursor_image)
osu_player = Unit("Osu Player", 15, 0.1, 0.18, 1, page_1_frame, trash_image)
radar = Unit("Radar", 100, 0.5, 0.36, 1, page_1_frame, radar_image)
factory = Unit("Factory", 2000, 10, 0.54, 1, page_1_frame, factory_image)
astolfo_bean = Unit("Astolfo Bean", 50000, 25, 0.72,
                    1, page_1_frame, bean_image)

page_2_frame = Frame()

# Creates the units of page 2
collector = Unit("Collector", 200000, 75, 0, 2, page_2_frame, collector_image)
hell = Unit("Hell", 500000, 175, 0.18, 2, page_2_frame, fire_image)
certainlyt = Unit("CertainlyT", 2, -500, 0.36, 2, page_2_frame, riot_image)
beeg_seal = Unit("Beeg Seal", 1000000, 500, 0.54,
                 2, page_2_frame, plush_seal_image)
hell_seal = Unit("Seal of Hell", 5000000, 2000, 0.72,
                 2, page_2_frame, hell_seal_image)

page_3_frame = Frame(background=theme.background_color)

settings_label = Label(page_3_frame, text="Settings", font=(theme.font, 24), bg=theme.background_color,
                       foreground=theme.text_color)
settings_label.place(relwidth=1, relx=0, rely=0)

tick_rate_label = Label(page_3_frame, text="Tick rate", font=(theme.font, 15), bg=theme.background_color,
                        foreground=theme.text_color)
tick_rate_label.place(relwidth=1, relx=0, rely=0.08)

tick_slider = Scale(page_3_frame, from_=1, to=1000, orient=HORIZONTAL)
tick_slider.place(relwidth=1, relx=0, rely=0.13)
tick_slider.set(30)

themes_label = Label(page_3_frame, text="Themes", font=(theme.font, 15), bg=theme.background_color,
                     foreground=theme.text_color)
themes_label.place(relwidth=1, relx=0, rely=0.21)

blue_theme_button = Button(page_3_frame, font=(theme.font, 20), text="Blue Theme",
                           command=lambda: theme_change(blue_theme),
                           bg=blue_theme[5], activebackground=blue_theme[6], foreground=blue_theme[1])
blue_theme_button.place(relwidth=1, relheight=0.16, relx=0, rely=0.253)

pink_theme_button = Button(page_3_frame, font=(theme.font, 20), text="Pink Theme",
                           command=lambda: theme_change(pink_theme),
                           bg=pink_theme[5], activebackground=pink_theme[6], foreground=pink_theme[1])
pink_theme_button.place(relwidth=1, relheight=0.16, relx=0, rely=0.413)

green_theme_button = Button(page_3_frame, font=(theme.font, 20), text="Green Theme",
                            command=lambda: theme_change(green_theme),
                            bg=green_theme[5], activebackground=green_theme[6], foreground=green_theme[1])
green_theme_button.place(relwidth=1, relheight=0.16, relx=0, rely=0.573)

dark_theme_button = Button(page_3_frame, font=(theme.font, 20), text="Dark Theme",
                           command=lambda: theme_change(dark_theme),
                           bg=dark_theme[5], activebackground=dark_theme[6], foreground=dark_theme[1])
dark_theme_button.place(relwidth=1, relheight=0.16, relx=0, rely=0.733)

# Creates the pages and sets makes them the page object
page_1 = Page(1)
page_2 = Page(2)
page_3 = Page(3)

# This label displays the amount of seals the user has
seals_display = Label(root, font=(theme.font, 20), bg=theme.background_color,
                      foreground=theme.text_color)
seals_display.place(relx=0.05, rely=0.01)

# This button is the seal clicking button
seal_button = Button(root, command=uni_values.seal_button, image=seal_image, bg=theme.seal_button_color,
                     activebackground=theme.seal_button_active_color)
seal_button.place(relheight=0.84, relwidth=0.4, relx=0.05, rely=0.08)

# This label displays the "Seals Per Second" (includes clicks)
per_second_display = Label(root, text="0 SPS", font=(theme.font, 20), bg=theme.background_color,
                           foreground=theme.text_color)
per_second_display.place(relx=0.05, rely=0.93)

# Adds the labels and frames to their respective lists
labels.extend([settings_label, tick_rate_label, themes_label,
               seals_display, per_second_display])
frames.extend([page_1_frame, page_2_frame, page_3_frame])

# This sets the initial size of the window
root.geometry("800x600")
root.mainloop()
