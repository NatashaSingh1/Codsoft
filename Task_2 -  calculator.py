import tkinter as tk

def calculate():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        op = operation.get()
        
        if op == '+':
            result.set(a + b)
        elif op == '-':
            result.set(a - b)
        elif op == '*':
            result.set(a * b)
        elif op == '/':
            if b == 0:
                result.set("Can't divide by 0")
            else:
                result.set(a / b)
        else:
            result.set("Choose operation")
    except:
        result.set("Invalid input")

# Main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="Enter first number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Operation choice
tk.Label(root, text="Choose operation (+, -, *, /)").pack()
operation = tk.Entry(root)
operation.pack()

# Button to calculate
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result display
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14)).pack()

root.mainloop()

