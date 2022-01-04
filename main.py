import tkinter as tk
import dbCall

bank_title = "Osborne_Bank v1.1"

mainBank = tk.Tk()

# Window Settings
mainBank.title(bank_title)
mainBank.geometry("500x250")

def logger(login, password):
    # response = dbCall.login()
    print()

def newUser(phone, card_id, password, c_password):
    response = dbCall.register()

    def error_show(error_log):
        tk.messagebox.showerror("Registration Error", error_log)

    if (response[0] != 0):
        error_show(response[1])
    else:
        yess = tk.TK()
        yess.title("Registration done")
        yess.geometry("350x100")
        msg = tk.Label(yess, text="Registration Successful !")
        from time import sleep
        sleep(2)
        yess.quit()
        


def tk_login(): # Login Window
    login_window = tk.Tk()
    login_window.title("Log into your account")
    login_window.geometry("400x200")

    # Inputs labels
    login_text = tk.Label(login_window, text="Login :").grid(row=0)
    login_passcode = tk.Label(login_window, text="Password :").grid(row=1)
    
    # Inputs
    login_field = tk.Entry(login_window)
    login_passcode = tk.Entry(login_window, show='*')
    login_validate = tk.Button(login_window, text="Login", width="8", height="1")

    # Packing (aligning)...
    login_field.grid(row=0, column=1)    
    login_passcode.grid(row=1, column=1)
    login_validate.grid(row=2, column=1)


def tk_register(): # Register Window
    register_window = tk.Tk()
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
    register_validate = tk.Button(register_window, text="Validate", width="8", height="1")


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