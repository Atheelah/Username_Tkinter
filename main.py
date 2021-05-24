from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Username And Password")
root.geometry("350x150")
root.resizable(height=False, width=False)
root.config(bg="orange")

# CREATING USERNAME LABEL AND ENTRY
userLbl = Label(root, text="Username :", font=("Consolas 12 bold"), bg="red", fg="white")
userLbl.place(x=0, y=10)
userEnt = Entry(root, fg="black")
userEnt.place(x=120, y=10)

# CREATING PASSWORD LABEL AND ENTRY
passLbl = Label(root, text="Password :", font=("Consolas 12 bold"), bg="red", fg="white")
passLbl.place(x=0, y=50)
passEnt = Entry(root, fg="black")
passEnt.place(x=120, y=50)

# CREATING PASSWORD AND ASSIGNING USERNAMES
user_pass = {"Vuyani": "vuya@2021", "Atheelah": "maroon17", "Ikraam": "carsthemovies", "Nathan": "blue101", "Amanda": "@manda20"}

# DEFINING A FUNCTION FOR USER SEARCH, IF THE DETAILS MATCH, YOU WILL BE SUCCESSFUL, IF NOT, YOU WILL BE UNSUCCESSFUL.
def user_search():
    if userEnt.get() in user_pass:
        if passEnt.get() == user_pass[userEnt.get()]:
            import next_window
            root.destroy()
        else:
            messagebox.showinfo(message='Login unsuccessful')
    else:
        messagebox.showinfo(message='Username doesnt exist')


# CREATING A VERIFY BUTTON
verBtn = Button(root, text="Verify", font=("Consolas 11 bold"), borderwidth=3, bg="red", fg="white", command=user_search)
verBtn.place(x=0, y=100)


# DEFINING A FUNCTION FOR THE CLEAR BUTTON
def button_clear():

    userEnt.delete(0, END)
    passEnt.delete(0, END)


# CREATING A CLEAR BUTTON
clearBtn = Button(root, text="Clear", font=("Consolas 11 bold"), borderwidth=3, bg="red", fg="white", command=button_clear)
clearBtn.place(x=130, y=100)

# DEFINING A FUNCTION FOR THE EXIT BUTTON
def button_exit():

 msg = messagebox.askquestion("Exit Application", "Are you sure you want to exit?", icon = "warning")
 if msg == 'yes':
    root.destroy()
 else:
    messagebox.showinfo('Return', 'Returning to the application screen')


# CREATING THE EXIT BUTTON
exBtn = Button(root, text="Exit", font=("Consolas 11 bold"), borderwidth=3, bg="red", fg="white", command=button_exit)
exBtn.place(x=250, y=100)

# ALLOWING THE GUI TO RUN
root.mainloop()


