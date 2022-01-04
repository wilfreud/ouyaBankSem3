import tkinter as tk

mainBank = tk.Tk()
# Window Settings
mainBank.title("Osborne_Bank v1.1")
mainBank.geometry("500x250")

def tk_login(): # Login Window
    login_window = tk.Tk()
    login_window.title("Log into your account")
    login_window.geometry("400x200")
    login_field = tk.Entry(login_window)
    login_passcode = tk.Entry(login_window, show='*')
    login_validate = tk.Button(login_window, text="Login", width="8", height="1")


    # Packing (aligning)...
    login_field.pack()
    login_passcode.pack()
    login_validate.pack()

def tk_register(): # Register Window
    register_window = tk.Tk()
    register_window.title("Create a bank account")
    register_window.geometry("400x200")
    register_first_names = tk.Entry(register_window)
    register_last_name = tk.Entry(register_window)
    register_phone_num = tk.Entry(register_window)
    register_validate = tk.Button(register_window, text="Validate", width="8", height="1")

    # Packing
    register_first_names.pack()
    register_last_name.pack()
    register_phone_num.pack()
    register_validate.pack()


# Welcome screen
welcome_text = tk.Label(mainBank, text="Welcome to Osborne Bank Account Manager")
welcome_text.pack()

login_btn = tk.Button(mainBank, text="Login", width="10", height="2", command=tk_login)
login_btn.pack()
login_btn = tk.Button(mainBank, text="Register", width="10", height="2", command=tk_register)
login_btn.pack()



mainBank.mainloop()