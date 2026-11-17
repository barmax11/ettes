print("\tMenu")
print("1.Вибрати піцу")
print("2.Вихід")

while True:
    action = input("Виберіть дію :")

    if action == "1":
        pizza = input("Яку піцу бажаєте :")
        count = int("Скільки піц ви хочете :")

        print(f"Замовлено {pizza}, {count} шт")
