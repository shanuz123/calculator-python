import tkinter as tk

root = tk.Tk()
root.title("My Calculator")
root.geometry("400x500")

# String to store the expression typed in Entry
expression = tk.StringVar()

# Entry creation
entry_widget = tk.Entry(root, textvariable=expression, width = 60, bg = "#D6D6D6", justify="right" ,bd=10, insertwidth=2)
entry_widget.grid(row=0, column=0, columnspan=4, ipadx=20, ipady=10)

# Buttons Layout

# Function when clicking the buttons
def button_clicked(value):
    entry_widget.insert(tk.END, value)

# make rows & columns stretch to fill window
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(4):
    root.columnconfigure(j, weight=1)

# Creating Buttons
button_7 = tk.Button(root, text="7", width=10, height=4, cursor="hand2", command=lambda: button_clicked("7"))
button_8 = tk.Button(root, text="8", width=10, height=4, cursor="hand2", command=lambda: button_clicked("8"))
button_9 = tk.Button(root, text="9", width=10, height=4, cursor="hand2", command=lambda: button_clicked("9"))
button_div = tk.Button(root, text="/", width=10, height=4, cursor="hand2", command=lambda: button_clicked("/"))

button_4 = tk.Button(root, text="4", width=10, height=4, cursor="hand2", command=lambda: button_clicked("4"))
button_5 = tk.Button(root, text="5", width=10, height=4, cursor="hand2", command=lambda: button_clicked("5"))
button_6 = tk.Button(root, text="6", width=10, height=4, cursor="hand2", command=lambda: button_clicked("6"))
button_mul = tk.Button(root, text="*", width=10, height=4, cursor="hand2", command=lambda: button_clicked("*"))

button_1 = tk.Button(root, text="1", width=10, height=4, cursor="hand2", command=lambda: button_clicked("1"))
button_2 = tk.Button(root, text="2", width=10, height=4, cursor="hand2", command=lambda: button_clicked("2"))
button_3 = tk.Button(root, text="3", width=10, height=4, cursor="hand2", command=lambda: button_clicked("3"))
button_sub = tk.Button(root, text="-", width=10, height=4, cursor="hand2", command=lambda: button_clicked("-"))

button_0 = tk.Button(root, text="0", width=10, height=4, cursor="hand2", command=lambda: button_clicked("0"))
button_point = tk.Button(root, text=".", width=10, height=4, cursor="hand2", command=lambda: button_clicked("."))
button_equal = tk.Button(root, text="=", width=10, height=4, cursor="hand2", command=lambda: button_clicked("="))
button_add = tk.Button(root, text="+", width=10, height=4, cursor="hand2", command=lambda: button_clicked("+"))

button_clear = tk.Button(root, text="C", width=10, height=4, cursor="hand2", command=lambda: button_clicked("C"))

# Arranging In grid
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_div.grid(row = 1, column = 3)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_mul.grid(row = 2, column = 3)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_sub.grid(row = 3, column = 3)

button_0.grid(row = 4, column = 0)
button_point.grid(row = 4, column = 1)
button_equal.grid(row = 4, column = 2)
button_add.grid(row = 4, column = 3)

button_clear.grid(row = 5, column = 0)



root.mainloop()