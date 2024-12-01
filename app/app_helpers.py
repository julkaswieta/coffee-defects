from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog as fd
from detect import process_image
import os


def import_image(img_path, size):
    img = Image.open(img_path)
    img.thumbnail((size, size))
    return ImageTk.PhotoImage(img)


def select_image(placeholder, img_path):
    try:
        filename = fd.askopenfilename(
            title='Select an image',
            initialdir='.',
            filetypes=[('Images', '*.jpg *.jpeg *.png')]
        )

        new_img = import_image(filename, 200)
        placeholder.config(image=new_img)
        placeholder.image = new_img

        img_path.set(filename)
    except:
        print("Couldn't load image")


def clear_existing_output(output_path):
    for file in os.listdir(output_path):
        os.remove(os.path.join(output_path, file))


def detect_defects(img_path, output_frame):
    output_path = os.path.abspath("./detected")

    clear_existing_output(output_path)
    process_image(img_path, output_path)

    output_frame.after(0, lambda: update_gallery(output_frame, output_path))


def update_gallery(output_frame, output_path):
    # Clear existing widgets
    for widget in output_frame.winfo_children():
        widget.destroy()

    # Display the updated gallery
    num_columns = 3
    image_size = (120, 120)
    row, col = 0, 0

    for img_path in os.listdir(output_path):
        path = os.path.join(output_path, img_path)
        img = Image.open(path)
        img.thumbnail(image_size)
        photo = ImageTk.PhotoImage(img)

        img_display = tk.Label(output_frame, image=photo)
        img_display.image = photo
        img_display.grid(row=row, column=col, padx=10, pady=(0, 10))

        img_label = tk.Label(
            output_frame, text=select_label(img_path), anchor="center")
        img_label.grid(row=row+1, column=col, padx=10, pady=(0, 10))

        col += 1
        if col >= num_columns:
            col = 0
            row += 2


def select_label(filename):
    if "defect" in filename:
        return "Defect"
    elif "longberry" in filename:
        return "Longberry"
    elif "peaberry" in filename:
        return "Peaberry"
    elif "premium" in filename:
        return "Premium bean"
    else:
        return "Unknown"
