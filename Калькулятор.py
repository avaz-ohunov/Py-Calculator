# Калькулятор.py

from tkinter import *
from pyautogui import press


press("NumLock") # Автонажатие клавиши NumLock


# Задаём параметры окну приложения
window = Tk()
window.title("Калькулятор")
window.geometry("370x450")
window.resizable(width=False, height=False)
window["bg"] = "#1b1c1b"
window.iconbitmap("Иконка.ico")



text = Label(window,
			text="Обычный",
			font="Comfortaa 20",
			bg="#1b1c1b",
			fg="white")
text.place(x=120, y=0)



# Создаём поле ввода
entry = Entry(window,
				font="Ubuntu 35",
				insertbackground="#1b1c1b",
				bg="#1b1c1b",
				fg="#dcdce0",
				width="14",
				relief="flat",
				justify="center")
entry.place(x=0, y=35)
entry.focus()





# Функция клика на кнопку 0
def click_0():
	entry.insert(END, "0")

# Параметры кнопки 0 
button0 = Button(window,
				text=" 0",
				font="Ubuntu, 34",
				width=7,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_0)
button0.place(x=0, y=361)


# Функция клика на кнопку 1
def click_1():
	entry.insert(END, "1")

# Параметры кнопки 1
button1 = Button(window,
				text="1",
				font="Ubuntu, 34",
				width=3,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_1)
button1.place(x=0, y=272)


# Функция клика на кнопку 2
def click_2():
	entry.insert(END, "2")

# Параметры кнопки 2
button2 = Button(window,
				text="2",
				font="Ubuntu, 34",
				width=2,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_2)
button2.place(x=72, y=272)


# Функция клика на кнопку 3
def click_3():
	entry.insert(END, "3")

# Параметры кнопки 3
button3 = Button(window,
				text="3",
				font="Ubuntu, 34",
				width=2,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_3)
button3.place(x=130, y=272)


# Функция клика на кнопку 4
def click_4():
	entry.insert(END, "4")

# Параметры кнопки 4
button4 = Button(window,
				text="4",
				font="Ununtu, 34",
				width=3,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_4)
button4.place(x=0, y=183)


# Функция клика на кнопку 5
def click_5():
	entry.insert(END, "5")

button5 = Button(window,
				text="5",
				font="Ubuntu, 34",
				width=2,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_5)
button5.place(x=72, y=183)


# Функция клика на кнопку 6
def click_6():
	entry.insert(END, "6")

# Параметры кнопки 6
button6 = Button(window,
				text="6",
				font="Ubuntu, 34",
				width=2,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_6)
button6.place(x=130, y=183)


# Функция клика на кнопку 7
def click_7():
	entry.insert(END, "7")

# Параметры кнопки 7
button7 = Button(window,
				text="7",
				font="Ubuntu, 34",
				width=3,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_7)
button7.place(x=0, y=94)


# Функция клика на кнопку 8
def click_8():
	entry.insert(END, "8")

# Параметры кнопки 8
button8 = Button(window,
				text="8",
				font="Ubuntu, 34",
				width=2,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_8)
button8.place(x=72, y=94)


# Функция клика на кнопку 9
def click_9():
	entry.insert(END, "9")

button9 = Button(window,
				text="9",
				font="Ubuntu, 34",
				width=2,
				bg="#1b1c1b",
				fg="#ecf76d",
				relief="flat",
				activebackground="#ecf76d",
				activeforeground="#ecf76d",
				cursor="hand2",
				command=click_9)
button9.place(x=130, y=94)



# Функция клика на кнопку del
def click_del():
	entry.delete( entry.index("insert") - 1 )

# Параметры кнопки del
button_delete = Button(window,
					text="del",
					font="Ubuntu, 34",
					width=3,
					bg="#1b1c1b",
					fg="#dba02a",
					relief="flat",
					activebackground="#dba02a",
					activeforeground="#dba02a",
					cursor="hand2",
					command=click_del)
button_delete.place(x=193, y=94)


# Функция клика на кнопку clear(C)
def click_C():
	entry.delete(0, END)

# Параметры кнопки clear(C)
button_clear = Button(window,
					text="C",
					font="Ubuntu, 34",
					width=3,
					bg="#1b1c1b",
					fg="#d48d87",
					relief="flat",
					activebackground="#d48d87",
					activeforeground="#d48d87",
					cursor="hand2",
					command=click_C)
button_clear.place(x=193, y=183)


# Функция кнопки =
def click_equally():
	calculate = eval( entry.get() )
	entry.delete(0, END)
	entry.insert(0, calculate)


button_equally = Button(window,
						text="=",
						font="Ubuntu, 34",
						width=3,
						bg="#1b1c1b",
						fg="#89d487",
						relief="flat",
						activebackground="#89d487",
						activeforeground="#89d487",
						cursor="hand2",
						command=click_equally)
button_equally.place(x=282, y=361)


# Функция клика на кнопку ÷
def click_split():
	entry.insert(END, "/")

# Параметры кнопки ÷
button_split = Button(window,
					text="÷",
					font="Ubuntu, 34",
					width=3,
					bg="#1b1c1b",
					fg="white",
					relief="flat",
					activebackground="white",
					activeforeground="white",
					cursor="hand2",
					command=click_split)
button_split.place(x=193, y=272)


# Функция клика на кнопку "."
def click_comma():
	entry.insert(END, ".")

# Параметры кнопки "."
button_comma = Button(window,
					text=".",
					font="Ubuntu, 34",
					width=3,
					bg="#1b1c1b",
					fg="white",
					relief="flat",
					activebackground="white",
					activeforeground="white",
					cursor="hand2",
					command=click_comma)
button_comma.place(x=193, y=361)


# Функция клика на кнопку "х"
def click_multiply():
	entry.insert(END, "*")

# Параметры кнопки "х"
button_multiply = Button(window,
						text="x",
						font="Ubuntu, 34",
						width=3,
						bg="#1b1c1b",
						fg="white",
						relief="flat",
						activebackground="white",
						activeforeground="white",
						cursor="hand2",
						command=click_multiply)
button_multiply.place(x=282, y=272)


# Функция клика на кнопку "-"
def click_minus():
	entry.insert(END, "-")

# Параметры кнопки "-"
button_minus = Button(window,
						text="–",
						font="Ubuntu, 34",
						width=3,
						bg="#1b1c1b",
						fg="white",
						relief="flat",
						activebackground="white",
						activeforeground="white",
						cursor="hand2",
						command=click_minus)
button_minus.place(x=282, y=183)


# Функция клика на кнопку "+"
def click_plus():
	entry.insert(END, "+")

# Параметры кнопки "+"
button_plus = Button(window,
						text="+",
						font="Ubuntu, 34",
						width=3,
						bg="#1b1c1b",
						fg="white",
						relief="flat",
						activebackground="white",
						activeforeground="white",
						cursor="hand2",
						command=click_plus)
button_plus.place(x=282, y=94)





# Функция нажатия клавиши Enter
def enter(event):
	if event.keysym == "Return":
		click_equally()
window.bind("<Return>", enter)


# Функция нажатия клавиши Escape
def esc(event):
	if event.keysym == "Escape":
		window.destroy()
window.bind("<Escape>", esc)


# Функция нажатия клавиши "C"
def enter_C(event):
	if event.keysym == "c":
		click_C()
window.bind("c", enter_C)












window.mainloop()


press("NumLock") # Автонажатие клавиши NumLock
