
from tkinter import *
from datetime import datetime
import time
import pytz

def Time_zones():

    """ first time zone """

    first_home = pytz.timezone("Asia/Tokyo")
    first_local_time = datetime.now(first_home)
    first_current_time = first_local_time.strftime("%a %H:%M:%S")
    first_clock_label.config(text = first_current_time)
    first_label.config(text = "Japan")
    first_clock_label.after(200 , Time_zones)

    """ second time zone """

    second_home = pytz.timezone("Asia/Kolkata")
    second_local_time = datetime.now(second_home)
    second_current_time = second_local_time.strftime("%a %H:%M:%S")
    second_clock_label.config(text = second_current_time)
    second_label.config(text = "India")
    second_clock_label.after(200 , Time_zones)

    """ third time zone """

    third_home = pytz.timezone("europe/London")
    third_local_time = datetime.now(third_home)
    third_current_time = third_local_time.strftime("%a %H:%M:%S")
    third_clock_label.config(text = third_current_time)
    third_label.config(text = "London")
    third_clock_label.after(200 , Time_zones)

    """ fourth time zone """

    fourth_home = pytz.timezone("America/New_York")
    fourth_local_time = datetime.now(fourth_home)
    fourth_current_time = fourth_local_time.strftime("%a %H:%M:%S")
    fourth_clock_label.config(text = fourth_current_time)
    fourth_label.config(text = "New_York")
    fourth_clock_label.after(200 , Time_zones)


root = Tk()

root.title("UTC")
root.geometry("1200x400")
root.config(bg= "#ccddff")


app_icon = PhotoImage(file = "World Clock.png")
root.iconphoto(False , app_icon)

# first time zone 

first_frame = Frame(root , bd = 5 , bg = "#ccddff")
first_frame.place(x = 10 , y = 118 , width = 220 , height = 150)

first_label = Label(first_frame , font = ("Raleway" , 35) , bg = "#ccddff")
first_label.place(x = 50 , y = 10)

first_country_logo = PhotoImage(file = "jp.png")
first_label_image = Label(root , image = first_country_logo)
first_label_image.place(x = 20 , y = 150)

first_clock_label = Label(first_frame , font = ("Raleway" , 15))
first_clock_label.place(x = 5 , y = 80)

# second time zone 

second_frame = Frame(root , bd = 5 , bg = "#ccddff")
second_frame.place(x = 300 , y = 118 , width = 220 , height = 150)

second_label = Label(second_frame , font = ("Raleway" , 35) , bg = "#ccddff")
second_label.place(x = 30 , y = 10)

second_country_logo = PhotoImage(file = "in.png")
second_label_image = Label(root , image = second_country_logo)
second_label_image.place(x = 290 , y = 150)

second_clock_label = Label(second_frame , font = ("Raleway" , 15))
second_clock_label.place(x = 5 , y = 80)

# third time zone 

third_frame = Frame(root , bd = 5 , bg = "#ccddff")
third_frame.place(x = 600 , y = 118 , width = 220 , height = 150)

third_label = Label(third_frame , font = ("Raleway" , 35) , bg = "#ccddff")
third_label.place(x = 50 , y = 10)

third_country_logo = PhotoImage(file = "gb.png")
third_label_image = Label(root , image = third_country_logo)
third_label_image.place(x = 600 , y = 150)

third_clock_label = Label(third_frame , font = ("Raleway" , 15))
third_clock_label.place(x = 5 , y = 80)

# fourth time zone 

fourth_frame = Frame(root , bd = 5 , bg = "#ccddff")
fourth_frame.place(x = 900 , y = 118 , width = 220 , height = 150)

fourth_label = Label(fourth_frame , font = ("Raleway" , 26) , bg = "#ccddff")
fourth_label.place(x = 50 , y = 10)

fourth_country_logo = PhotoImage(file = "us.png")
fourth_label_image = Label(root , image = fourth_country_logo)
fourth_label_image.place(x = 900 , y = 150)

fourth_clock_label = Label(fourth_frame , font = ("Raleway" , 15))
fourth_clock_label.place(x = 5 , y = 80)

Time_zones()

root.mainloop()