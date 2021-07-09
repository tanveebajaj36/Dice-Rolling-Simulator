import tkinter
from PIL import Image, ImageTk
import random

# top level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('Data Flair Roll the Dice')

# Adding label into the frame
l0 = tkinter.Label(root, text="")
l0.pack()

# adding label with different font and formatting
l1 = tkinter.Label(root, text="This is a Dice Rolling game!", fg="blue", font="Arial")
l1.pack()

# images
dice = ['Face 1.png', 'Face 2.png', 'Face 3.png', 'Face 4.png', 'Face 5.png', 'Face 6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
label1 = tkinter.Label(root, image=image1)
label1.image = image1

# packing a widget in the parent widget 
label1.pack(expand=True)

# function activated by button


def rolling_dice():
    image_1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image_1)
    # keep a reference
    label1.image = image_1


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='black', command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()
