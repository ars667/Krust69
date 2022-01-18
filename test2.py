import tkinter
import random


def line1(x1,y1,x2,y2):
    canvas.create_line(x1, y1, x2, y2)


def main():
    for i in range(1,11):    
        y1 = random.randint(1, 900)
        x1 = random.randint(1, 1200)
        y2 = random.randint(1, 900)
        x2 = random.randint(1, 1200)
        window.after(300, line1(y1,x1,y2, x2))
        window.update()


if __name__ == "__main__":
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=1200, height=900, bg="white")
    button = tkinter.Button(window, text="СТАРТ", command=main)
    button.pack()
    canvas.pack()
    window.mainloop()