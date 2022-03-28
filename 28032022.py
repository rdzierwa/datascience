def longest_word(filename):
    with open(filename, "r") as file:
        text = file.read().split()
    max_len = len(max(text, key=len))  # funkcja wyszukująca ilosć znaków w najdluższym słowie
    return [word for word in text if len(word) == max_len]  # wyszukuje najdłuższe słowa krótka notacja pętli


# print(longest_word('text.txt'))


def write_file(filename, list):
    file = open(filename, "w")
    for data in list:
        file.write(str(data + '\n'))
    if file.closed:
        print ("plik zamknięty")
    else:
        print("zamykam plik")
        file.close() # jeśli nie używamy with to należy zamykać plik.
        print (file.closed)


#color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#write_file('text2.txt', color)

def counting_word_in_file():
    """Napisz program, który otworzy plik sonety.txt i sprawdzi liczbę słów w całym tekście
    Dodatkowo, napisz funkcję, która zlicza słowa tylko w co 7 linijce tekstu
    """

    with open('sonety.txt','r') as datafile:
        data = datafile.readlines()
        count_word_all = 0
        count_line = 1
        for zdania in data: # można by zrobić for in range(0,len(data),7) 
            if count_line % 7 == 0 or count_line == 1:
                liczba = len(zdania.split())
                print(f'linijka {count_line} ma {liczba} słów')
            count_word_all += len(zdania.split())
            count_line += 1
        print(f'Liczba słów w pliku {count_word_all}')

counting_word_in_file()



