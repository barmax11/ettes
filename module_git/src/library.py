# print("Вітаємо вас у нашій бібліотеці")
# print("Гарного вам дня")

print("1. Отримати книжку")
print("2. Повернути книжку")
print("3. Вихід")

while True:
    action = int(input("Виберіть дію: "))

    if action == 1:
        name = input("Введіть своє імя :")
        book = input("Введіть назву книжки :")

        print(f"Кижнку {book} видано читачеві {name}")

    elif action == 2:
        name = input("Введіть своє імя :")
        book = input("Введіть назву книжки :")

        print(f"Читач {name} повернув книжку {book}")

    elif action == 3:
        print("До побачення")
        break

    else:
        print("Неправильна дія")

