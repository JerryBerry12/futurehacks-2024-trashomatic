import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import tkmacosx
import datamanager

window = tk.Tk()
window.geometry("500x225")
window.configure(bg='blue')
window.title("Trash-o-Matic")

def checkwheregoes():
    userinput = entry1.get()
    userinput = userinput.lower()
    userinput = userinput.replace(" ", "_")
    try:
        whereitgoes = datamanager.load(userinput)
        messagebox.showinfo("Found info!", "That piece of trash goes into: " + whereitgoes)
        entry1.delete(0, 'end')
    except KeyError:
        messagebox.showerror("Error!", "Sorry, I don't know where that goes. Please train me more, so that I can learn!")
        entry1.delete(0, 'end')




img = ImageTk.PhotoImage(Image.open("images/PNGs/logo-150x150.png"))
imglabel = tk.Label(window, image=img)
imglabel.pack()
label1 = tk.Label(text="Enter the name of a piece of trash:", bg='blue', fg="#ffffff")
label1.pack()
entry1 = tk.Entry(window, bg='blue', fg='white')
entry1.pack()
submitButton = tkmacosx.Button(window, text="Submit", command=checkwheregoes, bg='#0052cc', fg='#ffffff', borderless=1)
submitButton.pack()
window.mainloop()