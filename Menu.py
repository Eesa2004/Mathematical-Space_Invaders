import tkinter as tk
import sqlite3


f = ('Times', 14)

##con = sqlite3.connect('playerdata.db')
##cur = con.cursor()
##
##
##            })
##con.commit()


class application(tk.Frame): 

    def __init__(self, x=None): 
        super().__init__(x) 
        self.pack(pady = 200) 
        self.x = x 
        self.create_widgets() 
        self.x.geometry("800x600")
        self.x.title("Menu- Space_Invaders")
        self.x.configure(bg='#0B5A81') 
         
  
    def create_widgets(self):
        self.score = tk.Label(self, text="Highscore: "+(open('highscore.txt', 'r')).read(), bg='#CCCCCC',font=f)
        self.score.pack(anchor = "center")
        
        self.start = tk.Button(self, text="Start", fg="blue", width=15, font=f, command=self.Start) 
        self.start.pack(anchor = "center")

        self.login = tk.Button(self, width=15, text='Login', fg="green", font=f, command=self.Login) 
        self.login.pack(anchor = "center")

        self.controls = tk.Button(self, text="Controls", fg="purple", font=f, width=15, command=self.Controls) 
        self.controls.pack(anchor = "center")
  
        self.quit = tk.Button(self, text="Quit", fg="red", width=15, font=f, command=self.x.destroy) 
        self.quit.pack(anchor = "center") 
  
  
    def Start(self): 
        import Select_difficulty.py 
  
  
    def Login(self): 
        import Login.py


    def Controls(self):
        import Start.py
  
  
root = tk.Tk() 
app = application(x=root) 
app.mainloop() 
 
