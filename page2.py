from tkinter import *
from subprocess import Popen

ws = Tk()
ws.geometry('8000x500')
ws.title('Image steganography and File encryptor / decryptor')
ws['bg'] = '#5d8a82'



f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import page4


def prevPage():
    ws.destroy()
    import page5


Label(
    ws,
    text="Image steganography and File encryptor / decryptor",
    padx=20,
    pady=20,
    bg='plum',
    font=('Tw Cen MT Condensed Extra Bold', 40, 'bold'), fg="white"
).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Image steganography",
    bg='plum',
    font=('Tw Cen MT Condensed Extra Bold', 25, 'bold'), fg="white",
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

Button(
    ws,
    text="File encryptor / decryptor ",
    bg='plum',
    font=('Tw Cen MT Condensed Extra Bold', 25, 'bold'), fg="white",
    command=prevPage
).pack(fill=X, expand=TRUE, side=LEFT)


def back():
    ws.destroy()
    Popen('python ENDEC.py')


Buttonback = Button(ws,
    text="Back ",
    bg='plum',
    font=('Tw Cen MT Condensed Extra Bold', 25, 'bold'), fg="white",
    command=back
).pack(fill=X, expand=TRUE, side=LEFT)



ws.mainloop()
