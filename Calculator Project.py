import tkinter as tk

root = tk.Tk()
root.title("My Calculator")
root.geometry("400x500")
root.rowconfigure(0, weight=2)
root.resizable(False, False)

# String to store the expression typed in Entry
expression = tk.StringVar()

# Entry widget creation
display = tk.Entry(root, textvariable=expression, font=("Calibri", 24), bg = "#D6D6D6", justify="right" ,bd=10)
display.grid(row=0, column=0, columnspan=4, sticky="nsew", ipady=25)

# Buttons Setup

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
button_7 = tk.Button(root, text="7", cursor="hand2", command=lambda: button_clicked("7"),font=("Arial", 20, "bold"), bd=5)
button_8 = tk.Button(root, text="8",  cursor="hand2", command=lambda: button_clicked("8"), font=("Arial", 20, "bold"), bd=5)
button_9 = tk.Button(root, text="9",  cursor="hand2", command=lambda: button_clicked("9"), font=("Arial", 20, "bold"), bd=5)
button_div = tk.Button(root, text="/",  cursor="hand2", command=lambda: button_clicked("/"), font=("Arial", 20, "bold"), bd=5)

button_4 = tk.Button(root, text="4", cursor="hand2", command=lambda: button_clicked("4"), font=("Arial", 20, "bold"), bd=5)
button_5 = tk.Button(root, text="5", cursor="hand2", command=lambda: button_clicked("5"), font=("Arial", 20, "bold"), bd=5)
button_6 = tk.Button(root, text="6", cursor="hand2", command=lambda: button_clicked("6"), font=("Arial", 20, "bold"), bd=5)
button_mul = tk.Button(root, text="*", cursor="hand2", command=lambda: button_clicked("*"), font=("Arial", 20, "bold"), bd=5)

button_1 = tk.Button(root, text="1", cursor="hand2", command=lambda: button_clicked("1"), font=("Arial", 20, "bold"), bd=5)
button_2 = tk.Button(root, text="2", cursor="hand2", command=lambda: button_clicked("2"), font=("Arial", 20, "bold"), bd=5)
button_3 = tk.Button(root, text="3", cursor="hand2", command=lambda: button_clicked("3"), font=("Arial", 20, "bold"), bd=5)
button_sub = tk.Button(root, text="-", cursor="hand2", command=lambda: button_clicked("-"), font=("Arial", 20, "bold"), bd=5)

button_0 = tk.Button(root, text="0", cursor="hand2", command=lambda: button_clicked("0"), font=("Arial", 20, "bold"), bd=5)
button_point = tk.Button(root, text=".", cursor="hand2", command=lambda: button_clicked("."), font=("Arial", 20, "bold"), bd=5)
button_equal = tk.Button(root, text="=", cursor="hand2", command=evaluate, font=("Arial", 20, "bold"), bd=5)
button_add = tk.Button(root, text="+", cursor="hand2", command=lambda: button_clicked("+"), font=("Arial", 20, "bold"), bd=5)

button_clear = tk.Button(root, text="C", cursor="hand2", command = clear_display, font=("Arial", 20, "bold"), bd=5)
button_del = tk.Button(root, text="D", cursor="hand2", command = backspace, font=("Arial", 20, "bold"), bd=5)

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