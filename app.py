import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window_width = 800
window_height = 600
header_height = 80
main_frames_padding = 10

window = tk.Tk()
window.title("Coffee defect detection")
window.geometry(f"{window_width}x{window_height}")
window.configure(bg="#d1c4ab")

# High-level frames
header_frame = ttk.Frame(
    window,
    height=header_height,
    width=window_width,
    padding=main_frames_padding)

body_frame = ttk.Frame(
    window,
    height=(window_height - header_height - 2 * main_frames_padding),
    width=window_width,
    padding=main_frames_padding)

header_frame.pack(
    pady=main_frames_padding,
    padx=main_frames_padding, fill="both")

body_frame.pack(
    pady=(0, main_frames_padding),
    padx=main_frames_padding)

# header_frame['borderwidth'] = 2
# header_frame['relief'] = 'solid'

# body_frame['borderwidth'] = 2
# body_frame['relief'] = 'solid'

# Header frame fill
# Logo
img = Image.open("logo.png")
img.thumbnail((header_height, header_height))
img = ImageTk.PhotoImage(img)

logo = ttk.Label(header_frame, image=img)
logo.grid(row=0, column=0, rowspan=2)

# Title
title = ttk.Label(
    header_frame, text="Detect defects in images of coffee beans", font=("Arial", 25))
title.grid(row=0, column=1, padx=main_frames_padding)

# Instructions
instructions = ttk.Label(header_frame, text="Instructions will be in here")
instructions.grid(row=1, column=1, pady=10, padx=10)


# Run the App
window.mainloop()
