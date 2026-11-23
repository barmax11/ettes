print("\tMenu")
print("1.Вибрати піцу")
print("2.Вихід")
print("3.Показати все замовлення")

orders = []
total_count = 0

while True:
    action = input("Виберіть дію :")

    if action == "1":
        print("\nМаргарита - 150 грн")
        print("\nПепероні - 180 грн")
        print("\nЧортири сири - 200 грн")

        pizza = input("Яку піцу бажаєте :")

        if pizza not in ["маргарита", "пепероні", "чотири сири"]:
            print("Ви ввели неправильну назву піци")
            continue

        count = int(input("Скільки піц ви хочете :"))

        for order in orders:
            total_count += order[1]

        if count <= 0:
            print("Кількіст піц повинна бути більше 0")

        elif total_count + count > 15:
            print("Максимальна кількість піц у замовленні 15")

        else:
            if pizza == "маргарита":
                price = 150
            elif pizza == "пепероні":
                price = 180
            elif pizza == "чотири сири":
                price = 200

            orders.append([pizza, count, price])

            print(f"Замовлено {pizza}, {count}")

    elif action == "2":
        break

    elif action == "3":
        print("\n========== ВАШЕ ЗАМОВЛЕННЯ ==========")
        print("Піца\t\tКількість\tВартість")
        print("--------------------------------------")

        total_price = 0

        for order in orders:
            pizza = order[0]
            count = order[1]
            price = order[2]

            cost = count * price
            total_price += cost

            print(f"{pizza}\t\t{count}\t\t{cost} грн")

        print("--------------------------------------")
        print(f"Загальна вартість: {total_price} грн")
        print("======================================")

    else:
        print("Ви ввели неправильну дію")
