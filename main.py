import tkinter
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
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    ticks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if reps in [0, 2, 4, 6]:
        mins_to_clock = 0.3
        reps += 1
        title_label.config(text="Work", fg=GREEN)
    elif reps in [1, 3, 5, 7]:
        mins_to_clock = 0.1
        reps += 1
        title_label.config(text="Break", fg=PINK)
    else:
        mins_to_clock = 0.2
        reps = 0
        title_label.config(text="Pause", fg=RED)
    count_down(mins_to_clock * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_mins = int(count / 60)
    count_secs = count % 60
    if count_mins == 0 and count_secs == 0:
        if reps-1 in [1, 3, 5, 7]:    # We want to add tick only after each break
            session = int((reps)/2)
            ticks_string = ""
            for _ in range(session):
                ticks_string += "✅"
            ticks.config(text=ticks_string)
        start_timer()
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro app")
window.config(padx=100, pady= 50, bg=YELLOW)

title_label = tkinter.Label(text="Timer", font=(FONT_NAME, 40, "normal"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)    # highlightthickness erases canvas border
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", highlightthickness=0, bg=GREEN, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text="Reset", highlightthickness=0, bg=RED, command=reset_timer)
reset_button.grid(column=2, row=2)

ticks = tkinter.Label(bg=YELLOW, fg="#006400")
ticks.grid(column=1, row=3)

window.mainloop()