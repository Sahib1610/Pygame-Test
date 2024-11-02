import sys
import tkinter as tk
import os

def sp():
    window.destroy()
    os.system(r"Singleplayer.py")

def mp():
    window.destroy()
    os.system(r"Multiplayer.py")

def Exit():
    sys.exit()

window = tk.Tk()
window.title("Main Menu")
window.geometry("800x600")
window.maxsize(800,600)

bg = tk.PhotoImage(file="Images/background.png")
single = tk.PhotoImage(file="Images/Single.png")
multi = tk.PhotoImage(file="Images/Multi.png")
QUIT = tk.PhotoImage(file="Images/logout.png")

canvas= tk.Canvas(window,width=800,height=600)
canvas.pack(fill="both",expand=False)
canvas.create_image(0,0,image=bg,anchor="nw")

title = canvas.create_text(400,100,text = "Main Menu", font=("Ariel",80),fill="DeepSkyBlue")

singleplayer= tk.Button(window,text="Single Player",font=("Blacklight",23),image=single,padx=20,compound=tk.LEFT,height=50,width=500,fg="SkyBlue",bg="RoyalBlue2",activebackground="Green",activeforeground="White",cursor="Hand1",command=sp)
singleplayer_canvas= canvas.create_window(400,200,anchor= "center",window=singleplayer)

multiplayer= tk.Button(window,text="Multi Player",font=("Blacklight",23),image=multi,padx=20,compound=tk.LEFT,height=50,width=500,fg="SkyBlue",bg="RoyalBlue2",activebackground="Green",activeforeground="White",cursor="Hand1",command=mp)
multiplayer_canvas= canvas.create_window(400,300,anchor= "center",window=multiplayer)

Quit =  tk.Button(window,text="Quit",font=("Blacklight",23),fg="SkyBlue",image=QUIT,padx=120,compound=tk.LEFT,height=50,width=300,bg="RoyalBlue2",activebackground="Red",activeforeground="White",cursor="Hand1",command=Exit)
Quit_canvas= canvas.create_window(400,400,anchor= "center",window=Quit)

tk.mainloop()