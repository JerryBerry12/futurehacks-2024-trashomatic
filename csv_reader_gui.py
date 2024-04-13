import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import tkmacosx
import datamanager

window = tk.Tk()
window.geometry("500x281")
window.configure(bg='blue')
window.title("Trash-o-Matic Mass Import")

def massimport():
    file1 = open(entry1.get(), 'r')
    count = 0

    for line in file1:
        line = line.rstrip()
        list = line.split(",")
        trash = list[0]
        number = list[1]
        trash = trash.lower()
        trash = trash.replace(" ", "_")
        if number == "1":
          textvalue = "compost"
        elif number == "2":
          textvalue = "bottles/cans"
        elif number == "3":
          textvalue = "paper"
        elif number == "4":
          textvalue = "trash"
        elif number == "5":
          textvalue = "plastic"
        else:
          messagebox.showerror("Error!", "Error while importing your data! Your csv file is most likely corrupted or misformatted.")
          entry1.delete(0, 'end')
        datamanager.save(trash, textvalue)
        count = count + 1

    successmessage = "Successfully imported " + str(count) + " pieces of trash!"
    messagebox.showinfo("Success!", successmessage)

img = ImageTk.PhotoImage(Image.open("images/PNGs/logo-150x150.png"))
imglabel = tk.Label(window, image=img)
imglabel.pack()
label1 = tk.Label(text="Please make sure your csv file is correctly formatted!", bg='blue', fg="white")
label1.pack()
label2 = tk.Label(text="This is an irreversable action!", bg='red', fg="white", font='Helvetica 18 bold')
label2.pack()
label3 = tk.Label(text="Enter the path to your csv file (full please):", bg='blue', fg='#ffffff')
label3.pack()
entry1 = tk.Entry(window, bg='blue', fg='white')
entry1.pack()
submitButton = tkmacosx.Button(window, text="Submit", command=massimport, bg='#0052cc', fg='#ffffff', borderless=1)
submitButton.pack()
window.mainloop()