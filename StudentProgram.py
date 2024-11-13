from tkinter import *
import tkinter.ttk as ttk
import sqlite3
from tkcalendar import DateEntry
from tkinter import messagebox
import keyboard as k
import time

# Connect to the database
conn1 = sqlite3.connect('first.db')
table1 = conn1.cursor()
conn2 = sqlite3.connect('second.db')
table2 = conn2.cursor()
conn3 = sqlite3.connect('third.db')
table3 = conn3.cursor()
conn4 = sqlite3.connect('fourth.db')
table4 = conn4.cursor()

root = Tk()
root.title('Main')
root.geometry("1000x700")


def showData():
    # functions
    def addGroup():
        group_name = str(group_entry.get()).capitalize().strip()
        group_name1 = 'A' + group_name
        group_name2 = 'M' + group_name
        group_name3 = 'H' + group_name
        table1.execute(f'CREATE TABLE IF NOT EXISTS "{group_name}"  (\n'
                       f'	"Name"	TEXT,\n'
                       f'	"ID"	INTEGER NOT NULL UNIQUE,\n'
                       f'	"Grade"	INTEGER,\n'
                       f'	"Phone_Number"	TEXT,\n'
                       f'	"Parent_Phone_Number"	TEXT,\n'
                       f'	"Entry_Date"	TEXT,\n'
                       f'	PRIMARY KEY("ID" AUTOINCREMENT)\n'
                       f');')
        table2.execute(f'CREATE TABLE IF NOT EXISTS "{group_name1}" (\n'
                       f'	"Name"	TEXT,\n'
                       f'	"ID"	INTEGER NOT NULL UNIQUE ,\n'
                       f'	PRIMARY KEY("ID" AUTOINCREMENT)\n'
                       f');')
        table3.execute(f'CREATE TABLE IF NOT EXISTS "{group_name2}" (\n'
                       f'	"Name"	TEXT,\n'
                       f'	"ID"	INTEGER NOT NULL UNIQUE,\n'
                       f'	PRIMARY KEY("ID" AUTOINCREMENT)\n'
                       f');')
        table4.execute(f'CREATE TABLE IF NOT EXISTS "{group_name3}" (\n'
                       f'	"Name"	TEXT,\n'
                       f'	"ID"	INTEGER NOT NULL UNIQUE,\n'
                       f'	PRIMARY KEY("ID" AUTOINCREMENT)\n'
                       f');')
        group_entry.delete(0, END)
        conn1.commit()
        conn2.commit()
        conn3.commit()
        conn4.commit()
        table1.execute(f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        columnData = table1.fetchall()
        tableNames = []
        for i in range(len(columnData) - 1):
            tableNames.append(columnData[i][0])
        grade_combo2.configure(values=tableNames)
        grade_combo1.configure(values=tableNames)

    def updateStudent():
        name = str(name_entry.get())
        code = int(id_entry.get())
        number = str(number_entry.get())
        parent_number = str(parent_entry.get())
        date1 = str(date_entry.get())
        grade = int(grade_entry.get())
        x = str(grade_combo2.get())
        x1 = 'A' + str(x)
        x2 = 'M' + str(x)
        x3 = 'H' + str(x)
        table1.execute(
            f"UPDATE '{x}' SET Name = '{name}', `Phone_Number` = '{number}', Grade = {grade} , Parent_Phone_Number = '{parent_number}', Entry_Date='{date1}'  WHERE ID = {code}")
        table2.execute(f"UPDATE {x1} SET Name ='{name}' WHERE ID = {code}")
        table3.execute(f"UPDATE {x2} SET Name ='{name}' WHERE ID = {code}")
        table4.execute(f"UPDATE {x3} SET Name ='{name}' WHERE ID = {code}")
        conn1.commit()
        conn2.commit()
        conn3.commit()
        conn4.commit()
        searchData()
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        id_entry.delete(0, END)
        grade_combo2.delete(0, END)
        grade_entry.delete(0, END)
        parent_entry.delete(0, END)
        date_entry.delete(0, END)

    def addStudent():
        x = str(grade_combo2.get())
        x1 = 'A' + str(x)
        x2 = 'M' + str(x)
        x3 = 'H' + str(x)
        table1.execute(f"SELECT * FROM '{x}'")
        dataZ = table1.fetchall()
        if len(dataZ) == 0:
            name = str(name_entry.get())
            code = int(id_entry.get())
            number = int('0' + number_entry.get())
            parent_number = str(parent_entry.get())
            date1 = str(date_entry.get())
            grade = int(grade_entry.get())
            table1.execute(
                f"INSERT INTO '{x}' (Name, ID, Phone_Number, Grade, Parent_Phone_Number, Entry_Date) VALUES ('{name}', {code}, '{number}',{grade}, '{parent_number}', '{date1}')")
            table2.execute(f"INSERT INTO {x1} (Name, ID) VALUES ('{name}', {code})")
            table3.execute(f"INSERT INTO {x2} (Name, ID) VALUES ('{name}', {code})")
            table4.execute(f"INSERT INTO {x3} (Name, ID) VALUES ('{name}', {code})")
            conn1.commit()
            conn2.commit()
            conn3.commit()
            conn4.commit()
        else:
            name = str(name_entry.get())
            number = int('0' + number_entry.get())
            parent_number = str(parent_entry.get())
            date1 = str(date_entry.get())
            grade = int(grade_entry.get())
            table1.execute(
                f"INSERT INTO '{x}' (Name, Phone_Number, Grade ,Parent_Phone_Number, Entry_Date) VALUES ('{name}', '{number}',{grade},'{parent_number}', '{date1}')")
            table2.execute(f"INSERT INTO {x1} (Name) VALUES ('{name}')")
            table3.execute(f"INSERT INTO {x2} (Name) VALUES ('{name}')")
            table4.execute(f"INSERT INTO {x3} (Name) VALUES ('{name}')")
            conn1.commit()
            conn2.commit()
            conn3.commit()
            conn4.commit()

        table1.execute(f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        columnData = table1.fetchall()
        tableNames = []
        for i in range(len(columnData) - 1):
            tableNames.append(columnData[i][0])
        grade_combo2.configure(values=tableNames)
        grade_combo1.configure(values=tableNames)
        grade_combo2.delete(0, END)
        grade_combo1.delete(0, END)
        grade_combo1.insert(0, str(x))
        grade_combo2.insert(0, str(x))
        searchData()
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        id_entry.delete(0, END)
        grade_combo2.delete(0, END)
        grade_entry.delete(0, END)
        parent_entry.delete(0, END)
        date_entry.delete(0, END)

    def searchData():
        for item in tree.get_children():
            tree.delete(item)
        x = grade_combo1.get()
        grade_combo2.delete(0, END)
        grade_combo2.insert(0, x)
        table1.execute(f"SELECT * FROM '{x}' ORDER BY ID")
        data1 = table1.fetchall()
        count1 = 0
        for row1 in data1:
            if (count1 % 2) == 0:
                tree.insert(parent='', index='end', values=row1[0:], tags='evenRow')
            else:
                tree.insert(parent='', index='end', values=row1[0:], tags='oddRow')
            count1 += 1
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        id_entry.delete(0, END)
        grade_combo2.delete(0, END)
        grade_entry.delete(0, END)
        parent_entry.delete(0, END)
        date_entry.delete(0, END)

    def selectStudent(e):
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        id_entry.delete(0, END)
        grade_combo2.delete(0, END)
        grade_entry.delete(0, END)
        parent_entry.delete(0, END)
        date_entry.delete(0, END)
        selected = tree.focus()
        values = tree.item(selected, 'values')

        name_entry.insert(0, values[0])
        number_entry.insert(0, values[3])
        id_entry.insert(0, values[1])
        grade_combo2.insert(0, grade_combo1.get())
        grade_entry.insert(0, values[2])
        parent_entry.insert(0, values[4])
        date_entry.insert(0, values[5])

    def removeStudent():
        code = int(id_entry.get())
        name = str(name_entry.get())
        x = str(grade_combo2.get())
        x1 = 'A' + str(x)
        x2 = 'M' + str(x)
        x3 = 'H' + str(x)
        table1.execute(f"DELETE FROM '{x}' WHERE ID = {code} AND Name = '{name}'")
        table2.execute(f"DELETE FROM {x1} WHERE ID = {code}")
        table3.execute(f"DELETE FROM {x2} WHERE ID = {code}")
        table4.execute(f"DELETE FROM {x3} WHERE ID = {code}")
        grade_combo2.delete(0, END)
        grade_combo1.delete(0, END)
        grade_combo2.insert(0, str(x))
        grade_combo1.insert(0, str(x))
        conn1.commit()
        conn2.commit()
        conn3.commit()
        conn4.commit()
        searchData()
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        id_entry.delete(0, END)
        grade_combo2.delete(0, END)
        grade_entry.delete(0, END)
        parent_entry.delete(0, END)
        date_entry.delete(0, END)

    def empty():
        name_entry.delete(0, END)
        number_entry.delete(0, END)
        id_entry.delete(0, END)
        grade_combo2.delete(0, END)
        grade_entry.delete(0, END)
        parent_entry.delete(0, END)
        date_entry.delete(0, END)

    def exit1():
        conn1.commit()
        conn2.commit()
        conn3.commit()
        conn4.commit()
        window.destroy()

    # Create a window
    window = Tk()
    window.configure(bg="#1E2025")
    window.title("Student Data")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#F0F0F0", fieldbackground="#F0F0F0", foreground="black",
                    font=("Arial", 10))
    style.map("Custom.Treeview", background=[("selected", "#0078D7")])

    main_frame = LabelFrame(window, text="Table grade", background="#92A4B1", foreground="#1E2025")
    main_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    tree_frame = Frame(main_frame)
    tree_frame.pack(pady=10)
    # Create a TreeView widget
    tree = ttk.Treeview(tree_frame)
    grade_combo1 = ttk.Combobox(main_frame)
    grade_combo1.pack(side=BOTTOM, padx=10, pady=10)
    search_button = Button(main_frame, text="Search data", command=searchData)
    search_button.pack(side=BOTTOM, padx=10, pady=10)
    # Define the columns

    # Create a vertical scroll bar
    scrollbar = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar1 = ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=tree.xview)
    scrollbar1.pack(side=BOTTOM, fill=X)
    # Associate the scroll bar with the TreeView
    tree.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar.set, selectmode="extended",
                   style="Custom.Treeview")
    tree['columns'] = ('name', 'code_number', 'grade', 'number', 'parent_number', 'date')

    # Format the columns
    tree.column('#0', width=0, stretch=NO)
    tree.column('name', width=250)
    tree.column('code_number', width=100)
    tree.column('grade', width=100)
    tree.column('number', width=100)
    tree.column('parent_number', width=100)
    tree.column('date', width=100)

    # Set the headings
    tree.heading('#0', text='', anchor=CENTER)
    tree.heading('name', text='Name', anchor=CENTER)
    tree.heading('code_number', text='Code', anchor=CENTER)
    tree.heading('grade', text='Grade', anchor=CENTER)
    tree.heading('number', text='Phone Number', anchor=CENTER)
    tree.heading('parent_number', text='Parent Number', anchor=CENTER)
    tree.heading('date', text='Entry Date', anchor=CENTER)

    tree.tag_configure('oddRow', background="WHITE", foreground="#1E2025")
    tree.tag_configure('evenRow', background="#1E2025", foreground="WHITE")
    # Pack the TreeView and run the window
    tree.pack(side=LEFT, fill=BOTH, expand=True)

    newGroupFrame = LabelFrame(window, text='Add Group', background="#92A4B1", foreground="#1E2025")
    newGroupFrame.pack(fill=X, expand=YES, padx=20, pady=10)

    groupName = Label(newGroupFrame, text='Group Name',background="#92A4B1", foreground="#1E2025")
    groupName.grid(column=0, row=0, columnspan=2, pady=10, padx=5)

    group_entry = Entry(newGroupFrame)
    group_entry.grid(column=2, row=0, columnspan=2, pady=10, padx=5)

    groupButton = Button(newGroupFrame, text='Add Group', command=addGroup)
    groupButton.grid(column=4, row=0, columnspan=2, pady=10, padx=5)
    # entry box
    data_frame = LabelFrame(window, text="Record", bg="#92A4B1", foreground="#1E2025")
    data_frame.pack(fill=X, expand=YES, padx=20, pady=10)

    name_label = Label(data_frame, text="Name", bg="#92A4B1", foreground="#1E2025")
    name_label.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
    name_entry = Entry(data_frame)
    name_entry.grid(row=0, column=3, padx=20, pady=10, columnspan=2)

    id_label = Label(data_frame, text="ID", bg="#92A4B1", foreground="#1E2025")
    id_label.grid(row=0, column=5, padx=20, pady=10, columnspan=2)
    id_entry = Entry(data_frame)
    id_entry.grid(row=0, column=7, padx=20, pady=10, columnspan=2)

    grade_label = Label(data_frame, text="Grade", bg="#92A4B1", foreground="#1E2025")
    grade_label.grid(row=2, column=0, padx=20, pady=10, columnspan=2)
    grade_entry = Entry(data_frame)
    grade_entry.grid(row=2, column=3, padx=20, pady=10, columnspan=2)

    number_label = Label(data_frame, text="Phone Number", bg="#92A4B1", foreground="#1E2025")
    number_label.grid(row=2, column=5, padx=20, pady=10, columnspan=2)
    number_entry = Entry(data_frame)
    number_entry.grid(row=2, column=7, padx=20, pady=10, columnspan=2)

    chosenGrade_label = Label(data_frame, text="Choose group", bg="#92A4B1", foreground="#1E2025")
    chosenGrade_label.grid(row=0, column=9, padx=20, pady=10, columnspan=2)

    grade_combo2 = ttk.Combobox(data_frame)
    grade_combo2.grid(row=0, column=11, columnspan=2, padx=10, pady=10)

    parent_label = Label(data_frame, text='Parent Number', bg="#92A4B1", foreground="#1E2025")
    parent_label.grid(row=2, column=9, columnspan=2, padx=10, pady=10)

    parent_entry = Entry(data_frame)
    parent_entry.grid(row=2, column=11, columnspan=2, padx=10, pady=10)

    date_label = Label(data_frame, text='Entry Date', bg="#92A4B1", foreground="#1E2025")
    date_label.grid(row=2, column=13, columnspan=2, padx=10, pady=10)

    date_entry = DateEntry(data_frame)
    date_entry.grid(row=2, column=15, columnspan=2, padx=10, pady=10)
    date_entry.delete(0, END)

    button_frame = LabelFrame(window, text="Commands", background="#92A4B1", foreground="#1E2025")
    button_frame.pack(side=BOTTOM, pady=10, padx=20, fill=X, expand=YES)

    updateStudent_button = Button(button_frame, text="Update Student", command=updateStudent, background="WHITE",
                                  foreground="#1E2025")
    updateStudent_button.grid(row=0, column=1, columnspan=2, pady=10, padx=50)

    empty_button = Button(button_frame, text="Empty", command=empty, background="WHITE", foreground="#1E2025")
    empty_button.grid(row=0, column=5, columnspan=3, pady=10, padx=50)
    tree.bind("<ButtonRelease-1>", selectStudent)

    addStudent_button = Button(button_frame, text="Add Student", command=addStudent, background="WHITE",
                               foreground="#1E2025")
    addStudent_button.grid(row=0, column=3, columnspan=2, pady=10, padx=50)

    remove_button = Button(button_frame, text="Remove Student", command=removeStudent, background="WHITE",
                           foreground="#1E2025")
    remove_button.grid(row=0, column=8, columnspan=3, pady=10, padx=50)

    exit_button = Button(button_frame, text="Exit Window", command=exit1, background="WHITE", foreground="#1E2025")
    exit_button.grid(row=0, column=11, columnspan=2, pady=10, padx=50)
    table1.execute(f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    columnData = table1.fetchall()
    tableNames = []
    for i in range(len(columnData) - 1):
        tableNames.append(columnData[i][0])
    grade_combo2.configure(values=tableNames)
    grade_combo1.configure(values=tableNames)

    window.mainloop()

    # Close the connection to the database
    conn1.close()
    conn2.close()
    conn3.close()


def showQuizes():
    def selectStudent(e):
        code_entry.delete(0, END)
        selected = tree.focus()
        values = tree.item(selected, 'values')
        code_entry.insert(0, values[1])

    def updateQuiz():
        grade = str(grade_combo1.get())
        table1.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData = table1.fetchall()
        num = []
        for i in columnData:
            num.append(i[1])
        if str(search_combo.get()) in num:
            x = int(mark_entry.get())
            grade = str(grade_combo1.get())
            code = int(code_entry.get())
            table1.execute(f"UPDATE '{grade}' SET {str(search_combo.get())} = {x} WHERE ID = {code}")
            conn1.commit()
            searchData()
        mark_entry.delete(0, END)
        code_entry.delete(0, END)
        search_combo.delete(0, END)

    def searchData():
        grade = str(grade_combo1.get())
        # Create a TreeView widget
        global tree
        for item in tree.get_children():
            tree.delete(item)
        table1.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData = table1.fetchall()
        num = []
        for i in columnData:
            num.append(i[1])
        sort_combo.configure(values=num[6:])
        columns = num[0:3] + num[6:]
        tree['columns'] = tuple(columns)
        tree.column('#0', width=0)
        tree.heading('#0', text='', anchor=CENTER)
        # Format the columns
        for i in columns:
            tree.column(f"{i}", width=100)
            tree.heading(f"{i}", text=f"{i}", anchor=CENTER)

        # Create a vertical scroll bar

        # Associate the scroll bar with the TreeView
        tree.configure(yscrollcommand=scrollbar.set, selectmode="extended", style="Custom.Treeview")

        tree.tag_configure('oddRow', background="white")
        tree.tag_configure('evenRow', background="lightblue")
        if str(sort_combo.get()) == '0':
            select_query = f'''
             SELECT * FROM '{grade}';
            '''
        else:
            select_query = f'''
                         SELECT * FROM '{grade}' ORDER BY {str(sort_combo.get())} DESC;
                        '''

        table1.execute(select_query)
        data = table1.fetchall()
        count = 0
        for row in data:
            if (count % 2) == 0:
                tree.insert(parent='', index='end', values=row[0:3] + row[6:], tags='evenRow')
            else:
                tree.insert(parent='', index='end', values=row[0:3] + row[6:], tags='oddRow')
            count += 1
        # Pack the TreeView and run the window
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        search_combo.configure(values=num[6:])
        what_combo2.configure(values=num[6:])

    def addQuiz():
        grade = str(grade_combo2.get())
        table1.execute(f"SELECT NAME, ID FROM '{grade}'")
        data = table1.fetchall()
        quizName = str(name_entry.get()).capitalize()
        table1.execute(f"ALTER TABLE '{grade}' ADD COLUMN {quizName} INTEGER")
        quizWindow = Tk()
        quizWindow.title("Add Quiz")
        student_label = ttk.Label(quizWindow, font=("Helvetica", 12, "bold"))
        student_label.pack()
        student_entry = ttk.Entry(quizWindow)
        student_entry.pack()
        conn1.commit()

        def buttonPressed():
            global labelName
            global count
            table1.execute(f"UPDATE'{grade}' SET {quizName} = {int(student_entry.get())} WHERE ID = {(data[count][1])}")
            tree1.insert('', 'end', values=(data[count][0], int(student_entry.get())))
            conn1.commit()
            student_entry.delete(0, END)
            if count == len(data) - 1:
                quizWindow.destroy()
            else:
                count += 1
                labelName = str(f"Student name: {data[count][0]} with code: {data[count][1]}")
                student_label.config(text=labelName)
                conn1.commit()
            grade_combo2.delete(0, END)
            name_entry.delete(0, END)

        global count
        count = 0
        labelName = str(f"Student name: {data[count][0]} with code: {data[count][1]}")
        student_label.config(text=labelName)

        # Create a button to mark attendance
        mark_button = ttk.Button(quizWindow, text="Add marks", command=buttonPressed)
        mark_button.pack()

        # Create a treeview to display attendance records
        tree1 = ttk.Treeview(quizWindow, columns=("Student", "Mark"))
        tree1.column('#0', width=0)
        tree1.heading("Student", text="Student", anchor=CENTER)
        tree1.heading("#0", text="", anchor=CENTER)
        tree1.heading("Mark", text="Mark", anchor=CENTER)
        tree1.pack()

        quizWindow.mainloop()

    def sendData():
        group = str(what_combo.get())
        quiz1 = str(what_combo2.get())
        table1.execute(f"SELECT Name, ID, Parent_Phone_Number, {quiz1} FROM '{group}';")
        data2 = table1.fetchall()
        try:
            import pywhatkit
            import pyautogui
            pywhatkit.font = None
            pywhatkit.bg_color = None
            for i in data2:
                text = f"Hello\nلقد حصل الطالب صاحب الكود    علي درجة     في "
                pywhatkit.sendwhatmsg_instantly(f"+20+'{i[2]}'",
                                                f"Hello,\nI hope this message finds you well\n{i[0]} with code:{i[1]} has got {i[3]} in {quiz1}\n Thanks\nSincerely,\nHossam Mohamed",
                                                10, True, 2)
                pyautogui.click(1050, 950)
                time.sleep(1)
                k.press_and_release('enter')
            root.destroy()
            window.destroy()
        except Exception as e:
            error_msg = str(e)
            if "Error while connecting to the Internet" in e:
                print("There is an error")

    global window
    window = Tk()
    window.title("Student Data")
    window.configure(bg='#1E2025')
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#F0F0F0", fieldbackground="#F0F0F0", foreground="black",
                    font=("Arial", 10))
    style.map("Custom.Treeview", background=[("selected", "#0078D7")])
    main_frame = LabelFrame(window, text="Table grade", background="#92A4B1", foreground="#1E2025")
    main_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    global tree, tree_frame
    tree_frame = Frame(main_frame)
    tree_frame.pack(pady=10)
    tree = ttk.Treeview(tree_frame)
    tree.bind("<ButtonRelease-1>", selectStudent)
    scrollbar = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar1 = ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=tree.xview)
    scrollbar1.pack(side=BOTTOM, fill=X)
    tree.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar.set)
    search_button = Button(main_frame, text="Search data", command=searchData)
    search_button.pack(side=BOTTOM, padx=10, pady=10)
    grade_combo1 = ttk.Combobox(main_frame)
    grade_combo1.pack(side=BOTTOM, padx=10, pady=10)
    label1 = Label(main_frame, text='Choose group', background="#92A4B1", foreground="#1E2025")
    label1.pack(side=BOTTOM)
    sort_combo = ttk.Combobox(main_frame)
    sort_combo.pack(side=RIGHT, padx=10, pady=10)
    sort_combo.insert(0, '0')
    sort_label = Label(main_frame, text='Sort by', background="#92A4B1", foreground="#1E2025")
    sort_label.pack(side=RIGHT)
    whatsapp_frame = LabelFrame(window, text='Send Reports', background="#92A4B1", foreground="#1E2025")
    whatsapp_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    what_group = Label(whatsapp_frame, text='Choose group', background="#92A4B1", foreground="#1E2025")
    what_group.grid(row=0, columnspan=2, column=0, pady=10, padx=10)
    what_combo = ttk.Combobox(whatsapp_frame)
    what_combo2 = ttk.Combobox(whatsapp_frame)
    what_combo.grid(row=0, columnspan=2, column=2, pady=10, padx=10)
    what_combo2.grid(row=0, columnspan=2, column=4, pady=10, padx=10)
    what_button = Button(whatsapp_frame, text='Send', command=sendData)
    what_button.grid(row=0, columnspan=2, column=6, pady=10, padx=10)
    edit_frame = LabelFrame(window, text='Edit Quiz Mark', background="#92A4B1", foreground="#1E2025")
    edit_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    label2 = Label(edit_frame, text='Choose quiz',background="#92A4B1", foreground="#1E2025")
    label2.grid(row=0, columnspan=2, column=0, pady=10, padx=10)
    search_combo = ttk.Combobox(edit_frame)
    search_combo.grid(row=0, columnspan=2, column=2, pady=10, padx=10)
    code_label = Label(edit_frame, text='Student Code:', background="#92A4B1", foreground="#1E2025")
    code_label.grid(row=0, column=4, columnspan=1, padx=5, pady=10)
    code_entry = Entry(edit_frame)
    code_entry.grid(row=0, column=5, columnspan=2, pady=10, padx=5)
    mark_label = Label(edit_frame, text='New Mark:', background="#92A4B1", foreground="#1E2025")
    mark_label.grid(row=0, column=7, columnspan=1, padx=5, pady=10)
    mark_entry = Entry(edit_frame)
    mark_entry.grid(row=0, column=8, columnspan=2, pady=10, padx=5)
    update_button = Button(edit_frame, text='Update Quiz data', command=updateQuiz)
    update_button.grid(row=0, column=10, columnspan=2, padx=5, pady=10)
    quiz_frame = LabelFrame(window, text='Add Quiz', background="#92A4B1", foreground="#1E2025")
    quiz_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    label3 = Label(quiz_frame, text='Choose group', background="#92A4B1", foreground="#1E2025")
    label3.grid(row=0, columnspan=2, column=0, pady=10, padx=10)
    grade_combo2 = ttk.Combobox(quiz_frame)
    grade_combo2.grid(row=0, column=2, columnspan=2, pady=10, padx=5)
    addQuiz_button = Button(quiz_frame, text="Add Quiz", command=addQuiz)
    addQuiz_button.grid(column=10, row=0, columnspan=2, padx=20, pady=10)
    name_entry = Entry(quiz_frame)
    name_entry.grid(row=0, column=8, padx=10, pady=10, columnspan=2)
    name_label = Label(quiz_frame, text='Quiz Name', background="#92A4B1", foreground="#1E2025")
    name_label.grid(column=6, row=0, columnspan=2)
    table1.execute(f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    columnData = table1.fetchall()
    tableNames = []
    for i in range(len(columnData) - 1):
        tableNames.append(columnData[i][0])
    grade_combo1.configure(values=tableNames)
    grade_combo2.configure(values=tableNames)
    what_combo.configure(values=tableNames)


def showAttendance():
    def sendWhat():
        global grade, lectureName
        table1.execute(f"""SELECT Parent_Phone_Number FROM '{grade[1]}'""")
        dataN = table1.fetchall()
        table2.execute(f"""SELECT Name , ID, "{lectureName}" FROM {grade}""")
        dataM = table2.fetchall()
        try:
            import pywhatkit
            import pyautogui
            for i in range(len(dataM)):
                if str(dataM[i][2]).capitalize() == "Present":
                    pass
                else:
                    pywhatkit.sendwhatmsg_instantly(f"+20+'{dataM[i][0]}'",
                                                    f"Hello,\nI hope this message finds you well\n{dataM[i][0]} with code {dataM[i][1]} is absent from {lectureName}\nThanks\nSincerely,\nHossam Mohamed",
                                                    10)
                    pyautogui.click(1050, 950)
                    time.sleep(1)
                    k.press_and_release('enter')
            root.destroy()
            window.destroy()
        except Exception as e:
            error_msg = str(e)
            if "Error while connecting to the Internet" in e:
                print("There is an error")

    def selectStudent(e):
        grade = 'A' + str(grade_combo1.get())
        selected = tree.focus()
        values = tree.item(selected, 'values')
        state_entry.delete(0, END)
        code_entry.delete(0, END)
        search_combo.delete(0, END)
        code_entry.insert(0, values[1])
        table2.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData2 = table2.fetchall()
        num = []
        for i in columnData2:
            num.append(i[1])
        search_combo.configure(values=num[2:])

    def checkAttendance(group):
        table2.execute(f"""SELECT * FROM '{group}'""")
        data = table2.fetchall()
        if len(data[0]) > 5:
            for i in range(len(data)):
                if data[i][-1] == 'Absent' and data[i][-2] == 'Absent' and data[i][-3] == 'Absent':
                    messagebox.showerror(message=f"{data[i][0]} with code:{data[i][1]} has been absent 3 lectures")
                    break

    def searchData():
        grade = 'A' + str(grade_combo1.get())
        # Create a TreeView widget
        table2.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData2 = table2.fetchall()
        num = []
        for i in columnData2:
            num.append(i[1])
        search_combo.configure(values=num[2:])
        global tree
        for item in tree.get_children():
            tree.delete(item)
        table2.execute(f"PRAGMA table_info({grade})")
        # Define the columns
        columnData = table2.fetchall()
        num = []
        for i in columnData:
            num.append(i[1])
        tree['columns'] = tuple(num)
        tree.column('#0', width=0)
        tree.heading('#0', text='', anchor=CENTER)
        # Format the columns
        for i in range(len(num)):
            if i == 0:
                tree.column(f"{num[i]}", width=200)
                tree.heading(f"{num[i]}", text=f"{num[i]}", anchor=CENTER)
            else:
                tree.column(f"{num[i]}", width=150)
                tree.heading(f"{num[i]}", text=f"{num[i]}", anchor=CENTER)

        # Create a vertical scroll bar

        # Associate the scroll bar with the TreeView
        tree.configure(yscrollcommand=scrollbar.set, selectmode="extended", style="Custom.Treeview")

        tree.tag_configure('oddRow', background="WHITE", foreground="#1E2025")
        tree.tag_configure('evenRow', background="#1E2025", foreground="WHITE")
        select_query = f'''
                     SELECT * FROM {grade};
                    '''
        table2.execute(select_query)
        data = table2.fetchall()
        count = 0
        for row in data:
            if (count % 2) == 0:
                tree.insert(parent='', index='end', values=row[0:len(num)], tags='evenRow')
            else:
                tree.insert(parent='', index='end', values=row[0:len(num)], tags='oddRow')
            count += 1
        # Pack the TreeView and run the window
        tree.pack(side=LEFT, fill=BOTH, expand=True)

    def addAttendance():
        global grade, lectureName
        grade = 'A' + str(grade_combo2.get())
        table2.execute(f"SELECT NAME FROM {grade} ORDER BY ID ASC")
        data = table2.fetchall()
        lectureName = '(' + str(date_entry.get()) + ')'
        table2.execute(f"ALTER TABLE {grade} ADD COLUMN '{lectureName}' TEXT")
        attendanceWindow = Tk()
        attendanceWindow.title("Add Lecture")

        def update_attendance(student):
            attendance[student] = 'Present' if attendance[student] == 'Absent' else 'Absent'

        def allAttended():
            for i in range(len(data)):
                table2.execute(f"UPDATE {grade} SET '{lectureName}' ='Present' WHERE NAME ='{names[i]}'")
                conn2.commit()
            attendanceWindow.destroy()

        def mark_attendance():
            for student in attendance:
                state = 'Present' if attendance[student] == 'Present' else 'Absent'
                table2.execute(f"UPDATE {grade} SET '{lectureName}' = '{state}' WHERE NAME = '{student}'")
                conn2.commit()
            checkAttendance(grade)
            attendanceWindow.destroy()
            searchData()

        names = []
        for i in range(len(data)):
            names.append(data[i][0])
        attendance = {}
        for i, student in enumerate(names):
            attendance[student] = 'Absent'
        row = 0
        column = 0
        attendance_vars = {}
        for i, student in enumerate(names):
            checkbox = Checkbutton(attendanceWindow, text=student, font=("Helvetica", 10),
                                   command=lambda student=student: update_attendance(student))
            if (column == 8):
                column = 0
                row += 1
            checkbox.grid(row=row, column=column, columnspan=2, sticky="w")
            attendance_vars[student] = checkbox
            column += 2
        submit_button = Button(attendanceWindow, text="Submit", command=mark_attendance)
        submit_button.grid(row=row + 1, column=4, pady=10)
        save_button = Button(attendanceWindow, text='All attended', command=allAttended)
        save_button.grid(row=row + 1, column=5, pady=10)
        attendanceWindow.mainloop()

    def updateAttendance():
        grade = 'A' + str(grade_combo1.get())
        table2.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData = table2.fetchall()
        num = []
        for i in columnData:
            num.append(i[1])
        if str(search_combo.get()) in num:
            x = str(state_entry.get())
            grade = 'A' + str(grade_combo1.get())
            code = int(code_entry.get())
            table2.execute(f"""UPDATE '{grade}' SET "{str(search_combo.get())}" = '{x}' WHERE ID = {code}""")
            conn2.commit()
            searchData()
        state_entry.delete(0, END)
        search_combo.delete(0, END)
        code_entry.delete(0, END)
        search_combo.delete(0, END)

    window = Tk()
    window.title("Student Data")
    window.config(background="#1E2025")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#F0F0F0", fieldbackground="#F0F0F0", foreground="black",
                    font=("Arial", 10))
    style.map("Custom.Treeview", background=[("selected", "#0078D7")])
    main_frame = LabelFrame(window, text="Table grade", background="#92A4B1", foreground="#1E2025")
    main_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    global tree, tree_frame
    tree_frame = Frame(main_frame)
    tree_frame.pack(pady=10)
    tree = ttk.Treeview(tree_frame)
    tree.bind("<ButtonRelease-1>", selectStudent)
    scrollbar = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar1 = ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=tree.xview)
    scrollbar1.pack(side=BOTTOM, fill=X)
    tree.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar.set)
    grade_combo1 = ttk.Combobox(main_frame)
    grade_combo1.pack(side=BOTTOM, padx=10, pady=10)
    search_button = Button(main_frame, text="Search data", command=searchData)
    search_button.pack(side=BOTTOM, padx=10, pady=10)
    edit_frame = LabelFrame(window, text='Edit Attendance', background="#92A4B1", foreground="#1E2025")
    edit_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    group_label = Label(edit_frame, text='Choose lecture', background="#92A4B1", foreground="#1E2025")
    group_label.grid(column=0, row=0, columnspan=2, padx=5, pady=10)
    search_combo = ttk.Combobox(edit_frame)
    search_combo.grid(row=0, columnspan=2, column=2, pady=10, padx=10)
    code_label = Label(edit_frame, text='Student Code:', background="#92A4B1", foreground="#1E2025")
    code_label.grid(row=0, column=4, columnspan=1, padx=5, pady=10)
    code_entry = Entry(edit_frame)
    code_entry.grid(row=0, column=5, columnspan=2, pady=10, padx=5)
    state_label = Label(edit_frame, text='Attendance State:', background="#92A4B1", foreground="#1E2025")
    state_label.grid(row=0, column=7, columnspan=1, padx=5, pady=10)
    state_entry = Entry(edit_frame)
    state_entry.grid(row=0, column=8, columnspan=2, pady=10, padx=5)
    update_button = Button(edit_frame, text='Update Attendance Data', command=updateAttendance)
    update_button.grid(row=0, column=10, columnspan=2, padx=5, pady=10)
    button_frame = LabelFrame(window, text="Commands", background="#92A4B1", foreground="#1E2025")
    button_frame.pack(side=BOTTOM, pady=10, padx=20, fill=X, expand=YES)
    addQuiz_button = Button(button_frame, text="Add Lecture", command=addAttendance)
    addQuiz_button.grid(column=0, row=0, columnspan=2, padx=20, pady=10)
    group_label = Label(button_frame, text='Choose group',background="#92A4B1", foreground="#1E2025")
    group_label.grid(column=2, row=0, columnspan=2, padx=5, pady=10)
    grade_combo2 = ttk.Combobox(button_frame)
    grade_combo2.grid(column=4, row=0, columnspan=2, padx=5, pady=10)
    date_entry = DateEntry(button_frame)
    date_entry.grid(row=0, column=12, columnspan=2, padx=10, pady=10)
    date_label = Label(button_frame, text='Lecture Date', bg="#92A4B1", foreground="#1E2025")
    date_label.grid(row=0, column=10, columnspan=2, padx=10, pady=10)
    sendButton = Button(button_frame, text='Send Attendance Report', command=sendWhat)
    sendButton.grid(row=0, column=14, columnspan=2, padx=10, pady=10)
    table1.execute(f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    columnData = table1.fetchall()
    tableNames = []
    for i in range(len(columnData) - 1):
        tableNames.append(columnData[i][0])
    grade_combo2.configure(values=tableNames)
    grade_combo1.configure(values=tableNames)


def showMonth():
    def searchData():
        grade = 'M' + str(grade_combo1.get())
        # Create a TreeView widget
        global tree
        for item in tree.get_children():
            tree.delete(item)
        table3.execute(f"PRAGMA table_info({grade})")
        # Define the columns
        columnData = table3.fetchall()
        num = []
        for i in columnData:
            num.append(i[1])
        search_combo.configure(values=num[2:])
        tree['columns'] = tuple(num)
        tree.column('#0', width=0)
        tree.heading('#0', text='', anchor=CENTER)
        # Format the columns
        for i in range(len(num)):
            if i == 0:
                tree.column(f"{num[i]}", width=150)
                tree.heading(f"{num[i]}", text=f"{num[i]}", anchor=CENTER)
            else:
                tree.column(f"{num[i]}", width=100)
                tree.heading(f"{num[i]}", text=f"{num[i]}", anchor=CENTER)

        # Create a vertical scroll bar

        # Associate the scroll bar with the TreeView
        tree.configure(yscrollcommand=scrollbar.set, selectmode="extended", style="Custom.Treeview")

        tree.tag_configure('oddRow', background="#1E2025", foreground="WHITE")
        tree.tag_configure('evenRow', background="WHITE", foreground="#1E2025")
        select_query = f'''
                     SELECT * FROM {grade};
                    '''
        table3.execute(select_query)
        data = table3.fetchall()
        count = 0
        for row in data:
            if (count % 2) == 0:
                tree.insert(parent='', index='end', values=row[0:len(num)], tags='evenRow')
            else:
                tree.insert(parent='', index='end', values=row[0:len(num)], tags='oddRow')
            count += 1
        # Pack the TreeView and run the window
        tree.pack(side=LEFT, fill=BOTH, expand=True)

    def selectStudent(e):
        grade = 'M' + str(grade_combo1.get())
        selected = tree.focus()
        values = tree.item(selected, 'values')
        state_entry.delete(0, END)
        code_entry.delete(0, END)
        search_combo.delete(0, END)
        code_entry.insert(0, values[1])
        table3.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData2 = table3.fetchall()
        num = []
        for i in columnData2:
            num.append(i[1])
        search_combo.configure(values=num[2:])

    def addMonth():
        grade = 'M' + str(grade_combo2.get())
        table3.execute(f"SELECT NAME FROM {grade} ORDER BY ID ASC")
        data = table3.fetchall()
        monthName = str(name_entry.get())
        table3.execute(f"ALTER TABLE {grade} ADD COLUMN '{monthName}' TEXT")
        monthWindow = Tk()
        monthWindow.title("Add Month")

        def update_month(student):
            months[student] = 'Paid' if months[student] == 'Not Paid' else 'Not Paid'

        def allPaid():
            for i in range(len(data)):
                table3.execute(f"UPDATE {grade} SET '{monthName}' ='Paid' WHERE NAME ='{names[i]}'")
                conn3.commit()
            monthWindow.destroy()

        def mark_payments():
            for student in months:
                state = 'Paid' if months[student] == 'Paid' else 'Not Paid'
                table3.execute(f"UPDATE {grade} SET '{monthName}' = '{state}' WHERE NAME = '{student}'")
                conn3.commit()
            monthWindow.destroy()

        names = []
        for i in range(len(data)):
            names.append(data[i][0])
        months = {}
        for i, student in enumerate(names):
            months[student] = 'Not Paid'
        row = 0
        column = 0
        month_vars = {}
        for i, student in enumerate(names):
            checkbox = Checkbutton(monthWindow, text=student, font=("Helvetica", 10),
                                   command=lambda student=student: update_month(student))
            if column == 8:
                column = 0
                row += 1
            checkbox.grid(row=row, column=column, columnspan=2, sticky="w")
            month_vars[student] = checkbox
            column += 2
        submit_button = Button(monthWindow, text="Submit", command=mark_payments)
        submit_button.grid(row=row + 1, column=3, pady=10)
        save_button = Button(monthWindow, text='All attended', command=allPaid)
        save_button.grid(row=row + 1, column=1, pady=10)

        monthWindow.mainloop()

    def updateMonthData():
        grade = 'M' + str(grade_combo1.get())
        table3.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData = table3.fetchall()
        num = []
        for i in columnData:
            num.append(i[1])
        if str(search_combo.get()) in num:
            x = str(state_entry.get()).capitalize().strip()
            print(x)
            if x=='Paid' or x=='1':
                x='Paid'
            else:
                x='Not Paid'
            grade = 'M' + str(grade_combo1.get())
            code = int(code_entry.get())
            table3.execute(f"""UPDATE '{grade}' SET "{str(search_combo.get())}" = '{x}' WHERE ID = {code}""")
            conn3.commit()
            searchData()
        state_entry.delete(0, END)
        search_combo.delete(0, END)
        code_entry.delete(0, END)

    window = Tk()
    window.title("Student Data")
    window.configure(background="#1E2025")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#F0F0F0", fieldbackground="#F0F0F0", foreground="black",
                    font=("Arial", 10))
    style.map("Custom.Treeview", background=[("selected", "#0078D7")])
    main_frame = LabelFrame(window, text="Table grade", background="#92A4B1", foreground="#1E2025")
    main_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    global tree, tree_frame
    tree_frame = Frame(main_frame)
    tree_frame.pack(pady=10)
    tree = ttk.Treeview(tree_frame)
    tree.bind("<ButtonRelease-1>", selectStudent)
    scrollbar = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar1 = ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=tree.xview)
    scrollbar1.pack(side=BOTTOM, fill=X)
    tree.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar.set)
    table1.execute(f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    columnData = table1.fetchall()
    tableNames = []
    for i in range(len(columnData) - 1):
        tableNames.append(columnData[i][0])
    grade_combo1 = ttk.Combobox(main_frame, values=tableNames)
    grade_combo1.pack(side=BOTTOM, padx=10, pady=10)
    search_button = Button(main_frame, text="Search data", command=searchData)
    search_button.pack(side=BOTTOM, padx=10, pady=10)
    edit_frame = LabelFrame(window, text='Edit Month Data', background="#92A4B1", foreground="#1E2025")
    edit_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    label1 = Label(edit_frame, text='Choose Month',background="#92A4B1", foreground="#1E2025")
    label1.grid(row=0, columnspan=2, column=0, pady=10, padx=10)
    search_combo = ttk.Combobox(edit_frame)
    search_combo.grid(row=0, columnspan=2, column=2, pady=10, padx=10)
    code_label = Label(edit_frame, text='Student Code:', background="#92A4B1", foreground="#1E2025")
    code_label.grid(row=0, column=4, columnspan=1, padx=5, pady=10)
    code_entry = Entry(edit_frame)
    code_entry.grid(row=0, column=5, columnspan=2, pady=10, padx=5)
    state_label = Label(edit_frame, text='Month State:', background="#92A4B1", foreground="#1E2025")
    state_label.grid(row=0, column=7, columnspan=1, padx=5, pady=10)
    state_entry = Entry(edit_frame)
    state_entry.grid(row=0, column=8, columnspan=2, pady=10, padx=5)
    update_button = Button(edit_frame, text='Update Month Data', command=updateMonthData)
    update_button.grid(row=0, column=10, columnspan=2, padx=5, pady=10)
    button_frame = LabelFrame(window, text="Commands", background="#92A4B1", foreground="#1E2025")
    button_frame.pack(side=BOTTOM, pady=10, padx=20, fill=X, expand=YES)
    addQuiz_button = Button(button_frame, text="Add Month", command=addMonth)
    addQuiz_button.grid(column=8, row=0, columnspan=2, padx=20, pady=10)
    grade_combo2 = ttk.Combobox(button_frame, values=tableNames)
    grade_combo2.grid(column=2, row=0, columnspan=2, padx=10, pady=10)
    name_entry = Entry(button_frame)
    name_entry.grid(column=6, row=0, columnspan=2, padx=10, pady=10)
    name_label = Label(button_frame, text="Month Name", background="#92A4B1", foreground="#1E2025")
    name_label.grid(column=4, row=0, columnspan=2, padx=10, pady=10)
    name2_label = Label(button_frame, text="Choose grade", background="#92A4B1", foreground="#1E2025")
    name2_label.grid(column=0, row=0, columnspan=2, padx=5, pady=10)
    window.mainloop()


def showHomework():
    def sendWhat():
        global grade, lectureName
        grade = 'H' + str(grade_combo1.get())
        lectureName = str('(' + str(date_entry.get()) + ')')
        table1.execute(f"""SELECT Parent_Phone_Number FROM '{grade[1:]}'""")
        dataN = table1.fetchall()
        table4.execute(f"""SELECT Name , ID, "{lectureName}" FROM {grade}""")
        dataM = table4.fetchall()
        try:
            import pywhatkit
            import pyautogui
            for i in range(len(dataM)):
                if str(dataM[i][2]).capitalize() == "Present":
                    pass
                else:
                    pywhatkit.sendwhatmsg_instantly(f"+20+'{dataM[i][0]}'",
                                                    f"Hello,\nI hope this message finds you well\n{dataM[i][0]} with code {dataM[i][1]} is absent from {lectureName}\nThanks\nSincerely,\nHossam Mohamed",
                                                    10)
                    pyautogui.click(1050, 950)
                    time.sleep(1)
                    k.press_and_release('enter')
            window.destroy()
        except Exception as e:
            error_msg = str(e)
            if "Error while connecting to the Internet" in e:
                print("There is an error")

    def selectStudent(e):
        grade = 'H' + str(grade_combo1.get())
        selected = tree.focus()
        values = tree.item(selected, 'values')
        code_entry.delete(0, END)
        search_combo.delete(0, END)
        code_entry.insert(0, values[1])
        table4.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData2 = table4.fetchall()
        num = []
        for i in columnData2:
            num.append(i[1])
        search_combo.configure(values=num[2:])

    def searchData():
        grade = 'H' + str(grade_combo1.get())
        # Create a TreeView widget
        table4.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData2 = table4.fetchall()
        num = []
        for i in columnData2:
            num.append(i[1])
        search_combo.configure(values=num[2:])
        global tree
        for item in tree.get_children():
            tree.delete(item)
        table4.execute(f"PRAGMA table_info({grade})")
        # Define the columns
        columnData = table4.fetchall()
        num = []
        for i in columnData:
            num.append(i[1])
        tree['columns'] = tuple(num)
        tree.column('#0', width=0)
        tree.heading('#0', text='', anchor=CENTER)
        # Format the columns
        for i in range(len(num)):
            if i == 0:
                tree.column(f"{num[i]}", width=200)
                tree.heading(f"{num[i]}", text=f"{num[i]}", anchor=CENTER)
            else:
                tree.column(f"{num[i]}", width=150)
                tree.heading(f"{num[i]}", text=f"{num[i]}", anchor=CENTER)

        # Create a vertical scroll bar

        # Associate the scroll bar with the TreeView
        tree.configure(yscrollcommand=scrollbar.set, selectmode="extended", style="Custom.Treeview")

        tree.tag_configure('oddRow', background="WHITE", foreground="#1E2025")
        tree.tag_configure('evenRow', background="#1E2025", foreground="WHITE")
        select_query = f'''
                     SELECT * FROM {grade};
                    '''
        table4.execute(select_query)
        data = table4.fetchall()
        count = 0
        for row in data:
            if (count % 2) == 0:
                tree.insert(parent='', index='end', values=row[0:len(num)], tags='evenRow')
            else:
                tree.insert(parent='', index='end', values=row[0:len(num)], tags='oddRow')
            count += 1
        # Pack the TreeView and run the window
        tree.pack(side=LEFT, fill=BOTH, expand=True)

    def addHomework():
        global grade, lectureName
        grade = 'H' + str(grade_combo2.get())
        table4.execute(f"SELECT NAME FROM {grade} ORDER BY ID ASC")
        data = table4.fetchall()
        lectureName = str('(' + str(date_entry.get()) + ')')
        table4.execute(f"ALTER TABLE '{grade}' ADD COLUMN '{lectureName}' INTEGER")
        homeworkWindow = Tk()
        homeworkWindow.title("Add Homework")
        names = []
        for i in range(len(data)):
            names.append(data[i][0])
        homework = {}
        row = 0
        col = 0
        scales = []
        for i, student in enumerate(names):
            frame = Frame(homeworkWindow)
            frame.grid(row=row, column=col)
            label = Label(frame, text=student)
            label.grid(row=0, column=0)
            scale = Scale(frame, from_=0, to=10, length=150, orient=HORIZONTAL)
            scale.grid(row=0, column=1)
            scales.append(scale)
            if col == 4:
                col = 0
                row += 1
            else:
                col += 1
        print(lectureName)

        def submitHomework():
            grades = []
            for scaleZ in scales:
                gradeZ = int(scaleZ.get())
                grades.append(gradeZ)
            for i in range(len(names)):
                print(f"{grade}, {lectureName}, {grades[i]}, {names[i]}")
                table4.execute(f"""UPDATE '{grade}' SET "{lectureName}" = {grades[i]} WHERE Name = '{names[i]}' """)
                conn4.commit()

        submit_button = Button(homeworkWindow, text='Submit', command=submitHomework)
        submit_button.grid(row=row + 1, column=int(col / 2))

        homeworkWindow.mainloop()

    def updateHomework():
        grade = 'H' + str(grade_combo1.get())
        table4.execute(f"PRAGMA table_info('{grade}')")
        # Define the columns
        columnData = table4.fetchall()
        num = []
        for i in columnData:
            num.append(i[1])
        print(num)
        if str(search_combo.get()) in num:
            x = str(state_entry.get())
            grade = 'H' + str(grade_combo1.get())
            code = int(code_entry.get())
            table4.execute(f"""UPDATE '{grade}' SET "{str(search_combo.get())}" = '{x}' WHERE ID = {code}""")
            conn4.commit()
            searchData()
        search_combo.delete(0, END)
        code_entry.delete(0, END)
        search_combo.delete(0, END)

    window = Tk()
    window.title("Student Data")
    window.config(background="#1E2025")
    style = ttk.Style()
    style.configure("Custom.Treeview", background="#F0F0F0", fieldbackground="#F0F0F0", foreground="black",
                    font=("Arial", 10))
    style.map("Custom.Treeview", background=[("selected", "#0078D7")])
    main_frame = LabelFrame(window, text="Table grade", background="#92A4B1", foreground="#1E2025")
    main_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    global tree, tree_frame
    tree_frame = Frame(main_frame)
    tree_frame.pack(pady=10)
    tree = ttk.Treeview(tree_frame)
    tree.bind("<ButtonRelease-1>", selectStudent)
    scrollbar = ttk.Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar1 = ttk.Scrollbar(tree_frame, orient=HORIZONTAL, command=tree.xview)
    scrollbar1.pack(side=BOTTOM, fill=X)
    tree.configure(xscrollcommand=scrollbar1.set, yscrollcommand=scrollbar.set)
    grade_combo1 = ttk.Combobox(main_frame)
    grade_combo1.pack(side=BOTTOM, padx=10, pady=10)
    search_button = Button(main_frame, text="Search data", command=searchData)
    search_button.pack(side=BOTTOM, padx=10, pady=10)
    edit_frame = LabelFrame(window, text='Edit Homework', background="#92A4B1", foreground="#1E2025")
    edit_frame.pack(fill=X, expand=YES, padx=20, pady=20)
    name2_label = Label(edit_frame, text='Choose Homework', background="#92A4B1", foreground="#1E2025")
    name2_label.grid(row=0, columnspan=2, column=0, pady=10, padx=5)
    search_combo = ttk.Combobox(edit_frame)
    search_combo.grid(row=0, columnspan=2, column=2, pady=10, padx=5)
    code_label = Label(edit_frame, text='Student Code:', background="#92A4B1", foreground="#1E2025")
    code_label.grid(row=0, column=4, columnspan=1, padx=5, pady=10)
    code_entry = Entry(edit_frame)
    code_entry.grid(row=0, column=5, columnspan=2, pady=10, padx=5)
    state_label = Label(edit_frame, text='Homework State:', background="#92A4B1", foreground="#1E2025")
    state_label.grid(row=0, column=7, columnspan=1, padx=5, pady=10)
    state_entry = Scale(edit_frame, from_=0, to=10, length=150, orient=HORIZONTAL)
    state_entry.grid(row=0, column=8, pady=10, padx=5)
    update_button = Button(edit_frame, text='Update Homework Data', command=updateHomework)
    update_button.grid(row=0, column=9, columnspan=2, padx=5, pady=10)
    button_frame = LabelFrame(window, text="Commands", background="#92A4B1", foreground="#1E2025")
    button_frame.pack(side=BOTTOM, pady=10, padx=20, fill=X, expand=YES)
    addQuiz_button = Button(button_frame, text="Add Homework", command=addHomework)
    addQuiz_button.grid(column=0, row=0, columnspan=2, padx=20, pady=10)
    group_label = Label(button_frame, text='Choose group', background="#92A4B1", foreground="#1E2025")
    group_label.grid(column=2, row=0, columnspan=2, padx=5, pady=10)
    grade_combo2 = ttk.Combobox(button_frame)
    grade_combo2.grid(column=4, row=0, columnspan=2, padx=5, pady=10)
    date_entry = DateEntry(button_frame)
    date_entry.grid(row=0, column=8, columnspan=2, padx=10, pady=10)
    date_label = Label(button_frame, text='Lecture Date', bg="#92A4B1", foreground="#1E2025")
    date_label.grid(row=0, column=6, columnspan=2, padx=10, pady=10)
    sendButton = Button(button_frame, text='Send Homework Report', command=sendWhat)
    sendButton.grid(row=0, column=10, columnspan=2, padx=10, pady=10)
    table1.execute(f"SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    columnData = table1.fetchall()
    tableNames = []
    for i in range(len(columnData) - 1):
        tableNames.append(columnData[i][0])
    grade_combo2.configure(values=tableNames)
    grade_combo1.configure(values=tableNames)
    grade = 'H' + str(grade_combo1.get())
    window.mainloop()


window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
mainLabel = Label(root, text="Hossam Mohamed\nMaths Teacher", font=("Helvetica", 18, "bold"), borderwidth=2,
                  anchor=CENTER,
                  bg="#1E2025", fg='#92A4B1')

studentButton = Button(root, text='Student Data', pady=10, padx=20, command=showData, height=3, width=20, bg='#92A4B1',
                       fg="#1E2025", font=11)

quizButton = Button(root, text='Quizes Data', pady=10, padx=20, command=showQuizes, height=3, width=20, bg='#92A4B1',
                    fg="#1E2025", font=11)

attendanceButton = Button(root, text='Attendance', pady=10, padx=20, command=showAttendance, height=3, width=20,
                          bg='#92A4B1', fg="#1E2025", font=11)

monthButton = Button(root, text='Month Subscription', pady=10, padx=20, command=showMonth, height=3, width=20,
                     bg='#92A4B1', fg="#1E2025", font=11)
homeworkButton = Button(root, text='Homework', pady=10, padx=20, command=showHomework, height=3, width=20,
                        bg='#92A4B1', fg="#1E2025", font=11)
root.configure(bg='#1E2025')
mainLabel.pack(pady=20)
studentButton.pack(side=TOP, padx=10)
quizButton.pack(side=TOP, padx=10)
attendanceButton.pack(side=TOP, padx=10)
monthButton.pack(side=TOP, padx=10)
homeworkButton.pack(side=TOP, padx=10)
root.mainloop()
