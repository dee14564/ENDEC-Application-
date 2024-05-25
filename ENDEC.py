from tkinter import *
from subprocess import Popen
from PIL import ImageTk, Image
from tkinter import font as tkFont

ws = Tk()
ws.geometry("1105x550")
ws.title('Endec')
ws.resizable(0, 0)


global image1
image1 = ImageTk.PhotoImage(Image.open("v.jpg"))

canvas = Canvas(ws,width= 800, height= 400)
canvas.pack(fill= "both", expand=True)

# Display image
canvas.create_image(0, 0, image=image1, anchor="nw")

# Add a text in canvas
#canvas.create_text(270,250,text=" Image steganography \n Message Encryptor & Decryptor \n File encryptor and decryptor",
#                font=("Tw Cen MT Condensed Extra Bold", 30),fill="white")

def nextPage():
    ws.destroy()
    import page2


def prevPage():
    ws.destroy()
    import page3



Button(
    ws,
    text="Files",
    bg='snow',
    font=('Tw Cen MT Condensed Extra Bold', 25, 'bold'), fg="orchid4",
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="Plain Text",
    bg='snow',
    font=('Tw Cen MT Condensed Extra Bold', 25, 'bold'), fg="orchid4",
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)


def Page():
    ws.destroy()
    Popen('python password-vault.py')


backbutton = Button(ws,
                    text="Password generator and manager",
                    bg='snow',
                    font=('Tw Cen MT Condensed Extra Bold', 25, 'bold'), fg="orchid4",
                    command=Page).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
