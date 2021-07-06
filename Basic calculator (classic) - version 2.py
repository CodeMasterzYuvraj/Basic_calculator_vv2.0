import tkinter
import tkinter.font as font

# Starting my code and making a window of tkinter

window = tkinter.Tk() # Creating a tkinter window
window.resizable(0, 0)
window.title("Basic Calculator (classic)")
dfont = font.Font(size=20)
ddfont = font.Font(size=15)
display = tkinter.Entry(window, width=25, font=dfont, bg="lightgrey", fg="grey")

display.insert(0, "0")



def number_click(n):
    x = display.get()
    if x == "0":
        display.delete(0, tkinter.END)
    a = display.get()
    current = str(a) + str(n)
    display.delete(0, tkinter.END)
    display.insert(0, current)


def solve(operation):
    f_num = display.get()
    f_num = float(f_num)
    global num1
    num1 = float(f_num)
    global current_operation
    current_operation = operation
    display.delete(0, tkinter.END)


def evaluate():
    s_num = display.get()
    s_num = float(s_num)

    if current_operation == "-":
        ab = num1 - s_num
    if current_operation == "+":
        ab = num1 + s_num
    if current_operation == "*":
        ab = num1 * s_num
    if current_operation == "/":
        ab = num1 / s_num
    if current_operation == "x":
        product = num1
        numd = num1
        global repeat
        repeat = int(s_num)
        for i in range(repeat-1):
            product = product * numd
        ab = product




    global ans
    ans = float(ab)

    display.delete(0, tkinter.END)
    if float(ans) == int(ans):
        display.insert(0, int(ans))
    if float(ans) != int(ans):
        display.insert(0, float(ans))



def clean():
    display.delete(0, tkinter.END)
    display.insert(0, "0")


def backspace():
    d = display.get()
    display.delete(0, tkinter.END)

    display.insert(0, d[:-1])

bfont = font.Font(size=16)
nfont = font.Font(size=15)
hfont = font.Font(size=10)


def memory_c():
    global m
    m = display.get()


def paste():
    display.delete(0, tkinter.END)
    display.insert(0, m)


def pet():
    display.delete(0, tkinter.END)
    display.insert(0, ans)


def about_f():
    at = tkinter.Tk()
    at.title("Calculator's info")
    at.resizable(0, 0)
    intr = """
Producer - Yuvraj
Age - 13
Class VIII

contact email - yuvraj4tech117@gmail.com
"""
    b = tkinter.Label(at, text=intr).grid(row=0, column=0)


def p2():
    sd = display.get()
    sd = float(sd)
    global final
    final = sd * sd
    display.delete(0, tkinter.END)
    if float(final) == int(final):
        display.insert(0, int(final))
    if float(final) != int(final):
        display.insert(0, float(final))





# Creating buttons
dotfont = font.Font(size=24)
memory = tkinter.Button(window, padx=38, pady=12, text="Copy", bg="LIGHTSALMON", command=memory_c, font=nfont).grid(row=3, column=3)
pe = tkinter.Button(window, padx=37, text="Undo previous solution", command=pet, font=hfont, bg="LIGHTCORAL", fg="black").grid(row=7, column=0, columnspan=2)
about = tkinter.Button(window, padx=59, text="About my calculator", command=about_f, font=hfont, bg="LIGHTCORAL", fg="black").grid(row=7, column=2, columnspan=2)
pastes = tkinter.Button(window, padx=35, pady=12, text="Paste", command=paste, font=nfont, bg="LIGHTSALMON", fg="black").grid(row=1, column=3)
x2 = tkinter.Button(window, padx=17, pady=12, text="x power 2", command=p2, font=nfont, bg="silver", fg="black").grid(row=2, column=3)


dot = tkinter.Button(window, padx=34.5, pady=1.4,  text=".", command=lambda: number_click("."), bg="silver", font=dotfont)
button_1 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="1", command=lambda: number_click(1), font=nfont)
button_2 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="2", command=lambda: number_click(2), font=nfont)
button_3 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="3", command=lambda: number_click(3), font=nfont)
button_4 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="4", command=lambda: number_click(4), font=nfont)
button_5 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="5", command=lambda: number_click(5), font=nfont)
button_6 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="6", command=lambda: number_click(6), font=nfont)
button_7 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="7", command=lambda: number_click(7), font=nfont)
button_8 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="8", command=lambda: number_click(8), font=nfont)
button_9 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="9", command=lambda: number_click(9), font=nfont)
button_0 = tkinter.Button(window, padx=40, pady=12, fg="black", bg="lightgrey", text="0", command=lambda: number_click(0), font=nfont)
plus = tkinter.Button(window, padx=40, pady=12, text="+", command=lambda: solve("+"), fg="black", bg="silver", font=bfont)
minus = tkinter.Button(window, padx=42, pady=12, text="-", command=lambda: solve("-"), fg="black", bg="silver", font=bfont)
expo = tkinter.Button(window, padx=42, pady=12, text="^", command=lambda: solve("x"), fg="black", bg="silver", font=bfont)
mult = tkinter.Button(window, padx=39, pady=12, text="×", command=lambda: solve("*"), fg="black", bg="silver", font=bfont)
div = tkinter.Button(window, padx=39, pady=12, text="÷", command=lambda: solve("/"), fg="black", bg="silver", font=bfont)
remainder = tkinter.Button(window, padx=14, pady=12, text="remainder", command=lambda: solve("%"), fg="black", bg="silver", font=bfont)
equal = tkinter.Button(window, padx=93, pady=14, text="=", command=evaluate, font=nfont)
clear = tkinter.Button(window, padx=44, pady=13, text="CE ", bg="grey", command=clean, font=nfont)
back = tkinter.Button(window, padx=42, pady=13, text=" ⌫ ", bg="grey", command=backspace, font=nfont)


# Displaying buttons and entry widgets

mult.grid(row=4, column=2)
div.grid(row=5, column=2)
remainder.grid(row=4, column=3)
display.grid(row=0, column=0, columnspan=4, pady=20)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_6.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=2)

button_3.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_1.grid(row=3, column=2)

plus.grid(row=4, column=0)
button_0.grid(row=4, column=1)
back.grid(row=5, column=3)

minus.grid(row=5, column=0)
expo.grid(row=6, column=0)
equal.grid(row=6, column=1, columnspan=2)
clear.grid(row=6, column=3)

dot.grid(row=5, column=1)
window.mainloop()
