from tkinter import *
from tkinter import ttk

# colors
c1 = "#2e2e2d"  # black
c2 = "#feffff"
c3 = "#38576b"
c4 = "#eceff1"
c5 = "#ffab40"

# Creating window
window = Tk()
window.title("Calculator")

# Size Values
window.geometry("235x310")
window.config()

# Creating frames
frame_display = Frame(window, width=235, height=50, bg=c3)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=268, )
frame_body.grid(row=1, column=0)

# Variable all values
all_values = ""


# Creating function
def input_values(event):
    global all_values
    all_values = all_values + str(event)
    # Show values on display
    value_text.set(all_values)


# function to calculate
def calculate():
    global all_values
    result = eval(all_values)
    value_text.set(str(result))


# Function clear display
def clear():
    global all_values
    all_values = ""
    value_text.set("")


# Creating labels
value_text = StringVar()
display_label = Label(frame_display, textvariable=value_text, width=16, height=2, padx=5, relief=FLAT, anchor="e",
                      justify=RIGHT, font='Ivy 18', bg=c3, fg=c2)
display_label.place(x=0, y=0)

# Creating buttons in frame_body
b_c = Button(frame_body, command=clear, text="C", width=11, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_c.place(x=0, y=0)

b_p = Button(frame_body, command=lambda: input_values('%'), text="%", width=5, height=2, bg=c4, font='Ivy 13 bold',
             relief=RAISED, overrelief=RIDGE)
b_p.place(x=118, y=0)

b_div = Button(frame_body, command=lambda: input_values('/'), text="/", width=5, height=2, bg=c5, fg=c2, font='Ivy 13 bold', relief=RAISED,
               overrelief=RIDGE)
b_div.place(x=177, y=0)

# line (7 8 9 and *)
b_7 = Button(frame_body, command=lambda: input_values('7'), text="7", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=52)
b_8 = Button(frame_body, command=lambda: input_values('8'), text="8", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)
b_9 = Button(frame_body, command=lambda: input_values('9'), text="9", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=52)

b_times = Button(frame_body, command=lambda: input_values('*'), text="*", width=5, height=2, bg=c5, fg=c2, font='Ivy 13 bold', relief=RAISED,
                 overrelief=RIDGE)
b_times.place(x=177, y=52)

# line (4 5 6 and -)
b_4 = Button(frame_body, command=lambda: input_values('4'), text="4", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104)
b_5 = Button(frame_body, command=lambda: input_values('5'), text="5", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)
b_6 = Button(frame_body, command=lambda: input_values('6'), text="6", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=104)

b_minus = Button(frame_body, command=lambda: input_values('-'), text="-", width=5, height=2, bg=c5, fg=c2, font='Ivy 13 bold', relief=RAISED,
                 overrelief=RIDGE)
b_minus.place(x=177, y=104)

# line (1 2 3 and +)
b_1 = Button(frame_body, command=lambda: input_values('1'), text="1", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=156)
b_2 = Button(frame_body, command=lambda: input_values('2'), text="2", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=156)
b_3 = Button(frame_body, command=lambda: input_values('3'), text="3", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=156)

b_ = Button(frame_body, command=lambda: input_values('+'), text="+", width=5, height=2, bg=c5, fg=c2, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_.place(x=177, y=156)

# line (0 .  =)
b_0 = Button(frame_body, command=lambda: input_values('0'), text="0", width=11, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=208)

b_dot = Button(frame_body, command=lambda: input_values('.'), text=".", width=5, height=2, bg=c4, font='Ivy 13 bold', relief=RAISED, overrelief=RIDGE)
b_dot.place(x=118, y=208)

b_equals = Button(frame_body, command=calculate, text="=", width=5, height=2, bg=c5, fg=c2, font='Ivy 13 bold', relief=RAISED,
                  overrelief=RIDGE)
b_equals.place(x=177, y=208)

# looping window
window.mainloop()
