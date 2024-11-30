from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import time


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

        # showinfo(
        #     title="Image selected",
        #     message=filename
        # )

        new_img = import_image(filename, 200)
        placeholder.config(image=new_img)
        placeholder.image = new_img

        img_path.set(filename)
    except:
        print("Couldn't load image")


def detect_defects(img_path):
    print(img_path)
    print("detecting beans here")
