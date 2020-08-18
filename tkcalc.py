from tkinter import *

class SimpleAddCal:
    def __init__(self, win):
        # Labels
        self.lbl1 = Label(win, text = 'NO:')
        self.lbl1.place(x = 100, y = 50)
        self.lbl2 = Label(win, text = 'NO:')
        self.lbl2.place(x = 100, y = 80)
        self.lbl3 = Label(win, text = '=')
        self.lbl3.place(x = 100, y = 200)
       # Entry
        self.t1 = Entry(bd = 3)
        self.t2 = Entry(bd = 3)
        self.t3 = Entry(bd = 10)

        self.t1.place(x = 200, y = 50)
        self.t2.place(x = 200, y = 80)
        self.t3.place(x = 200, y = 200)
        #buttons
        self.btn1 = Button(win, text = '+', command = self.add)
        self.btn2 = Button(win, text = '-', command = self.sub)
        self.btn3 = Button(win, text = 'x', command = self.multiply)
        self.btn4 = Button(win, text = '/', command = self.divide)
       
        self.btn1.place(x = 100, y = 150)
        self.btn2.place(x = 200, y = 150)
        self.btn3.place(x = 300, y = 150)
        self.btn4.place(x = 400, y = 150)

        #trigger addtion

    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

        #trigger subtract
    def sub(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))
    #trigger mutiply
    def multiply(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))
    #trigger division
    def divide(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 / num2
        self.t3.insert(END, str(result))
                



window = Tk()
mywin = SimpleAddCal(window)
window.title('FORTUNES calculator')
window.geometry('500x400+10+10')
window.config(bg='gray')
window.mainloop()