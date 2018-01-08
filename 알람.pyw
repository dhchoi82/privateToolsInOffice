#!/usr/bin/python3

import time
from tkinter import Tk, ttk#, LEFT , Frame, Label, Entry

def message(time, alarmtext=""):
    msgbox = Tk()
    timemsg = "설정된 {}분이 지났습니다.".format(time)
    lbl0 = ttk.Label(msgbox, text=timemsg)
    lbl0.pack()
    lbl1 = ttk.Label(msgbox, text=alarmtext)
    lbl1.pack()
    
    w = msgbox.winfo_width()+200
    h = msgbox.winfo_height()+40
    x = int((msgbox.winfo_screenwidth()-w)/2)
    y = int((msgbox.winfo_screenheight()-h)/2)
    
    msgbox.geometry("{}x{}+{}+{}".format(w,h,x,y))
    msgbox.mainloop()

root0 = Tk()
root = ttk.Frame(root0)
root.pack()

label0 = ttk.Label(root, text="설정시간")
label0.grid(row=0,column=0)

label1 = ttk.Label(root, text="알림문자")
label1.grid(row=1,column=0)

timeEntry = ttk.Entry(root)
textEntry = ttk.Entry(root)

def alarm(event):
    secondToSleep = 0
    minuteToSleep = float(timeEntry.get())
    alarmMessage = str(textEntry.get())
    
    try:
        secondToSleep = minuteToSleep*60
    except:
        pass
    finally:
        root0.destroy()
    
    time.sleep(secondToSleep)
    message(minuteToSleep, alarmMessage)

timeEntry.grid(row=0,column=1)
timeEntry.focus_set()
textEntry.grid(row=1,column=1)
root0.bind("<Return>", alarm)

unit = ttk.Label(root, text="분")
unit.grid(row=0,column=2)

root.mainloop()
