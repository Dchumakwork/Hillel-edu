# task 01 == Виправте синтаксичні помилки
# тут не зовсім однозначно прописане завдання як на мене, але наскільки я зрозумів - має на виході вийти повна фраза і при цьому у функції використовуваться змінна
print("Hello", end = ", "); print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples*4

# task 05 == виправте назви змінних
_storona = 1
storona_2 = 2
storona_3 = 3
Storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = _storona + storona_2 + storona_3 + Storona_4
print(perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple = 4
pear = apple + 5
plum = apple - 2
fruits = apple + pear + plum
print(fruits)
# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morningTemp = 5
afternoonTemp = morningTemp - 10
eveningTemp = afternoonTemp + 4
print(eveningTemp)
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
generalBoys = 24
generalGirls = generalBoys / 2
generalChildren = generalGirls + generalBoys
absentChildren = 1+2
currentChildren = generalChildren - absentChildren
print(currentChildren)
# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
price1 = 8
price2 = price1+2
price3 = (price1 + price2) / 2
priceTotal = price1 + price2 + price3
print(priceTotal)

# зміни файлу для гіт комміта