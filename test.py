import tkinter
import random


def line1(y, x):
    canvas.create_line(0, y, x, 0, fill="black", width=3)


def line2(x, y):
    canvas.create_line(x, 0, 1200, y, fill="black", width=3)


def line3(y, x):
    canvas.create_line(1200, y, x, 900, fill="black", width=3)


def line4(x, y):
    canvas.create_line(x, 900, 0, y, fill="black", width=3)


def main():
    y = random.randint(1, 900)
    for i in range(1, 11):
        x = random.randint(1, 1200)
        window.after(100, line1(y, x))
        y = random.randint(1, 900)
        window.after(200, line2(x, y))
        x = random.randint(1, 1200)
        window.after(300, line3(y, x))
        y = random.randint(1, 900)
        window.after(400, line4(x, y))
        window.update()


if __name__ == "__main__":
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=1200, height=900, bg="white")
    button = tkinter.Button(window, text="СТАРТ", command=main)
    button.pack()
    canvas.pack()
    window.mainloop()