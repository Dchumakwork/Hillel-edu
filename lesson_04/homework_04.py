adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 == В цьому завданні як я зрозумів потрібно використовувать виключно методи строк, але я не зміг придумать як
# тільки ними покрити умови, коли кількість замінних пробілів може бути різною. Тому прописав тільки для явної заміни.
# Якщо ж треба вирішить інакше, то прошу підказать напрямок
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("   ", " ")
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
h_amount = adwentures_of_tom_sawer.count("h")
print(h_amount)

# task 05 тут приблизно така ж ситуація - виключно методами строк не знаю як вирішить задачу. Тому просто порахував
# по кількості великих літер. Була ще ідея посплітить через пробіл і зробить перевірки через istitle, але ж деякі стрінги
# в такому випадку можуть починаться не з літери, а іншого символу
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
total_titles = 0
for i in adwentures_of_tom_sawer:
    if i.isupper():
        total_titles=total_titles+1
print(total_titles)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_pos = adwentures_of_tom_sawer.find("Tom")
second_pos = adwentures_of_tom_sawer.find("Tom", first_pos+1)
print(first_pos, second_pos)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3])

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for i in adwentures_of_tom_sawer_sentences:
    if i.startswith("By the time"):
        print(i)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
words_last_sent = adwentures_of_tom_sawer_sentences[-1].split()
print(len(words_last_sent))