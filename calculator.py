import tkinter as tk


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)


expression = ""
input_text = tk.StringVar()
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_field = tk.Entry(input_frame, textvariable=input_text, font=('Arial', 18), bd=10, insertwidth=2, width=22, borderwidth=4, relief='ridge', justify='right')
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)  

def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result  
    except:
        input_text.set("Error")
        expression = ""

btns_frame = tk.Frame(root)
btns_frame.pack()

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]


for i, row in enumerate(buttons):
    for j, char in enumerate(row):
        if char == '=':
            btn = tk.Button(btns_frame, text=char, fg='white', bg='green', width=10, height=3, command=btn_equal)
        else:
            btn = tk.Button(btns_frame, text=char, width=10, height=3, command=lambda ch=char: btn_click(ch))
        btn.grid(row=i, column=j, padx=1, pady=1)


clear_btn = tk.Button(root, text='Clear', fg='white', bg='red', width=42, height=2, command=btn_clear)
clear_btn.pack(pady=10)

root.mainloop()
