import tkinter
import math

button_values = [
    ["AC", "%", "⌫", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "%", "⌫"]

row_count = len(button_values)
column_count = len(button_values[0])

color_blue= "#1B02A3"
color_black= "#181818" 
color_grey= "#3A3A3A"



window = tkinter.Tk()
window.title("MyCalc by Anurh")
window.resizable(False, False)

frame = tkinter.Frame(window)
label= tkinter.Label(frame, text="0", font=("Arial", 45),background=color_black,
                     foreground="white", anchor="e", width=column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value= button_values[row][column]
        button=tkinter.Button(frame, text=value, font=("Arial", 30),
                               width=column_count-1, height=1,
                               command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.configure(foreground=color_black, background="white")
        elif value in right_symbols:
            button.configure(foreground="white", background=color_blue)
        else:
            button.configure(foreground="white", background=color_grey)
        button.grid(row=row+1, column=column)

frame.pack()

A= "0"
op= None
B= None
answer= None
new_calculation= False


def clear_cal():
    global A, B, op, answer
    A= "0"
    B= None
    op= None
    answer= None


def rem_zeroes(n):
    if n%1 ==0:
        n = int(n)
    return str(n)


def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, op, answer, new_calculation

    if value in right_symbols:

        if value == "=":

            if A is not None and op is not None and B is not None:

                num1= float(A)
                num2= float(B)

                if op == "+":
                    answer= rem_zeroes(num1 + num2)

                elif op == "-":
                    answer= rem_zeroes(num1 - num2)

                elif op == "×":
                    answer= rem_zeroes(num1 * num2)

                elif op == "÷":
                    if num2 == 0:
                        label["text"]= "*error*"
                        clear_cal()
                        return
                    else:
                        answer= rem_zeroes(num1 / num2)

                label["text"]= answer

                A= answer
                B= None
                op= None
                new_calculation= True

        elif value in "+-×÷":

            if new_calculation:

                A= answer
                B= None
                op= value

                label["text"]= "Ans" + value

                new_calculation= False

            elif op is None:

                A= label["text"]
                B= None
                op= value

                label["text"]= A + value

            else:

                op= value

                if B is not None:
                    label["text"]= A + value

    elif value in top_symbols:

        if value == "AC":

            clear_cal()
            label["text"]= "0"
            new_calculation= False

        elif value == "%":

            if op is not None and B is not None:

                B= rem_zeroes(float(B) / 100)

                if A == answer:
                    label["text"]= "Ans" + op + B
                else:
                    label["text"]= A + op + B

            else:

                current_number= label["text"]

                if current_number.startswith("Ans"):
                    current_number= current_number[3:]

                result= float(current_number) / 100

                label["text"]= rem_zeroes(result)

        elif value == "⌫":

            if op is not None and B is not None:

                if len(B) > 1:
                    B= B[:-1]
                else:
                    B= "0"

                if A == answer:
                    label["text"]= "Ans" + op + B
                else:
                    label["text"]= A + op + B

            else:

                current_number= label["text"]

                if current_number.startswith("Ans"):
                    current_number= current_number[3:]

                if len(current_number) > 1:
                    label["text"]= current_number[:-1]
                else:
                    label["text"]= "0"

    elif value == "√":

        if op is not None and B is not None:

            result= math.sqrt(float(B))

            B= rem_zeroes(result)

            if A == answer:
                label["text"]= "Ans" + op + B
            else:
                label["text"]= A + op + B

        else:

            current_number= label["text"]

            if current_number.startswith("Ans"):
                current_number= current_number[3:]

            number= float(current_number)

            if number < 0:
                label["text"]= "*error*"
            else:
                result= math.sqrt(number)
                label["text"]= rem_zeroes(result)

    else:

        if new_calculation:

            label["text"]= value
            A= "0"
            B= None
            op= None
            new_calculation= False

        elif value == ".":

            if op is not None:

                if B is None:
                    B= "0."

                elif "." not in B:
                    B += "."

                if A == answer:
                    label["text"]= "Ans" + op + B
                else:
                    label["text"]= A + op + B

            else:

                if "." not in label["text"]:
                    label["text"] += "."

        elif value in "0123456789":

            if op is not None:

                if B is None or B == "0":
                    B= value
                else:
                    B += value

                if A == answer:
                    label["text"]= "Ans" + op + B
                else:
                    label["text"]= A + op + B

            else:

                if label["text"] == "0":
                    label["text"]= value
                else:
                    label["text"] += value


window.update()

window_width= window.winfo_width()
window_height= window.winfo_height()

screen_width= window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

x= int((screen_width // 2) - (window_width // 2))
y= int((screen_height // 2) - (window_height // 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.mainloop()

