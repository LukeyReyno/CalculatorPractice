import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(padx=100, pady=100)
        self.create_widgets()
        

    def create_widgets(self):
        times16 = ('Times', '16')

        self.result = tk.Label(self, text= " " * 40, fg = "red", font=times16, background="lightblue", borderwidth=2)
        self.result.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        col = 0
        row = 1
        num = 0
        self.numB = []

        while num < 10:
            self.numB += [tk.Button(self, text=str(num))]
            self.numB[num]["command"] = lambda n=num : self.post(n)
            self.numB[num].grid(row=row, column=col, padx=2, pady=2, ipadx = 20, ipady=2)
            num += 1
            if col < 2:
                col += 1
            else:
                row += 1
                col = 0

        for op in ['+', '-', '*', '/', '%']:
            self.opB = tk.Button(self, text=op)
            self.opB["command"] = lambda o=op : self.post(o)
            self.opB.grid(row=row, column=col, padx=2, pady=2, ipadx = 20, ipady=2)
            num += 1
            if col < 2:
                col += 1
            else:
                row += 1
                col = 0

        self.equalB = tk.Button(self, text='=')
        self.equalB["command"] = self.solve
        self.equalB.grid(row=6, column=0, columnspan=2, padx=2, pady=2, ipadx = 48, ipady=2)
        
        self.quit = tk.Button(self, text="QUIT", fg="purple", command=self.master.destroy)
        self.quit.grid(row=7, column=1, padx=10)

        self.clearB = tk.Button(self, text='C')
        self.clearB["command"] = self.clear
        self.clearB.grid(row=6, column=2, padx=2, pady=2, ipadx = 20, ipady=2)
        
        self.quit = tk.Button(self, text="QUIT", fg="purple", command=self.master.destroy)
        self.quit.grid(row=7, column=1, padx=10)

    def post(self, n):
        self.result["text"] = self.result["text"][1:] + str(n)

    def solve(self):
        self.result["text"] = " " * (40 - len(str(eval(self.result["text"])))) + str(eval(self.result["text"]))

    def clear(self):
        self.result["text"] = " " * 40

root = tk.Tk(className="Calculator")
root.configure(background="lavender")
app = Application(master=root)
app.mainloop()