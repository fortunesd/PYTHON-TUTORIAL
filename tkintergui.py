# tkinter is a graphical user interface for python. its a standard python interface

# how oto create an application using tkinter

'''
1. import the module - tkinter
2. create the main window(conatanier)
3. add any number of widgets in the main window
4. apply the event trigger on the widgets
'''

from tkinter import *

window = Tk()

#add widgets there 
#button widgets
btn = Button(window, text = 'This is a button widget', fg = 'green')
btn.place(x = 0, y = 10)
#label widgets
lbl = Label(window, text = 'This is a label widget', fg = 'red', font = ('Helvetica',16))
lbl.place(x = 0, y = 30)

#entry widgets
txtfld = Entry(window, text = 'this is an entry widget', fg = 'black', bd = 5)
txtfld.place(x = 0, y = 60)


window.title('welcome to Tclassified.com ICT center')
window.geometry('400x300+10+20')
window.config(bg='skyblue')
window.mainloop()


