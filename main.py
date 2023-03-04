import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window

keyboard_keys = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace', 'Tab', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', 'CapsLock', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'Enter', 'Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'Shift', 'Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Ctrl', '←', '↑', '↓', '→']

word_count = 0
seconds_5 = 5
timer_id = None  # identifier for the timer
game=True

def start():
    global game,count
    game=True
    count_down()
    count = 6
    label_secs_5.configure(text=count)
    button.place_forget()
    label_word_count.configure(font=("Arial", 40),fg_color="white")
    entry.configure(state="normal", background="white")
    button_color.place(x=0, y=0)
    button_color_1.place(x=0, y=940)




def countdown():
    """Count down from 5 to 0 and restart when a key is pressed"""
    global count, timer_id,game
    count = 6
    label_secs_5.configure(text=count)
    def counting():
        """Count down by 1 every second"""
        global count, timer_id,game
        if count > 0:
            count -= 1
            label_secs_5.configure(text=count)
            timer_id = label_secs_5.after(1000, counting)
        if count == 6:
            button_color.configure(fg_color="#5D9C59")
            button_color_1.configure(fg_color="#5D9C59")

            label_games_secs.configure(fg_color="#5D9C59")
        if count == 5:
            button_color.configure(fg_color="#5D9C59")
            button_color_1.configure(fg_color="#5D9C59")

            label_games_secs.configure(fg_color="#5D9C59")
        if count == 4:
            button_color.configure(fg_color="#C7E8CA")
            button_color_1.configure(fg_color="#C7E8CA")

            label_games_secs.configure(fg_color="#C7E8CA")
        if count == 3:
            button_color.configure(fg_color="#DDF7E3")
            button_color_1.configure(fg_color="#DDF7E3")

            label_games_secs.configure(fg_color="#DDF7E3")
        if count == 2:
            button_color.configure(fg_color="#E96479")
            button_color_1.configure(fg_color="#E96479")

            label_games_secs.configure(fg_color="#E96479")
        if count == 1:
            button_color.configure(fg_color="#F55050")
            button_color_1.configure(fg_color="#F55050")

            label_games_secs.configure(fg_color="#F55050")
        if count == 0:
            button_color.configure(fg_color="#DF2E38")
            button_color_1.configure(fg_color="#DF2E38")

            label_games_secs.configure(fg_color="#DF2E38")
            label_secs_5.configure(text="Countdown finished!")
            game = False
            entry.configure(state="disabled", fg="#434242")


    counting()

def reset():
    """Reset the countdown timer"""
    global timer_id
    if timer_id:
        label_secs_5.after_cancel(timer_id)
        timer_id = None
    countdown()

def count_down(secs=300):  # 60 Secs For Game Time
    if secs == -1 or game==False:
        entry.configure(state="disabled",background="#EEEEEE")
        button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        label_word_count.configure(font=("Arial",120),fg_color="#EEEEEE")
        label_games_secs.configure(fg_color="#DF2E38")
        button_color.place_forget()
        button_color_1.place_forget()




    else:
        label_games_secs.configure(text=secs)
        root.after(1000, count_down, secs - 1)




    return secs

def check(event):
    """Handle key press event"""
    if event.keysym != "space":
        reset()
    root.after(10, check_delayed, event)

def check_delayed(event):
    """Handle key press event after a brief delay"""
    global word_count
    inp = entry.get(1.0, "end-1c")
    if len(inp) >= 1:
        if event.keysym == "space":
            if inp[::-1][1]== " " or inp[::-1][1] == "" or not inp:
                pass
            else:
                print(inp[::-1][1])
                word_count += 1
                label_word_count.configure(text=word_count)


entry = tk.Text(root,width=74,height=40.8,font=("Arial",15),insertofftime=5,state="disabled",)
entry.place(x=0,y=50)

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root, text="START", command=start,width=250,height=220,fg_color="#DD5353",text_color="#674747",font=("MonoScape",50),hover_color="#B73E3E")
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


label_secs_5=customtkinter.CTkLabel(master=root, text="5",font=("Arial",40),text_color="#FCFFE7",)
label_secs_5.place(x=400, y=735, anchor=tk.CENTER)
label_secs_5.place_forget()

label_word_count=customtkinter.CTkLabel(master=root, text="0",font=("Arial",40),text_color="black",fg_color="white")
label_word_count.place(x=400, y=805, anchor=tk.CENTER)





button_color = customtkinter.CTkButton(master=root, text="", width=800,height=50,fg_color="#5D9C59",text_color="black",state="disabled")
button_color.place(x=0, y=0)



button_color_1 = customtkinter.CTkButton(master=root, text="", width=800,height=50,fg_color="#5D9C59",text_color="black",state="disabled")
button_color_1.place(x=0, y=940)

label_games_secs=customtkinter.CTkLabel(master=root,fg_color="#5D9C59", text="60",font=("Arial",40),text_color="black")
label_games_secs.place(x=400, y=20, anchor=tk.CENTER)








root.bind("<Key>", check)

window_width = 800
window_height = 990
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y-40}')
root.mainloop()

