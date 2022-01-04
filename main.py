import tkinter as tk
from tkinter import messagebox
import database

bank_title = "Osborne_Bank v1.1"

mainBank = tk.Tk()

# Window Settings
mainBank.title(bank_title)
mainBank.geometry("500x250")

def logger(login, password, stif):
    premult = database.finder(login.get(), password.get())
    if (premult == 200):
        wellog = tk.Tk()
        wellog.title("Successfully logged !")
        welLab = tk.Label(wellog, text=f"Welcome, {login}")
        welLab.pack()
        wellog.quit()
        stif.quit()


def newUser(phone, card_id, password, c_password, last_name, first_names, wdow):
    print()

    def error_show(error_log):
        messagebox.showerror("Registration Error", error_log)

    def exiter(mee):
        wdow.destroy()
        mee.destroy()

    if (len(str(first_names)) < 2 or str(first_names).isspace()):
        error_show("First name(s) must have an acceptable lenght")

    elif (len(str(last_name)) < 2 or str(last_name).isspace()):
        error_show("Last name must have an acceptable lenght")

    elif (not(str(phone).isdigit()) or (len(str(phone)) < 9)):
        error_show("Phone Number is wrong")

    elif (not(str(card_id).isdigit()) or len(str(card_id)) < 9):
        error_show("INE must be digits only and at least 9")

    elif (password == ""): 
        error_show("Passwords must not be null")

    elif (len(str(password)) < 4 or str(password).isspace()):
        error_show("Password must be at least 4 characters")

    elif  (password != c_password):
        error_show("Passwrds don't match")
    else:
        yess = tk.Tk()
        yess.title("Registration done")
        yess.geometry("350x100")
        msg = tk.Label(yess, text="Registration Successful!\nPlease go login")
        msg.pack()
        click = tk.Button(yess, text="OK", command=lambda: exiter(yess))
        click.pack()
        # yess.quit()
        

def tk_login(): # Login Window
    login_window = tk.Tk()
    login_window.title("Log into your account")
    login_window.geometry("400x200")

    # Inputs labels
    login_text = tk.Label(login_window, text="INE :").grid(row=0)
    login_passcode = tk.Label(login_window, text="Password :").grid(row=1)
    
    # Inputs
    login_field = tk.Entry(login_window)
    login_passcode = tk.Entry(login_window, show='*')
    login_validate = tk.Button(login_window, text="Login", width="8", height="1", command=lambda: logger(login_field, login_passcode, login_field))

    # Packing (aligning)...
    login_field.grid(row=0, column=1)    
    login_passcode.grid(row=1, column=1)
    login_validate.grid(row=2, column=1)


def tk_register(): # Register Window
    register_window = tk.Tk()
    register_window.focus_set()
    register_window.title("Create a bank account")
    register_window.geometry("400x200")

    # Text 'labels' for inouts
    register_name0 = tk.Label(register_window, text="First Names").grid(row=0)
    register_name1 = tk.Label(register_window, text="Last Name").grid(row=1)
    register_phone = tk.Label(register_window, text="Phone Number").grid(row=2)
    register_card_num = tk.Label(register_window, text="INE").grid(row=3)
    register_passcode = tk.Label(register_window, text="Password").grid(row=4)
    register_confirm_passcode = tk.Label(register_window, text="Confirm Password").grid(row=5)

    # Input fields
    register_first_names = tk.Entry(register_window)
    register_last_name = tk.Entry(register_window)
    register_phone_num = tk.Entry(register_window)
    register_ine = tk.Entry(register_window)
    register_password = tk.Entry(register_window, show='*')
    register_password_confirm = tk.Entry(register_window, show='*')
    register_validate = tk.Button(register_window, text="Validate", width="8", height="1", command=lambda: newUser(register_phone_num.get(), register_ine.get(), register_password.get(), register_password_confirm.get(), register_last_name.get(), register_first_names.get(), register_window))


    # Linking fields & labels | & |Packing
    register_first_names.grid(row=0, column=1)
    register_last_name.grid(row=1, column=1)
    register_phone_num.grid(row=2, column=1)
    register_ine.grid(row=3, column=1)
    register_password.grid(row=4, column=1)
    register_password_confirm.grid(row=5, column=1)
    register_validate.grid(row=6, column=1)


def tk_about(): # About popup
    aboutpop = tk.Tk()
    aboutpop.title(f"About {bank_title}")
    aboutpop.geometry("400x50")
    aboutCreator = tk.Label(aboutpop, text="This has been developed by {$$$} inc")
    aboutCreator.pack()

# Upper menu
mainmenu = tk.Menu(mainBank)
onlymenu = tk.Menu(mainmenu, tearoff=0)
onlymenu.add_command(label="About...", command=tk_about)
onlymenu.add_separator()
onlymenu.add_command(label="Exit", command=mainBank.quit)
mainmenu.add_cascade(label="Stuff", menu=onlymenu)

# Welcome screen
welcome_text = tk.Label(mainBank, text="Welcome to Osborne Bank Account Manager")
login_btn = tk.Button(mainBank, text="Login", width="10", height="2", command=tk_login)
register_btn = tk.Button(mainBank, text="Register", width="10", height="2", command=tk_register)

welcome_text.pack(pady=20)
login_btn.pack()
register_btn.pack()


# Main Loop
mainBank.config(menu=mainmenu)
mainBank.mainloop()