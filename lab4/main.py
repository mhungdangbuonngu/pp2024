from output import *
import tkinter as tk
from tkinter import ttk
#gui 
window=tk.Tk()
window.title("super dupper doom")
window.geometry('340x440')

#ttk 
label=ttk.Label(window,text='student management ') 
label.pack()

inputButton=ttk.Button(window,text='input mark', command=inputMarkCmd)
inputButton.pack(ipadx=7,ipady=7)

countGpas=ttk.Button(window,text='count Gpa',command=countGpaCmd)
countGpas.pack(ipadx=7,ipady=7)

sortButton=ttk.Button(window, text='sort gpa', command=sortGpaCmd)      
sortButton.pack(ipadx=7,ipady=7)

showGButton=ttk.Button(window, text="show gpa",command=showGpaCmd)
showGButton.pack(ipadx=6,ipady=6)

showMButton=ttk.Button(window, text='show marks',command=showMarkCmd)
showMButton.pack(ipadx=6,ipady=6)


window.mainloop()
#endregion