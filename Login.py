from tkinter import *
from tkinter import messagebox
import sqlite3
import hashlib, uuid

a = (open('highscore.txt', 'r'))
con = sqlite3.connect('playerdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
                    name text, 
                    email text, 
                    age number, 
                    gender text,
                    highscore varString,
                    password Varstring
                )
            ''')
con.commit()

            
ws = Tk()
ws.title('Login- Space_Invaders')
ws.geometry('940x500')
ws.config(bg='#0B5A81')

f = ('Times', 14)
##salt = "5gz"
##salt = uuid.uuid4().hex


def insert_record():
    check_counter=0
    warn = ""
    if register_name.get() == "":
       warn = "Name can't be empty"
    else:
        check_counter += 1
        
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1

    if register_age.get() == "":
       warn = "Age can't be empty"
    else:
        check_counter += 1
    
    if  var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1

    if check_counter == 7:        
        try:
            con = sqlite3.connect('playerdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (:name, :email, :age, :gender, :highscore, :password)", {
                            'name': register_name.get(),
                            'email': register_email.get(),
                            'age': register_age.get(),
                            'gender': var.get(),
                            'highscore': '0',
                            'password': h.hexdigest()

            })
            con.commit()
            messagebox.showinfo('confirmation', 'Record Saved')

        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)

def login_response():
    try:
        con = sqlite3.connect('playerdata.db')
        c = con.cursor()
        for row in c.execute("Select * from record"):
            username = row[1]
            pwd = row[5]
        
    except Exception as ep:
        messagebox.showerror('', ep)

    uname = email_tf.get()
    upwd = pwd_tf.get()
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and x.hexdigest() == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
            ws.destroy()
            import Menu.py
        
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)

    
var = StringVar()
var.set('male')


# widgets
left_frame = Frame(ws, bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

Label(left_frame, text="Enter Email", bg='#CCCCCC', font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(left_frame, text="Enter Password", bg='#CCCCCC',font=f).grid(row=1, column=0, pady=10)

email_tf = Entry(left_frame, font=f)

pwd_tf = Entry(left_frame, font=f, show='*')
##upwd = pwd_tf.get()
x = hashlib.md5((pwd_tf.get()).encode())

login_btn = Button(left_frame, width=15, text='Login', font=f, relief=SOLID, cursor='hand2',command=login_response)

right_frame = Frame(ws, bd=2, bg='#CCCCCC', relief=SOLID, padx=10, pady=10)

Label(right_frame, text="Enter Name", bg='#CCCCCC',font=f).grid(row=0, column=0, sticky=W, pady=10)

Label(right_frame, text="Enter Email", bg='#CCCCCC',font=f).grid(row=1, column=0, sticky=W, pady=10)

Label(right_frame, text="Age", bg='#CCCCCC',font=f).grid(row=2, column=0, sticky=W, pady=10)

Label(right_frame, text="Select Gender", bg='#CCCCCC',font=f).grid(row=3, column=0, sticky=W, pady=10)

Label(right_frame, text="Enter Password", bg='#CCCCCC',font=f).grid(row=5, column=0, sticky=W, pady=10)

Label(right_frame, text="Re-Enter Password", bg='#CCCCCC',font=f).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(right_frame,bg='#CCCCCC', padx=10, pady=10)

register_name = Entry(right_frame, font=f)

register_email = Entry(right_frame, font=f)

register_age = Entry(right_frame, font=f)

male_rb = Radiobutton(gender_frame, text='Male', bg='#CCCCCC', variable=var,value='male', font=('Times', 10))

female_rb = Radiobutton(gender_frame, text='Female', bg='#CCCCCC', variable=var, value='female', font=('Times', 10))

register_pwd = Entry(right_frame, font=f, show='*')
##register_pwd_hash = hashlib.md5((register_pwd.get()+salt).encode())
db_password = register_pwd.get()
h = hashlib.md5(db_password.encode())

pwd_again = Entry(right_frame, font=f, show='*')

register_btn = Button(right_frame, width=15, text='Register', font=f, relief=SOLID, cursor='hand2', command=insert_record)


# widgets placement
email_tf.grid(row=0, column=1, pady=10, padx=20)
pwd_tf.grid(row=1, column=1, pady=10, padx=20)
login_btn.grid(row=2, column=1, pady=10, padx=20)
left_frame.place(x=50, y=50)

register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_age.grid(row=2, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
right_frame.place(x=500, y=50)

gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)

con = sqlite3.connect('playerdata.db')
cur = con.cursor()
for row in cur.execute("Select * from record"):
    uname = row[1]
    if uname == email_tf.get():
        cur.execute("UPDATE record SET highscore = a.read()")
        con.commit()


# infinite loop
ws.mainloop()
