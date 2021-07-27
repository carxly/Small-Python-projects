# ROCK PAPER SCISSCORS
from tkinter import * 
from tkinter.ttk import *

window = Tk()
window.title('Rock! Paper! Scissors!')
window.geometry('600x400')
greeting = Label(window, text='Rock, paper or scissors..??')
greeting.grid(column=1, row=0)

button1 = Button(window, text='ROCK')
button1.grid(column=0, row=2)
button2 = Button(window, text='PAPER')
button2.grid(column=1, row=2)
button3 = Button(window, text='SCISSORS')
button3.grid(column=2, row=2)

info = Label(window, text='Choose your weapon..')
info.grid(column=1, row=4)

window.mainloop()