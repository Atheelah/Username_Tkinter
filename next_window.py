from tkinter import *
root = Tk()
root.title("Username And Password")
root.geometry("350x150")
root.resizable(height=False, width=False)
root.config(bg="orange")
txt = Label(root, text="You Were Successful", font=("Consolas 20 bold"), bg="red", fg="white")
txt.place(x=25, y=50)
root.mainloop()
