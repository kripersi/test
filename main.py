r = int(input("Кол-во элементов: "))
arr = []

for i in range(r):
    elem = int(input("Элемент: "))
    arr.append(elem)

print(arr)

for el in range(len(arr)):
    arr[el] = arr[el]**2

print(arr)
