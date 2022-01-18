f = open('input.txt')
mas = []
N = 10
for i in range(N):
    for i in range(N):
        mas.append([])
        for j in range(N):
            mas[i].append(0)

    linenim = -1
    for line in f:  # рандомно заполняем граф
        linenim += 1
        for c in range(N):
            stringg = line
            print(stringg)
            k = 2*c+1
            mas[linenim][c] = int(stringg[k])
            print(linenim)
            print(c)
            print('...')
print(mas)