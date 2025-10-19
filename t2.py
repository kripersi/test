r = int(input("Кол-во элементов: "))
arr = []

for i in range(r):
    elem = int(input("Элемент: "))
    arr.append(elem)

print(arr)

for el in arr:
    if el == 20:
        arr.remove(el)

print(arr)
