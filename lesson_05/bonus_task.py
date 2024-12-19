some_string = "aPPle?! {banAna, grApe.} peach 88 ORANGE apple% APPLE 17 peach 36 pineaPPle 9852??? peaCH (orange) [Peach] peach @BananA "

def calc_words(string):
    # прибираю зайві символи зі стрінги методом об'єеднання (цей спосіб мені здався найбільш лаконічним).
    # Можливо тут можна було б використать регулярні вирази, але я з ними не мав справи і не знаю точно чи є
    # потрібні набори спецсимволів :)
    symbols_to_erase = "123456789.,!?:;()%$@[]{}#"
    clear_string = ''.join([symb for symb in string if symb not in symbols_to_erase])
    # змінюю регістр на нижній та розділяю стрінгу
    clear_string = clear_string.lower()
    clear_list = clear_string.split()
    # створюю порожній список для майбутнього порівняння значень і виключення повторень
    check_item = []
    # виводжу кількість слів по порядку їх першого знаходження в реченні
    for i in clear_list:
        if i not in check_item:
            word_amount = clear_list.count(i)
            print(f"{word_amount} matches of word '{i}' was(were) found in your sentence.")
            check_item.append(i)

    return clear_list

calc_words(some_string)