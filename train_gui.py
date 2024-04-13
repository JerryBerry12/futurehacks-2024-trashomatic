import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import tkmacosx
import datamanager

window = tk.Tk()
window.geometry("500x360")
window.configure(bg='blue')
window.title("Trash-o-Matic Trainer")
window.iconbitmap("images/trashcan.ico")

def savedata():
    userinput = entry1.get()
    userinput = userinput.lower()
    userinput = userinput.replace(" ", "_")
    userinput2 = entry2.get()
    if userinput2 == "1":
        datamanager.save(userinput, "compost")
        messagebox.showinfo("Success!", "Successfully saved to database!")
    elif userinput2 == "2":
        datamanager.save(userinput, "bottles/cans")
        messagebox.showinfo("Success!", "Successfully saved to database!")
    elif userinput2 == "3":
        datamanager.save(userinput, "paper")
        messagebox.showinfo("Success!", "Successfully saved to database!")
    elif userinput2 == "4":
        datamanager.save(userinput, "trash")
        messagebox.showinfo("Success!", "Successfully saved to database!")
    elif userinput2 == "5":
        datamanager.save(userinput, "plastic")
        messagebox.showinfo("Success!", "Successfully saved to database!")

img = ImageTk.PhotoImage(Image.open("images/PNGs/logo-150x150.png"))
imglabel = tk.Label(window, image=img)
imglabel.pack()

label1 = tk.Label(text="Enter the name of a piece of trash:", bg='blue', fg="#ffffff")
label1.pack()

entry1 = tk.Entry(window, bg='blue', fg='white')
entry1.pack()

label2 = tk.Label(text="Enter the number of where it goes:\n1 = compost\n2 = bottles/cans\n3 = paper\n4 = trash\n5 = plastic\n", bg='blue', fg="#ffffff")
label2.pack()

entry2 = tk.Entry(window, bg='blue', fg='white')
entry2.pack()

submitButton = tkmacosx.Button(window, text="Submit", command=savedata, bg='#0052cc', fg='#ffffff', borderless=1)
submitButton.pack()

window.mainloop()