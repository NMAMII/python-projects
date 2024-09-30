from tkinter import *
import math

# constants required for the code and for an easier adjustment if desired
pink = "#e2979c"
green = "#00A86B"
font = "Ariel"
working_time = 25
short_break = 5
long_break = 20
session = 0
timer_on = None


def timer_reset():
    """resetting the timer once the user press reset and all the working sessions will
    be set to zero, and the title return to its initial state"""
    window.after_cancel(timer_on)
    canvas.itemconfig(timer_text, text='00:00')
    timer.config(text="Timer", fg=green)
    check.config(text='')
    global session
    session = 0


def timer_start():
    """this function is for initiating the min counts and then adjust the title accordingly,
    for setting the break time according to the pomodoro technique;
    the break time varies with respect to the session order as shown in the function if statements"""
    global session
    work_time = working_time * 60
    long_break_time = long_break * 60
    short_break_time = short_break * 60
    session += 1
    if session % 8 == 0:
        timer['fg'] = green
        timer['text'] = 'break time'
        count_down(long_break_time)
    elif session % 2 == 0:
        timer['fg'] = green
        timer['text'] = 'break time'
        count_down(short_break_time)
    else:
        timer['fg'] = '#EE4B2B'
        timer['text'] = 'work time'
        count_down(work_time)


def count_down(count):
    """counts down according to the timer_start function,
    then proceed to add a check mark indicating that a work session was done
    """
    minutes = math.floor(count/60)
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif 10 > sec > 0:
        sec = f'0{sec}'
    if minutes - 10 < 0:
        minutes = f'0{minutes}'
    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count > 0:
        global timer_on
        timer_on = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        check_marks = ''
        sessions = math.floor(session / 2)
        for i in range(sessions):
            check_marks += '✓'
        check.config(text=check_marks)


# Setting the window
window = Tk()
window.title("Pomodoro")
window.config(padx=40,pady=40,bg='white')

# Loading the tomato image
canvas = Canvas(width=300,height=300,bg='white', highlightthickness=0)
photo = PhotoImage(file='output-onlinepngtools (1).png')
canvas.create_image(150,120,image =photo)
timer_text = canvas.create_text(150, 260, text="00:00", fill=pink, font=(font, 20, 'bold'))
canvas.grid(column=1,row=1)

# Starting label
timer = Label(text='Timer', font=(font, 20, 'bold'))
timer.config(bg='white', fg=green)
timer.grid(column=1,row = 0)

# Start button
button_start = Button(text='start', font=(font, 15, 'bold'), command=timer_start)
button_start.config(bg='white',fg='gray')
button_start.grid(row=3,column=0)
# Reset button
button_reset = Button(text='reset', font=(font, 15, 'bold'), command=timer_reset)
button_reset.config(bg='white',fg='gray')
button_reset.grid(row=3,column=2)

# Check mark
check = Label(font=(font, 15, 'bold'))
check.config(bg='white', fg=green)
check.grid(column=1,row = 3)

window.mainloop()
