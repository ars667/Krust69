import random
n = 5 #количество вершин графа

mas = [] #создаём пустой грайф из n вершин
name = 'input.txt'
for i in range(n):
    mas.append([])
    for j in range(n):
        mas[i].append(0)

for z in range(n): #рандомно заполняем граф
        for c in range(z+1, n):
            mas[z][c] = random.randint(0,9)
            mas[c][z] = mas[z][c]
for z in range(n):
    for c in range(z+1, n):
        a = random.randint(0,1)
        if a == 1:
            mas[z][c] = 10
f = open(name, 'w') #сохраняем в файл
for x in mas:
    for t in x:
        f.write(str(t) + ' ')
    f.write('\n')

