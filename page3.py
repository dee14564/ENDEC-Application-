#Message encryption and decryption
#vignere cipher
from tkinter import *
import random
import base64
from subprocess import Popen

root = Tk()
root.title(" Message  Encryptor / Decryptor ")

Tops = Frame(root, width=100,relief=RAISED,bg="plum")
Tops.pack(ipadx=140, ipady=10,side=TOP)

f1 = Frame(root, width=400,relief=RAISED,bg="plum")
f1.pack(ipadx=350, ipady=200,side=RIGHT)


lblInfo = Label(Tops, font=('Tw Cen MT Condensed Extra Bold', 52,'bold'),
                text="      Message Encryption and Decryption ",
                fg="snow", bd=100, anchor='w',bg="plum",justify='center')

lblInfo.grid(row=0, column=2)



# Initializing variables
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()


# labels for the message
lblMsg = Label(f1, font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),
               text="MESSAGE", bd=20, anchor="w",bg="plum",fg="snow")

lblMsg.grid(row=1, column=0)

# Entry box for the message
txtMsg = Entry(f1, font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),fg="snow",
               textvariable=Msg, bd=10, insertwidth=4,
               bg="orchid", justify='right')


txtMsg.grid(row=1, column=1)


# labels for the key
lblkey = Label(f1, font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),
               text="KEY (Only Integer)", bd=20, anchor="w",bg="plum",fg="snow")

lblkey.grid(row=2, column=0)

# Entry box for the key
txtkey = Entry(f1, font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),fg="snow",
               textvariable=key, bd=10, insertwidth=4,
               bg="orchid", justify='right')

txtkey.grid(row=2, column=1)


# labels for the mode
lblmode = Label(f1, font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),
                text="MODE(e for encrypt, d for decrypt)",
                bd=20, anchor="w",bg="plum",fg="snow")

lblmode.grid(row=3, column=0)

# Entry box for the mode
txtmode = Entry(f1, font=('Tw Cen MT Condensed Extra Bold', 20,'bold'),fg="snow",
                textvariable=mode, bd=10, insertwidth=4,
                bg="orchid", justify='right')

txtmode.grid(row=3, column=1)



# labels for the result
lblResult = Label(f1, font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),
                  text="The Result :-", bd=20, anchor="w",bg="plum",fg="snow")

lblResult.grid(row=2, column=2)

# Entry box for the result
txtResult = Entry(f1, font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),fg="snow",
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="orchid", justify='right')

txtResult.grid(row=2, column=3)

# Vigenère cipher

# Function to encode


def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode


def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


def Results():

    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'e'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))



# Function to reset the window


def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


# Show message button
btnTotal = Button(f1, padx=10, pady=8, bd=10,
                  font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'), width=10,
                  text="Show Message", bg="orchid",fg="snow",command=Results).grid(row=9, column=1)

# Reset button
btnReset = Button(f1, padx=10, pady=8, bd=10,
                   font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),
                  width=10, text="Reset", bg="orchid",fg="snow",
                  command=Reset).grid(row=9, column=2)


#back button

def back():
    root.destroy()
    Popen('python ENDEC.py')


Buttonback = Button(f1, padx=10, pady=8, bd=10, font=('Tw Cen MT Condensed Extra Bold', 20, 'bold'),
                 width=10, text="Back", bg="orchid",fg="snow",
                 command=back).grid(row=9, column=3)

# keeps window alive
root.mainloop()
