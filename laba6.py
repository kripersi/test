r = int(input("Кол-во строк: "))
c = int(input("Кол-во столбцов: "))
arr = []

for i in range(r):
    new_arr = []
    for n in range(c):
        elem = int(input("Элемент: "))
        new_arr.append(elem)
    arr.append(new_arr)

print(arr)

max_els_index = []
for row in arr:
    max_el = max(row)
    max_index = row.index(max_el)
    max_els_index.append(max_index)

print(max_els_index)
