import tkinter as tk
from PIL import Image, ImageTk
import time


root = tk.Tk()
root.geometry('1000x666')
root.title('Spam Mail Classifier')
bg_image = Image.open('bg.png')
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
button_image = Image.open('comp.png')
button_photo = ImageTk.PhotoImage(button_image)
button = tk.Button(root, image=button_photo, bd=0, highlightthickness=0, highlightbackground='#ffffff', bg='#ffffff', activebackground='#ffffff', relief='flat')
button.place(x=350, y=450)
time_label = tk.Label(root, font=('DS-Digital', 20), fg='black')
time_label.pack(side=tk.RIGHT, anchor=tk.SE, padx=10, pady=10)

def update_time():
    current_time = time.strftime('%H:%M %p')
    current_day = time.strftime('%A')
    time_label.config(text=f'{current_time}\n{current_day}')
    root.after(1000, update_time)


update_time()
root.mainloop()
