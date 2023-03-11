from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_countdown():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    l_timer.config(text="Timer", fg=GREEN)
    l_checkmark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_countdown():
    global reps # this application is very small so it's arguably fine to use global here
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        l_timer.config(text="Long", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        l_timer.config(text="Short", fg=PINK)
    elif reps % 2 != 0:
        count_down(work_sec)
        l_timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10: count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_countdown()
        num_check_mark = reps // 2
        l_checkmark.config(text="✔"*num_check_mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Background image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Label
l_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
l_checkmark = Label(fg=GREEN, bg=YELLOW)

l_checkmark.grid(column=1, row=3)
l_timer.grid(column=1, row=0)

# Button
btn_start = Button(text="Start", highlightthickness=0, command=start_countdown)
btn_reset = Button(text="Reset", highlightthickness=0, command=reset_countdown)

btn_start.grid(column=0, row=2)
btn_reset.grid(column=2, row=2)


window.mainloop()



