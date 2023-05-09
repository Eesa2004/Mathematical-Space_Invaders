import tkinter as tk   

f = ('Times', 14)

class application(tk.Frame): 

    def __init__(self, x=None): 
        super().__init__(x) 
        self.pack(pady = 170) 
        self.x = x 
        self.create_widgets() 
        self.x.geometry("800x600")
        self.x.title("Select Difficulty- Space_Invaders")
        self.x.configure(bg="#0A1428") 
         
  
    def create_widgets(self): 
        self.easy = tk.Button(self, text="EASY", font=f, fg="blue", width=20, height=3, command=self.Easy) 
        self.easy.pack(anchor = "center")
         
        self.hard = tk.Button(self, text="HARD", font=f, fg="green", width=20, height=3, command=self.Hard) 
        self.hard.pack(anchor = "center")
  
        self.quit = tk.Button(self, text="QUIT", font=f, fg="red", width=20, height=3, command=self.x.destroy) 
        self.quit.pack(anchor = "center") 
  
  
    def Easy(self):
        self.x.destroy()
        import Start_easy.py 
  
  
    def Hard(self):
        self.x.destroy()
        import Start_hard.py
  
  
root = tk.Tk() 
app = application(x=root) 
app.mainloop() 
