from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer 

from datetime import datetime
from time import sleep

from threading import Thread

#colors
bg_color = '#dbc8ac'
col = "#b73e3e" 
col2 = "#962a29"

# window
window = Tk()
window.title("INF221 GROUP 10")
window.geometry('350x150')
window.configure(bg=bg_color)

# frames 

frame_line = Frame(window, width=500, height=20, bg=col)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=500, height=500, bg=bg_color)
frame_body.grid(row=1, column=0)

# #configuring frame body
img = Image.open('alarmf.png')
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=100, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text = "Alarm Clock", height=1, font = ('Ivy', 18, "bold"), bg=bg_color, fg=col)
name.place(x=160, y=10)

# #hours
hour = Label(frame_body, text = "hour", height=1, font = ('Varela round', 8, "bold"), bg=bg_color, fg=col2)
hour.place(x=127, y=40)

c_hour = Combobox(frame_body, width=2, font=('Varela round', 12))
c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(0)
c_hour.place(x=130, y=58)

# #minutes
min = Label(frame_body, text = "minutes", height=1, font = ('Varela round', 8, "bold"), bg=bg_color, fg=col2)
min.place(x=177, y=40)

c_min = Combobox(frame_body, width=2, font=('Varela round', 12))
c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", 
                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", 
                   "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", 
                   "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",)
c_min.current(0)
c_min.place(x=180, y=58)

# #seconds
sec = Label(frame_body, text = "seconds", height=1, font = ('Varela round', 8, "bold"), bg=bg_color, fg=col2)
sec.place(x=233, y=40)

c_sec = Combobox(frame_body, width=2, font=('Varela round', 12))
c_sec['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", 
                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", 
                   "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", 
                   "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",)
c_sec.current(0)
c_sec.place(x=235, y=58)

# period
period = Label(frame_body, text = "period", height=1, font = ('Varela round', 8, "bold"), bg=bg_color, fg=col2)
period.place(x=288, y=40)

c_period = Combobox(frame_body, width=3, font=('Varela round', 12))
c_period['values'] = ("AM", "PM")
c_period.current(0)
c_period.place(x=290, y=58)

def activate_alarm():
    t = Thread(target=alarm)
    t.start()

def deactivate_alarm():
    print('Deactivated alarm: ', selected.get())
    mixer.music.stop()

selected = IntVar()

#activate button
rad1 = Radiobutton(frame_body, font=('Varela round', 8, "bold"), value = 1, text = "Activate", 
                   bg=bg_color, fg=col, command=activate_alarm, variable=selected)
rad1.place(x = 150, y=87)

def sound_alarm():
    mixer.music.load('alarmSound.mp3')
    mixer.music.play()
    selected.set(0)
    
# Deactivate alarm
rad2 = Radiobutton(frame_body, font=('Varela round', 8, "bold"), value = 2, text = "Deactivate", 
                   bg=bg_color, fg=col, command=deactivate_alarm, variable=selected)
rad2.place(x = 230, y=87)

def alarm():
    while True:
        control = selected.get()
        print(control)
        
        alarm_hour = c_hour.get()
        alarm_minute = c_min.get()
        alarm_second = c_sec.get()
        alarm_period = c_period.get()
        alarm_period = str(alarm_period).upper()
    
        now = datetime.now()
        
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")
        
        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            print("Start your day with a smile! :D")
                            sound_alarm()
        sleep(1)
mixer.init()
window.mainloop() 