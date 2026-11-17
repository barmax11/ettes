# Завдання 1
# Напишіть програму для роботи онлайн магазину.
# Товари:
# ● подушка – 650 грн
# ● ковдра – 1700 грн
# ● лампа – 500 грн
# ● брелок – 60 грн
# Меню дій:
# ● додати товар
# ● видалити товар
# ● очистити кошик
# ● показати вміст кошики та суму покупки
# ● вихід
# Користувачу показується меню один раз на початку
# програми
# Користувач вибирає номер дії після чого за потреби
# вводить назву товару то його кількість
# У випадку неправильно введених даних повідомити про
# це та повернутись до вибору номера дії
# Створіть для кожного товару змінну з кількістю цього
# товару у кошику для подальшої роботи

# print("\tMenu")
# print("Подушка 650 грн")
# print("Ковдра 1700 грн")
# print("Лампа 500 грн")
# print("Брелок 60 грн")
# print()
# print("1. Додати товар")
# print("2. Видалити товар")
# print("3. Очистити кошик")
# print("4. Показати вміст кошика та суму покупки")
# print("5. Вихід")
#
# pillows = 0
# blankets = 0
# lamps = 0
# keychains = 0
#
# while True:
#     action = int(input("Виберіть дію від (1-5) :"))
#
#     if action == 1:
#         product = input("Введіть назву товару :").upper()
#         quantity = int(input("Введіть кількість :"))
#
#         if quantity > 0:
#             if product == "ПОДУШКА":
#                 pillows += quantity
#             elif product == "КОВДРА":
#                 blankets += quantity
#             elif product == "ЛАМПА":
#                 lamps += quantity
#             elif product == "БРЕЛОК":
#                 keychains += quantity
#             else:
#                 print("Немає такого товару")
#
#         else:
#             print("Неправильна кількість")
#
#     elif action == 2:
#         product = input("Введіть назву товару :").upper()
#         quantity = int(input("Введіть кількість :"))
#         if quantity > 0:
#             if product == "ПОДУШКА" and pillows >= quantity:
#                 pillows -= quantity
#             elif product == "КОВДРА" and blankets >= quantity:
#                 blankets -= quantity
#             elif product == "ЛАМПА" and lamps >= quantity:
#                 lamps -= quantity
#             elif product == "БРЕЛОК" and keychains >= quantity:
#                 keychains -= quantity
#             else:
#                 print("Такого товару немає або недостатня кількість")
#         else:
#             print("Неправильна кількість")
#
#     elif action == 3:
#         pillow = 0
#         blanket = 0
#         lamp = 0
#         keychain = 0
#         print("Кошик очищено!")
#
#     elif action == 4:
#         total = pillows * 650 + blankets * 1700 + lamps * 500 + keychains * 60
#
#         print("\t ВАШ КОШИК ")
#         print("Подушка:", pillows)
#         print("Ковдра:", blankets)
#         print("Лампа:", lamps)
#         print("Брелок:", keychains)
#         print("Сума покупки:", total, "грн")
#
#     elif action == 5:
#         print("Дякуємо за покупку!")
#         break
#
#     else:
#         print("Неправильний номер дії!")
