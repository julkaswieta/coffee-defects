import tkinter as tk
from tkinter import ttk
from app_helpers import *
import threading

window_width = 800
window_height = 600
header_height = 80
main_frames_padding = 10

window = tk.Tk()
window.title("Coffee defect detection")
window.geometry(f"{window_width}x{window_height}")

# High-level frames
header_frame = tk.Frame(
    window,
    bg="#d1c4ab",
    height=header_height,
    width=window.winfo_width(),
    padx=main_frames_padding,
    pady=main_frames_padding)

body_frame = tk.Frame(
    window,
    bg="#d1c4ab",
    height=(window.winfo_height() - header_height - 2 * main_frames_padding),
    width=window.winfo_width(),
    padx=main_frames_padding,
    pady=main_frames_padding)

header_frame.pack(
    pady=main_frames_padding,
    padx=main_frames_padding, fill="both")

body_frame.pack(
    pady=(0, main_frames_padding),
    padx=main_frames_padding, fill="both", expand=True)

# Header frame fill
# Logo
logo_img = import_image("app/imgs/logo.png", header_height)
logo = tk.Label(header_frame, image=logo_img, bg="#d1c4ab")
logo.grid(row=0, column=0, rowspan=2)

# Title
title = tk.Label(
    header_frame, text="Detect defects in images of coffee beans", font=("Arial", 25), bg="#d1c4ab")
title.grid(row=0, column=1, padx=main_frames_padding)

# Instructions
instructions = tk.Label(
    header_frame, text="Upload image of your beans and then press 'Detect defects' to process the image.", bg="#d1c4ab", anchor="w")
instructions.grid(row=1, column=1, pady=10, padx=10)

# Body frame fill
# Image upload
img_selection_frame = tk.Frame(
    body_frame, width=(0.4 * body_frame.winfo_width()), height=body_frame.winfo_height(), bg="#d1c4ab")
img_selection_frame.pack(side=tk.LEFT, fill="y")

placeholder_path = tk.StringVar(window, value="app/imgs/placeholder.png")

ph_img = import_image(placeholder_path.get(), 200)
placeholder = tk.Label(img_selection_frame,
                       image=ph_img)
placeholder.pack(pady=20)

upload_img_btn = tk.Button(
    img_selection_frame, text="Upload image", command=lambda: select_image(placeholder, placeholder_path))
upload_img_btn.pack(fill="both")

# Processing
process_frame = tk.Frame(body_frame, width=0.2 * body_frame.winfo_width(),
                         height=body_frame.winfo_height(), bg="#d1c4ab", padx=20)
process_frame.pack(side=tk.LEFT, fill="y")

process_btn = tk.Button(
    process_frame,
    text="Detect defects"
)
process_btn.pack(pady=50, fill="both")

# Output display
# Scrollable canvas setup
canvas = tk.Canvas(body_frame, bg="#d1c4ab")
canvas.pack(side=tk.LEFT, fill="both", expand=True)

scrollbar = ttk.Scrollbar(body_frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# Bind canvas to update the scroll region
canvas.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# The output frame inside the canvas
output_frame = tk.Frame(canvas, bg="#d1c4ab", padx=20)
canvas.create_window((0, 0), window=output_frame, anchor="nw")

# add the command to the process button
process_btn.config(command=lambda: threading.Thread(
    target=detect_defects,
    args=(placeholder_path.get(), output_frame),
    daemon=True
).start())

window.mainloop()
