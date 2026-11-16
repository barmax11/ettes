# print("Вітаємо вас у нашій бібліотеці")
# print("Гарного вам дня")

print("1. Отримати книжку")
print("2. Вихід")

while True:
    action = int(input("Виберіть дію: "))

    if action == 1:
        name = input("Введіть своє ім'я: ")
        book = input("Введіть назву книжки: ")

        print(f"Кижнку {book} видано читачеві {name}")

    elif action == 2:
        print("До побачення")
        break

    else:
        print("Неправильна дія")

