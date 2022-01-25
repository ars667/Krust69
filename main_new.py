import random
import math
import tkinter
from math import *
from tkinter import *
import numpy as np
import threading

label = 'Выполнение завершено'
N = 8

def get_from_file():
    f = open('input.txt')
    mas = np.zeros((N, N))
    LN = -1
    for line in f:
        LN += 1
        LineSplit = line.split()
        for i in range(len(LineSplit)):
            mas[LN][i] = LineSplit[i]
    start()



R = 250
rad = 50
angle = (2.0 * pi) / float(int(N))



def generator():
    f = open('input.txt', 'w')
    massive = []  # создаём пустой грайф из n вершин
    name = 'input.txt'
    for i in range(N):
        massive.append([])
        for j in range(N):
            massive[i].append(0)

    for z in range(N):  # рандомно заполняем граф
        for c in range(z + 1, N):
            massive[z][c] = random.randint(1, 9)
            massive[c][z] = massive[z][c]
    for z in range(N):
        for c in range(z + 1, N):
            a = random.randint(0, 2)
            if a != 1:
                massive[z][c] = 10
                massive[c][z] = massive[z][c]
    for x in massive:
        for t in x:
            f.write(str(t) + ' ')
        f.write('\n')
    f.close()
    start()


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w, angle, R):
        self.graph.append([u, v, w])
        sin1 = math.sin(angle * u)
        cos1 = math.cos(angle * u)
        y1 = sin1 * R + 300
        x1 = cos1 * R + 400
        sin2 = math.sin(angle * v)
        cos2 = math.cos(angle * v)
        y2 = sin2 * R + 300
        x2 = cos2 * R + 400
        line2(x1, y1, x2, y2)
        #window.after(0, text1(x2, x1, x2, y1, int(w)))
        window.update()

        # window.after(100, line1(x1, y1, x2, y2))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))
            sin1 = math.sin(angle * u)
            cos1 = math.cos(angle * u)
            y1 = sin1 * R + 300
            x1 = cos1 * R + 400
            sin2 = math.sin(angle * v)
            cos2 = math.cos(angle * v)
            y2 = sin2 * R + 300
            x2 = cos2 * R + 400
            window.after(500, line3(x1, y1, x2, y2))
            #window.after(0, text2(x2, x1, y2, y1, w))
            window.update()


def line1(x1, y1, x2, y2):
    c.create_line(x1, y1, x2, y2, width=5)


def rectangle():
    c.create_rectangle(
        1, 1, 925, 820,
        outline="#111", fill="#fff")


def line2(x1, y1, x2, y2):
    c.create_line(x1, y1, x2, y2, fill="#fff", width=5)
    c.create_line(x1, y1, x2, y2, fill="#111", dash=(4, 2), width=3)


def line3(x1, y1, x2, y2):
    c.create_line(x1, y1, x2, y2, fill="#11f", width=5)


def text1(x2, x1, y2, y1, w):
    c.create_text(
        (x2 + x1) / 2, (y2 + y1) / 2 - 10, anchor=W, font="Arial",
        text=w)


def text2(x2, x1, y2, y1, w):
    c.create_text(
        (x2 + x1) / 2, (y2 + y1) / 2 - 10, anchor=W, font="Arial", fill='#11f', width=4,
        text=w)


def circle(x, y, i, rad):
    c.create_oval(
        x - rad, y - rad, x + rad, y + rad, outline="#111",
        fill="#fff", width=2
    )

    c.create_text(
        x, y, anchor=W, font="Arial",
        text=i
    )


def start():
    rectangle()
    f = open('input.txt')
    mas = np.zeros((N, N))
    LN = -1
    for line in f:
        LN += 1
        LineSplit = line.split()
        for i in range(len(LineSplit)):
            mas[LN][i] = LineSplit[i]
    for i in range(N):
        for j in range(i, N):
            if mas[i][j] != 10:
                sin1 = math.sin(angle * i)
                cos1 = math.cos(angle * i)
                y1 = sin1 * R + 300
                x1 = cos1 * R + 400
                sin2 = math.sin(angle * j)
                cos2 = math.cos(angle * j)
                y2 = sin2 * R + 300
                x2 = cos2 * R + 400
                line2(x1, y1, x2, y2)
                text1(x2, x1, y2, y1, int(mas[i][j]))
                window.update()

    for i in range(0, N):
        sin = math.sin(angle * i)
        cos = math.cos(angle * i)
        y = sin * R + 300
        x = cos * R + 400
        window.after(0, circle(x, y, i, rad))
        window.update()


def main():
    f = open('input.txt')
    mas = np.zeros((N, N))
    LN = -1
    for line in f:
        LN += 1
        LineSplit = line.split()
        for i in range(len(LineSplit)):
            mas[LN][i] = LineSplit[i]
    for i in range(N):
        for j in range(i, N):
            if mas[i][j] != 10:
                sin1 = math.sin(angle * i)
                cos1 = math.cos(angle * i)
                y1 = sin1 * R + 300
                x1 = cos1 * R + 400
                sin2 = math.sin(angle * j)
                cos2 = math.cos(angle * j)
                y2 = sin2 * R + 300
                x2 = cos2 * R + 400
                line2(x1, y1, x2, y2)
                window.update()

    for i in range(0, N):
        sin = math.sin(angle * i)
        cos = math.cos(angle * i)
        y = sin * R + 300
        x = cos * R + 400
        circle(x, y, i, rad)
        window.update()

    g = Graph(N)
    for i1 in range(N):
        for j1 in range(i1 + 1, N):
            if mas[i1][j1] != 10:
                g.add_edge(i1, j1, mas[i1][j1], angle, R)

    g.kruskal()
    root = Tk()
    root.geometry('200x50+300+200')
    label = Label(root, text='Выполнение завершено', fg='black')
    label.pack()
    root.mainloop()
window = Tk()
window.title('Krustall_Shchedrin')
window.geometry('850x800+75+20')
window.resizable(0, 0)
window.iconbitmap('icon.ico')
c = Canvas(window, width=850, height=600, bg='white')
button1 = tkinter.Button(window, text="СТАРТ", command=main)
button2 = tkinter.Button(window, text="СОЗДАТЬ ГРАФ", command=generator)
button4 = tkinter.Button(window, text="ОТКРЫТЬ", command=get_from_file)


button1.pack()
button2.pack()
button4.pack()
c.pack()
window.mainloop()
