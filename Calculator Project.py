import tkinter as tk

root = tk.Tk()
root.title("My Calculator")
root.geometry("400x500")
root.rowconfigure(0, weight=2)
root.configure(bg="#2B2B2B")
root.resizable(False, False)

# String to store the expression typed in Entry
expression = tk.StringVar()

# Entry widget creation
display = tk.Entry(
    root,
    textvariable=expression,
    font=("Arial", 24),    # bigger modern text
    bg="#1E1E1E",
    fg="#00FF88",
    bd=0,
    justify="right",
    highlightthickness=2,
    highlightbackground="#3C3F41"   # thin border
)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=25)

# Buttons Setup

# Creating button styling variables
btn_bg = "#3C3F41"
btn_fg = "#FFFFFF"
btn_active = "#4B4E50"
op_bg = "#008C8C"
op_active = "#009F9F"
op_fg = "#FFFFFF"

# Function when clicking the buttons
def button_clicked(value):
    display.insert(tk.END, value)

# Function when clear button is pressed
def clear_display():
    display.delete(0, tk.END)

# Function to remove the last character shown
def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

# Function when equal button is pressed
def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)

    except ZeroDivisionError:
        display.insert(0, "Cannot divide by zero")

    except:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# make rows & columns stretch to fill window
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Creating Buttons
button_7 = tk.Button(root, text="7", cursor="hand2", command=lambda: button_clicked("7"),font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_8 = tk.Button(root, text="8",  cursor="hand2", command=lambda: button_clicked("8"), font=("Arial", 20, "bold"), bd=5,bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_9 = tk.Button(root, text="9",  cursor="hand2", command=lambda: button_clicked("9"), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_div = tk.Button(root, text="/",  cursor="hand2", command=lambda: button_clicked("/"), font=("Arial", 20, "bold"), bd=5, bg=op_bg, fg=op_fg, activebackground=op_active, activeforeground=op_fg)

button_4 = tk.Button(root, text="4", cursor="hand2", command=lambda: button_clicked("4"), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_5 = tk.Button(root, text="5", cursor="hand2", command=lambda: button_clicked("5"), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_6 = tk.Button(root, text="6", cursor="hand2", command=lambda: button_clicked("6"), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_mul = tk.Button(root, text="x", cursor="hand2", command=lambda: button_clicked("*"), font=("Arial", 20, "bold"), bd=5, bg=op_bg, fg=op_fg, activebackground=op_active, activeforeground=op_fg)

button_1 = tk.Button(root, text="1", cursor="hand2", command=lambda: button_clicked("1"), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_2 = tk.Button(root, text="2", cursor="hand2", command=lambda: button_clicked("2"), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_3 = tk.Button(root, text="3", cursor="hand2", command=lambda: button_clicked("3"), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_sub = tk.Button(root, text="-", cursor="hand2", command=lambda: button_clicked("-"), font=("Arial", 20, "bold"), bd=5, bg=op_bg, fg=op_fg, activebackground=op_active, activeforeground=op_fg)

button_0 = tk.Button(root, text="0", cursor="hand2", command=lambda: button_clicked("0"), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_point = tk.Button(root, text=".", cursor="hand2", command=lambda: button_clicked("."), font=("Arial", 20, "bold"), bd=5, bg=btn_bg, fg=btn_fg, activebackground=btn_active, activeforeground=btn_fg)
button_equal = tk.Button(root, text="=", cursor="hand2", command=evaluate, font=("Arial", 20, "bold"), bd=5, bg=op_bg, fg=op_fg, activebackground=op_active, activeforeground=op_fg)
button_add = tk.Button(root, text="+", cursor="hand2", command=lambda: button_clicked("+"), font=("Arial", 20, "bold"), bd=5, bg=op_bg, fg=op_fg, activebackground=op_active, activeforeground=op_fg)

button_clear = tk.Button(root, text="C", cursor="hand2", command = clear_display, font=("Arial", 20, "bold"), bd=5, bg=op_bg, fg=op_fg, activebackground=op_active, activeforeground=op_fg)
button_del = tk.Button(root, text="D", cursor="hand2", command = backspace, font=("Arial", 20, "bold"), bd=5, bg=op_bg, fg=op_fg, activebackground=op_active, activeforeground=op_fg)

# Arranging In grid
button_7.grid(row = 1, column = 0 , sticky="nsew", padx=5, pady=5)
button_8.grid(row = 1, column = 1, sticky="nsew", padx=5, pady=5)
button_9.grid(row = 1, column = 2, sticky="nsew", padx=5, pady=5)
button_div.grid(row = 1, column = 3, sticky="nsew", padx=5, pady=5)

button_4.grid(row = 2, column = 0, sticky="nsew", padx=5, pady=5)
button_5.grid(row = 2, column = 1, sticky="nsew", padx=5, pady=5)
button_6.grid(row = 2, column = 2, sticky="nsew", padx=5, pady=5)
button_mul.grid(row = 2, column = 3, sticky="nsew", padx=5, pady=5)

button_1.grid(row = 3, column = 0, sticky="nsew", padx=5, pady=5)
button_2.grid(row = 3, column = 1, sticky="nsew", padx=5, pady=5)
button_3.grid(row = 3, column = 2, sticky="nsew", padx=5, pady=5)
button_sub.grid(row = 3, column = 3, sticky="nsew", padx=5, pady=5)

button_0.grid(row = 4, column = 0, sticky="nsew", padx=5, pady=5)
button_point.grid(row = 4, column = 1, sticky="nsew", padx=5, pady=5)
button_equal.grid(row = 4, column = 2, sticky="nsew", padx=5, pady=5)
button_add.grid(row = 4, column = 3, sticky="nsew", padx=5, pady=5)

button_clear.grid(row = 5, column = 0, sticky="nsew", padx=5, pady=5)
button_del.grid(row = 5, column = 1, sticky="nsew", padx=5, pady=5)



root.mainloop()