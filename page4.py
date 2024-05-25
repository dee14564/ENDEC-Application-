from tkinter import *
from tkinter import messagebox
from argparse import FileType
from tkinter.filedialog import *
from PIL import ImageTk, Image
from stegano import lsb
from tkinter import font as tkFont
from stegano import exifHeader as aaa
import os
from subprocess import Popen


def encode():
    main.destroy()
    enc = Tk()
    enc.attributes("-fullscreen", True)
    enc.wm_attributes('-transparentcolor')
    img = ImageTk.PhotoImage(Image.open("bg2.jpg"))
    fontl = tkFont.Font(family='Showcard Gothic', size=32)
    label1 = Label(enc, image=img)
    label1.pack()

    LabelTitle = Label(text="ENCODE", bg="plum3", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(x=420,y=100)

    def openfile():
        global fileopen
        global imagee

        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg,png files", "*jpg *png"), ("all files", "*.*")))
        imagee = ImageTk.PhotoImage(Image.open(fileopen))

        Labelpath = Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width=450)

        Labelimg = Label(image=imagee)
        Labelimg.place(relx=0.7, rely=0.3, height=200, width=200)

    Button2 = Button(text="Openfile",fg='white',bg='plum3', command=openfile)
    Button2.place(x=620,y=200, height=35, width=150)

    secimg = StringVar()
    radio1 = Radiobutton(text='jpeg', value='jpeg', variable=secimg)
    radio1.place(x=500,y=270,width=150)

    radio2 = Radiobutton(text='png', value='png', variable=secimg)
    radio2.place(x=780, y=270,width=150)

    Label1 = Label(text="Enter message",bd=30)
    Label1.place(x=500,y=400, height=30, width=130)
    entrysecmes = Entry()
    entrysecmes.place(x=660,y=395, relheight=0.05, relwidth=0.200)

    Label2 = Label(text="File Name",bd=30)
    Label2.place(x=500,y=450, height=30, width=130)

    entrysave = Entry()
    entrysave.place(x=660,y=449, relheight=0.05, relwidth=0.200)

    def encode():
        if secimg.get() == "jpeg":
            inimage = fileopen
            response = messagebox.askyesno("popup", "do you want to encode")
            if response == 1:
                aaa.hide(inimage, entrysave.get() + '.jpg', entrysecmes.get())
                messagebox.showinfo("popup", "successfully encode" + entrysave.get() + ".jpeg")


            else:
                messagebox.showwarning("popup", "unsuccessful")

        if secimg.get() == "png":
            inimage = fileopen
            response = messagebox.askyesno("popup", "do you want to encode")
            if response == 1:
                lsb.hide(inimage, message=entrysecmes.get()).save(entrysave.get() + '.png')
                messagebox.showinfo("popup", "successfully encode to " + entrysave.get() + ".png")


            else:
                messagebox.showwarning("popup", "unsuccessful")

    def back():
        enc.destroy()
        Popen('python page4.py')

    Button2 = Button(text="ENCODE",fg = 'white', bg = 'plum3', command=encode)
    Button2.place(x=620, y=600, height=35, width=150)

    Buttonback = Button(text="Back",fg = 'white', bg = 'plum3', command=back)
    Buttonback.place(x=620, y=650, height=35, width=150)


    enc.mainloop()


def decode():
    main.destroy()
    dec = Tk()
    dec.attributes("-fullscreen", True)
    dec.wm_attributes('-transparentcolor')
    img = ImageTk.PhotoImage(Image.open("bg2.jpg"))
    fontl = tkFont.Font(family='Showcard Gothic', size=32)
    label1 = Label(dec, image=img)
    label1.pack()

    LabelTitle = Label(text="DECODE", bg="plum3", fg="white", width=20)
    LabelTitle['font'] = fontl
    LabelTitle.place(x=420, y=100)

    secimg = StringVar()
    radio1 = Radiobutton(text='jpeg', value='jpeg', variable=secimg)
    radio1.place(x=500, y=340, width=150)

    radio2 = Radiobutton(text='png', value='png', variable=secimg)
    radio2.place(x=780, y=340, width=150)


    def openfile():
        global fileopen
        global imagee
        fileopen = StringVar()
        fileopen = askopenfilename(initialdir="/Desktop", title="select file",
                                   filetypes=(("jpeg files, png file", "*jpg *png"), ("all files", "*.*")))

        imagee = ImageTk.PhotoImage(Image.open(fileopen))
        Labelpath = Label(text=fileopen)
        Labelpath.place(relx=0.6, rely=0.25, height=21, width=450)

        Labelimg = Label(image=imagee)
        Labelimg.place(relx=0.7, rely=0.3, height=200, width=200)

    def deimg():
        if secimg.get() == "png":
            messag = lsb.reveal(fileopen)

        if secimg.get() == "jpeg":
            messag = aaa.reveal(fileopen)

        Label2 = Label(text=messag)
        Label2.place(relx=0.7, rely=0.7, height=21, width=204)

    Button2 = Button(text="Openfile", fg = 'white', bg = 'plum3', command=openfile)
    Button2.place(x=620, y=200, height=35, width=150)


    Button2 = Button(text="DECODE", fg='white', bg='plum3', command=deimg)
    Button2.place(x=620, y=550, height=35, width=150)

    def back():
        dec.destroy()
        Popen('python page4.py')

    Buttonback = Button(text="Back", fg='white', bg='plum3', command=back)
    Buttonback.place(x=620, y=600, height=35, width=150)

    dec.mainloop()


# main program
main = Tk()
main.title('Image Steganography ')
main.geometry("1300x750")
main.attributes("-fullscreen",True)
fontl = tkFont.Font(family='Showcard Gothic', size=30)

global image1
image1 = ImageTk.PhotoImage(Image.open("bg1.jpg"))
label = Label(main, text="lalal", image=image1)
label.pack()

encbutton = Button(text='Encode', fg="white",bg="plum2", width=20, command=encode)
encbutton['font'] = fontl
encbutton.place(x=430,y=170)

decbutton = Button(text='Decode', fg="white",bg="plum2", width=20, command=decode)
decbutton['font'] = fontl
decbutton.place(x=430,y=270)

def back():
    main.destroy()
    Popen('python page2.py')


backbutton = Button(text='BACK', fg="white",bg="plum2", width=20, command=back)
backbutton['font'] = fontl
backbutton.place(x=430,y=370)


def exit():
    main.destroy()


closebutton = Button(text='EXIT', fg="white",bg="plum2", width=20, command=exit)
closebutton['font'] = fontl
closebutton.place(x=430,y=470)
main.mainloop()