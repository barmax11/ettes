print("\tMenu")
print("1.Вибрати піцу")
print("2.Вихід")

while True:
    action = input("Виберіть дію :")

    if action == "1":
        print("\nМаргарита - 150 грн")
        print("\nПепероні - 180 грн")
        print("\nЧортири сири - 200 грн")

        pizza = input("Яку піцу бажаєте :")
        count = int(input("Скільки піц ви хочете :"))

        if pizza in ["МАРГАРИТА", "ПЕПЕРОНІ", "ЧОТИРИ СИРИ"]:
            print(f"Замовлено {pizza}, {count} шт")

        else:
            print("Ви ввели неправильну назву піци")

    if action == "2":
        break

    else:
        print("Ви ввели непрвильну дію")
