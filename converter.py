import sets
def output_to_file(output_list, file):  # вывод в файл
    for i in range(len(output_list)):
        for j in range(len(output_list[i])):
            file.write(str(output_list[i][j]))
            if j != len(output_list[i]) - 1:
                file.write('')
        file.write('\n')
f = open('input.txt', 'r')
F = open('output.txt', 'w')

s = [[int(j) for j in list(filter(None, i.split(' ')))] for i in list(filter(None, f.read().split('\n')))]
x = sets.adjacency_to_set(s)
output_to_file([list(i) for i in x], F)

F.close()
f.close()