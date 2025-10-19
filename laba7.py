r = [
    {"Avicom", "Сервер", "Декада", "Dega.ru"},
    {"Диалог", "Avicom", "Сервер", "Dega.ru"},
    {"Диалог", "Декада"},
    {"Диалог", "Avicom", "Сервер", "Dega.ru"},
    {"Диалог", "Декада"},
    {"Диалог", "Avicom", "Dega.ru"},
    {"Диалог", "Avicom", "Dega.ru"}
]
arr = {"Диалог", "Avicom", "Нэта", "Сервер", "Декада", "Dega.ru"}
a = set()

for i in r:
    for j in i:
        a.add(j)

print("Не используются: ", arr - a)
