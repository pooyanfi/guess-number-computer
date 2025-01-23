# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:16:37 2025

@author: pooyan ferdowsi
"""
import tkinter as tk
import random

# تنظیمات بازی
lower_bound = 0
upper_bound = 99
previous_guesses = []
hads = None

# تعریف توابع
def reset_game():
    """شروع دوباره بازی"""
    global lower_bound, upper_bound, previous_guesses, hads
    lower_bound = 0
    upper_bound = 99
    previous_guesses = []
    hads = random.randint(lower_bound, upper_bound)
    previous_label.config(text="Previous Guesses: []")
    update_message(f"Game reset! First guess: {hads}")

def go_down():
    """حدس کمتر"""
    global upper_bound, hads
    if hads is not None and hads > lower_bound:
        upper_bound = hads - 1
        make_guess()
    else:
        update_message("Invalid range! Cannot guess lower.")

def go_up():
    """حدس بیشتر"""
    global lower_bound, hads
    if hads is not None and hads < upper_bound:
        lower_bound = hads + 1
        make_guess()
    else:
        update_message("Invalid range! Cannot guess higher.")

def you_win():
    """نمایش پیغام برنده شدن"""
    update_message(f"Congratulations! The correct number was {hads}")

def update_message(message):
    """به‌روزرسانی پیام"""
    message_label.config(text=message)

def make_guess():
    """ایجاد یک حدس جدید"""
    global hads, previous_guesses
    if lower_bound <= upper_bound:
        hads = random.randint(lower_bound, upper_bound)
        previous_guesses.append(hads)
        previous_label.config(text=f"Previous Guesses: {previous_guesses}")
        update_message(f"My Guess: {hads}")
    else:
        update_message("No numbers left to guess!")

# رابط کاربری
root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("500x400")
root.configure(bg="#222831")

font_title = ("Helvetica", 20, "bold")
font_message = ("Helvetica", 16)
text_color = "#eeeeee"

title_label = tk.Label(root, text="Guess the Number", font=font_title, bg="#222831", fg=text_color)
title_label.pack(pady=10)

message_label = tk.Label(root, text="", font=font_message, bg="#222831", fg=text_color)
message_label.pack(pady=20)

previous_label = tk.Label(root, text="Previous Guesses: []", font=font_message, bg="#222831", fg=text_color)
previous_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#222831")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Go Down", command=go_down).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Go Up", command=go_up).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="You Win", command=you_win).grid(row=0, column=2, padx=10)

tk.Button(root, text="Restart Game", command=reset_game).pack(pady=20)

# شروع بازی
reset_game()
root.mainloop()
