from tkinter import *
from tkinter import ttk
import sqlite3

class studentDB:

    # will hold a database connection
    db_conn = 0
    # A cursor is used to traverse the records of the result
    theCursor = 0
    # will store the current student selected
    curr_student = 0

    # setup the database
    def setup_db (self) :
        # open or create a database
        self.db_conn = sqlite3.connect('student.db')
        # the cursor is able to traverses the records
        self.theCursor = self.db_conn.cursor()
        # create the table if it doesnot exist
        try:
            self.db_conn.execute("CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL) ;")
            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("ERROR : Table not created")

     #submit button function
    def stud_submit(self):
        
        # insert the student in the database
        self.db_conn.execute("INSERT INTO Students (FName, LName) " + "VALUES ('" + self.fn_entry_value.get() + "', '" + self.ln_enrty_value.get() + "')")

        #clear the entry boxes
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        #update the list box with the student list
        self.update_listbox()

    def update_listbox(self):
        #delete items in the list box
        self.list_box.delete(0, END)
        
        # get student from the database
        try:
            result = self.theCursor.execute('SELECT ID, FName, LName FROM Students')
            for row in result:
                stud_id = row[0]
                stud_fname =row[1]
                stud_lname = row[2]

        # put the students in the list box
            self.list_box.insert(stud_id, stud_fname + " " + stud_lname)

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")
        except:
            print("1: couldn't Retrieve data from database")
        
        # load the listbox selected student into the entries(textbox)

    def load_student(self, event =None):
            #get index selected which is the student id
            lb_widget = event.widget
            index = str(lb_widget.curselection() [0] + 1)

            #store the current student index
            self.curr_student = index

            #retrieve the student list form the database
    try:
        result = self.theCursor.execute("SELECT ID, FName, LName FROM Students WHERE ID="  + index)

            #you will now recieve a list of list that hold the result
        for row in result:
            stud_id = row[0]
            stud_fname = row[1]
            stud_lname = row[2]
            
            #set value in the entries
            self.fn.entry_value.set(stud_fname)
            self.ln_entry_value.set(stud_lname)
        
    except sqlite3.OperationalError:
            print("The Table Doesn't Exist")
    except:
        print("2 : Couldn't Retrieve Data From Database")
        
        #update student info
        
    def update_student(self, event=None):
        #update student records with change made in entry
        try:
            self.db_conn.execute('UPDATE Students SET FName ='" + self.fn_entry_value.get() +"', LName='"self.ln_entry_value.get() + "' WHERE ID=" + self.curr_student)
            self.db_conn.commit()
        except sqlite3.OperationalError:
            print("Database couldn't be Updated")

        # clear entry box
        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")

        # reupdate the list box with student list
        self.update_listbox()




    def __init__(self, root):
        root.title('student management Database system')
        root.geometry("270x340")
        root.config(bg = 'blue')

    
        # Add widgets
        # first row
        fn_label = Label(root, text = 'First Name')
        fn_label.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = W) 

        self.fn_entry_value = StringVar(root, value = '')
        self.fn_entry = ttk.Entry(root, textvariable = self.fn_entry_value)
        self.fn_entry.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = W)

        # second row
        ln_label = Label(root, text = 'Second Name')
        ln_label.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = W) 

        self.ln_entry_value = StringVar(root, value = '')
        self.ln_entry = ttk.Entry(root, textvariable = self.ln_entry_value)
        self.ln_entry.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = W)

        # third row
        self.submit_botton = ttk.Button(root, text = 'Submit', command = lambda: self.stud_submit)
        self.submit_botton.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = W) 

        self.update_botton = ttk.Button(root, text = 'Update', command = lambda: self.update_student)
        self.update_botton.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = W) 

        # fourth row
        scrollbar = Scrollbar(root)
        self.list_box = Listbox(root)
        self.list_box.bind('<<Listboxselect>>', self.load_student)

        self.list_box.insert(1, 'students will appear Here')
        self.list_box.grid(row = 3, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = W+E) 

        # Call for the database to be created
        self.setup_db()


        # update the Listbox with student list
        self.update_listbox()




root = Tk()
studDB = studentDB(root)
root.mainloop()