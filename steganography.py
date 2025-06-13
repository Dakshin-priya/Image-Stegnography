import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import os
from stegano import lsb
window=tkinter.Tk()
#icon
window.iconbitmap(r"C:/Users/admin/Downloads/favicon (5).ico")
#window size
window.geometry("1366x738")
#window title
window.title("Steganography")
#window.config(bg="#CACAFF")
# Create a photoimage object of the image in the path
image1 = Image.open(r"C:\Users\admin\Downloads\favicon (4).ico")
#r"C:\Users\admin\Downloads\shield.png"
test = ImageTk.PhotoImage(image1)

label1 = tkinter.Label(image=test)
label1.image = test

# Position image
label1.place(x=510, y=100)
#label
h=Label(window,text="Steganography",font=("times",28,"bold"))
h.place(x=570,y=110)


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


center(window)
 
def uploadimage():
    # to minimize window
    window.iconify()
    def showimage():
        n3=Toplevel(n2)

        n3.iconbitmap(r"C:/Users/admin/Downloads/favicon (5).ico")
        image1 = Image.open(r"C:\Users\admin\Downloads\favicon (4).ico")
        #r"C:\Users\admin\Downloads\shield.png"
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(n3,image=test)
        label1.image = test
        # Position image
        label1.place(x=510, y=100)
        h=Label(n3,text="Steganography",font=("times",28,"bold"))
        h.place(x=570,y=110)
        #window size
        n3.geometry("1366x738")
        #window title
        n3.title("Steganography")
        
        def hide():
            global secret
            message=text1.get(1.0,END)
            secret=lsb.hide(str(filename),message)
            messagebox.showinfo("steganography","Data hidden successfully")

        def save():
            secret.save("hidden.png")
            messagebox.showinfo("steganography","image saved successfully")

        
        global filename
        # to select image
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG file","*.png"),("JPG File","*.jpg"),("All file","*.txt")))

        #first frame
        f1=Frame(n3,bd=3,bg="white",width=340,height=280,relief=GROOVE)
        f1.place(x=350,y=200)

        l=Label(f1,bg="white")
        l.place(x=40,y=10)
        #to display image
        my_img = Image.open(filename)
        new_image = my_img.resize((340,270))
        img = ImageTk.PhotoImage(new_image)
        board = Label(f1, image=img)
        board.image = img
        board.place(x=0,y=0)

        #second frame
        f2=Frame(n3,bd=3,width=340,height=280,bg="white",relief=GROOVE)
        f2.place(x=700,y=200)
        #x=350 y=80
        text1=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
        text1.place(x=0,y=0,width=660,height=295)

        #scroll bar
        y=Scrollbar(f2,orient=VERTICAL)
        y.place(x=900,y=0,height=300)
        y.config(command=text1.yview)
        text1.configure(yscrollcommand=y.set)

        #third frame
        f3=Frame(n3,bd=3,bg="gray",width=690,height=100,relief=GROOVE)
        f3.place(x=350,y=500)

        Button(f3,text="Hide Data",width=10,height=2,font="arial 14 bold",command=hide).place(x=190,y=20)
        Button(f3,text="Save Image",width=10,height=2,font="arial 14 bold",command=save).place(x=360,y=20)



        label1 = Label(f2,image=test,width=250,height=250)
        label1.image = test
        
    n2=Toplevel(window)
    n2.iconbitmap(r"C:/Users/admin/Downloads/favicon (5).ico")
    image1 = Image.open(r"C:\Users\admin\Downloads\favicon (4).ico")
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(n2,image=test)
    label1.image = test
    # Position image
    label1.place(x=510, y=100)
    h=Label(n2,text="Steganography",font=("times",28,"bold"))
    h.place(x=570,y=110)
    #window size
    n2.geometry("1366x738")
    #window title
    n2.title("Steganography")
    img=Button(n2,text="Upload Image",bg="gray",fg="black",padx=10,pady=10
               ,font=("times",20,"bold"),activebackground="black",activeforeground="gray",command=showimage)
    img.place(x=578,y=250)
    

#encode button
encode=Button(window,text="Encode",bg="gray",fg="black",padx=10,pady=10,font=("times",20,"bold"),
              activebackground="black",activeforeground="gray",command=uploadimage)
encode.place(x=635,y=200)
def decodeimg():
    window.iconify()
    def showimage():
        n5=Toplevel(n4)
        n5.iconbitmap(r"C:/Users/admin/Downloads/favicon (5).ico")
        image1 = Image.open(r"C:\Users\admin\Downloads\favicon (4).ico")
        test = ImageTk.PhotoImage(image1)

        label1 = tkinter.Label(n5,image=test)
        label1.image = test
        # Position image
        label1.place(x=510, y=100)
        h=Label(n5,text="Steganography",font=("times",28,"bold"))
        h.place(x=570,y=110)
        #window size
        n5.geometry("1366x738")
        #window title
        n5.title("Steganography")
        def show():
            clear_message=lsb.reveal(filename)
            text1.delete(1.0,END)
            text1.insert(END,clear_message)
        
        global filename
        #to select image
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select Image File',filetype=(("PNG file","*.png"),("JPG File","*.jpg"),("All file","*.txt")))

        img=Image.open(filename)
        test = ImageTk.PhotoImage(img)
        
        #first frame
        f1=Frame(n5,bd=3,bg="white",width=340,height=280,relief=GROOVE)
        f1.place(x=350,y=200)

        l=Label(f1,bg="white")
        l.place(x=40,y=10)
        
        #to display image
        my_img = Image.open(filename)
        new_image = my_img.resize((340,270))
        img = ImageTk.PhotoImage(new_image)
        board = Label(f1, image=img)
        board.image = img
        board.place(x=0,y=0)

        #second frame
        f2=Frame(n5,bd=3,width=340,height=280,bg="white",relief=GROOVE)
        f2.place(x=700,y=200)
        text1=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
        text1.place(x=0,y=0,width=660,height=295)

        #scroll bar
        y=Scrollbar(f2,orient=VERTICAL)
        y.place(x=660,y=0,height=300)
        y.config(command=text1.yview)
        text1.configure(yscrollcommand=y.set)

        #third frame
        f3=Frame(n5,bd=3,bg="gray",width=690,height=100,relief=GROOVE)
        f3.place(x=350,y=500)

        Button(f3,text="Show Data",width=10,height=2,font="arial 14 bold",command=show).place(x=255,y=20)
        label1 = Label(f2,image=test,width=250,height=250)
        label1.image = test
     
    
    n4=Toplevel(window)
    n4.iconbitmap(r"C:/Users/admin/Downloads/favicon (5).ico")
    image1 = Image.open(r"C:\Users\admin\Downloads\favicon (4).ico")
    test = ImageTk.PhotoImage(image1)

    label1 = tkinter.Label(n4,image=test)
    label1.image = test
    # Position image
    label1.place(x=510, y=100)
    h=Label(n4,text="Steganography",font=("times",28,"bold"))
    h.place(x=570,y=110)
    #window size
    n4.geometry("1366x738")
    #window title
    n4.title("Steganography")

    i=Button(n4,text="Upload Image",bg="gray",fg="black",padx=10,pady=10,font=("times",20,"bold"),activebackground="black",activeforeground="gray",command=showimage)
    i.place(x=578,y=250)
        
#decode button
decode=Button(window,text="Decode",bg="gray",fg="black",padx=10,pady=10,font=("times",20,"bold"),
              activebackground="black",activeforeground="gray",command=decodeimg)
decode.place(x=635,y=300)

window.mainloop()
