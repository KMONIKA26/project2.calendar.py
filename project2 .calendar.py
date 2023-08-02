from tkinter import *
from tkcalendar import *

# create object
root = Tk()

# set geometry
root.geometry("400x400")

#add calendar
cal = Calendar(root, selectmode = 'day',year = 2001, month =6,day = 26)
cal.pack(pady=20)

def grad_date():
    date.config(text = "Selected Date is: "+ cal.get_date())
    
# add button and label 
Button(root, text = "Get Date",command = grad_date).pack(pady=20)
date = Label(root, text= "")
date.pack(pady = 20)
#Execute tkinter
root.mainloop()
