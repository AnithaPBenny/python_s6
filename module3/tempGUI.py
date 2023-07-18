import tkinter as tk
def convert_to_celsius():
    f = float(e1.get())
    c = (f - 32) * 5 / 9
    e2.delete(0, tk.END)  # Clear previous value
    e2.insert(tk.END, "{:.2f}".format(c))
def convert_to_fahrenheit():
    celsius = float(e2.get())
    f = celsius * 9 / 5 + 32
    e1.delete(0, tk.END)  # Clear previous value
    e1.insert(tk.END, "{:.2f}".format(f))

root = tk.Tk()
root.title("Temperature Converter")

# Fahrenheit Label and Entry
l1 = tk.Label(root, text="Fahrenheit:")
l1.grid(row=0, column=0, padx=10, pady=10)

e1 = tk.Entry(root)
e1.insert(tk.END, "32.0")  # Set initial value to 32.0
e1.grid(row=1, column=0, padx=10, pady=10)

# Celsius Label and Entry
l2 = tk.Label(root, text="Celsius:")
l2.grid(row=0, column=1, padx=10, pady=10)

e2 = tk.Entry(root)
e2.insert(tk.END, "0.0")  # Set initial value to 0.0
e2.grid(row=1, column=1, padx=10, pady=10)

b1 = tk.Button(root, text=">>>>", command=convert_to_celsius)
b1.grid(row=2, column=0, padx=10, pady=10)

b2 = tk.Button(root, text="<<<<", command=convert_to_fahrenheit)
b2.grid(row=2, column=1, padx=10, pady=10)
root.mainloop()
