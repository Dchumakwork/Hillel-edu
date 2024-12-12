alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on\
 where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which\
  way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh,\
   you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_sq = 436402
azov_sea_aq = 37800
both_sq = black_sea_sq + azov_sea_aq
print(f"Both seas square is {both_sq} km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_quantity = 375291
first_quantity = total_quantity - 222950
third_quantity = total_quantity - 250449
second_quantity = total_quantity - first_quantity - third_quantity
print(f"Goods quantity for each warehouse:\nFirst - {first_quantity}\nSecond - {second_quantity}\nThird - {third_quantity}")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_amount = 1179
print(f"Total PC price is {month_amount*18} UAH")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8; b = 9907 % 9; c = 2789 % 5; d = 7248 % 6; e = 7128 % 5; f = 19224 % 9
print(f"""Remainder from divisions are
a - {a}
b - {b}
c - {c}
d - {d}
e - {e}
f - {f}""")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_price = 4*274
mid_pizza_price = 2*218
juice_price = 4*35
cake_price = 350
water_price = 3*21
print(f"Total 'Birthday' price is {big_pizza_price + mid_pizza_price + juice_price + cake_price + water_price} UAH")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo_quantity = 232
photo_per_page = 8
total_pages = photo_quantity / photo_per_page
if photo_quantity % photo_per_page > 0:
    total_pages = photo_quantity // photo_per_page + 1# додаткова перевірка на залишок фотографій після розподілення на сторінки
print(f"Total pages needed to place all photos - {total_pages}")
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
tank_volume = 48
fuel_consumption = 9
print(f"Total fuel needed for a trip is {distance / 100 * fuel_consumption}")
# при обрахунку необхідної кількості заправок враховував, що старт подорожі починається з повним баком
print(f"Minimum stops for refilling the tank is {distance / 100 * fuel_consumption / tank_volume - 1}")