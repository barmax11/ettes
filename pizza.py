print("\tMenu")
print("1.Вибрати піцу")
print("2.Вихід")

while True:
    action = input("Виберіть дію :")

    if action == "1":
        print("\nМаргарита - 150 грн")
        print("\nПепероні - 180 грн")
        print("\nЧортири сири - 200 грн")

        pizza = input("Яку піцу бажаєте :").upper
        count = int("Скільки піц ви хочете :")

        print(f"Замовлено {pizza}, {count} шт")
