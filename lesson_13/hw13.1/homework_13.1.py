import csv

# ф-я зчитування приймає посилання на csv-файл (і роздільник при необхідності)
# та повертає в списку його хедер + дані в кортежах
def list_from_csv(file_ref, delim=','):
    with open(file_ref, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=delim)
        header = next(reader)
        content = []
        for row in reader:
            content.append(tuple(row))
    return [header, content]

file1 = list_from_csv('rmc.csv', ';')
file2 = list_from_csv('r-m-c.csv')

# ф-я порівннювання приймає списки з фунції порівняння та записує унікальні значення у вказаний файл
def only_unique_csv_values(compare_file1, compare_file2):
    if compare_file1[0] != compare_file2[0]:
        print(f'У порівнюваних файлів різні заголовки')
    else:
        unique_content = list(set(compare_file1[1]).symmetric_difference(set(compare_file2[1])))
        with open('result_chumak.csv', mode='w', encoding='utf-8', newline='') as result:
            writer = csv.writer(result)
            writer.writerow(compare_file1[0])
            writer.writerows(unique_content)
    print(f'Унікальні дані з порівнюваних файлів записані у "result_chumak.csv" ')

only_unique_csv_values(file1,file2)

