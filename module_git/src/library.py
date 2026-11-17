# print("Вітаємо вас у нашій бібліотеці")
# print("Гарного вам дня")

print("1. Отримати книжку")
print("2. Повернути книжку")
print("3. Вихід")

while True:
    action = int(input("Виберіть дію: "))

    if action == 1 or action == 2:
        name = input("Введіть своє ім'я: ")
        book = input("Введіть назву книжки: ")

        if name == "" or book == "":
            print("Імя та назва не можуть бути порожніми")

        elif action == 1:
            time = int(input("На скільки днів хочете взяти :"))

            if time < 0:
                print("Кількість днів не може бути відємною")

            elif time > 30:
                print("Книжку можна отримати максимум на 30 днів")

            else:
                print(f"Книжку {book} видано читачеві {name} на {time} днів")

        elif action == 2:
            print(f"Читач {name} повернув книжку {book}")

    elif action == 3:
        print("До побачення")
        break

    else:
        print("Неправильна дія")
