#!usr/bin/env python3
import sys, os
from tkinter import *
from PIL import Image, ImageTk
import qrcode

def main():

    if (len(sys.argv) == 2):
        print(f"Usage: python3 {sys.argv[1]} <search string> ")
        sys.exit(1)

    # create new window and change its traits
    root = Tk()
    root.title("Web2qr")
    root.geometry('500x500')

    # Creating qr code.
    queryURL = " ".join(sys.argv[1:]).strip().replace(' ', '+')
    URL = 'https://google.com/search?q=' + queryURL
    img = qrcode.make(URL)
    # type(img)
    img.save("qr.png")

    #Creating Image
    myImg = ImageTk.PhotoImage(Image.open("qr.png"))
    label = Label(root, image=myImg).pack()

    #Running window
    root.mainloop()

if __name__ == "__main__":
    main()
    # Remove png file
    if os.path.exists('qr.png'):
        os.remove('qr.png')