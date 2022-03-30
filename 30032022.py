# lambda a,b: (((a*a)+(b*b))**0.5)//5 == 0  # wywołanie takiej funkcji można przez przypisanie do zmiennej wtedy argumeny za lambda są argumentami fukcji
# lista=[1,2,3,4,5,6]

# for i in (filter(lambda a: a%2 == 0, lista)):
#     print(i)
temperatury = [
    37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
    35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
    39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
    36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
    33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
    39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
    34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
    34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
    34.2, 40.2, 34.3, 35.3
]
'''Filter potrzebuje funkcje do sprawdzenia która zwróci true lub false np lamba, oraz listę'''
# wynik = list(filter(lambda x: x >= 40.0, temperatury)) # wynik funkcji filter żeby była lista musimy użyć funkcji list
# print(wynik)
# wynik_sort = sorted(wynik)
# print(wynik_sort)
#
# print(temperatury)

from statistics import mean

sr_temp = mean(temperatury)  # średnia wartośc z listy
# print(sr_temp)

odch = list(map(lambda x: round(x - sr_temp, 1), temperatury))
# print(odch) # funkcja map pobiera każdy z elementów z listy temperatury i wrzuca do funkcji lambda

from functools import reduce


def fun_reduce2():
    nums = [1, 2, 3, 4, 5]
    print(reduce(lambda a, b: a + b, nums))
    # dodaje pierwsze dwie i zachowuje jako następne a i bierze kolejną wartość czyli 1+2 +3, później 1+2+3+4 i do końca listy
    # jeśli mamy dwa argumenty lub więcej, to robi tak że najpierw liczy na pierwszych n liczbach
    # następnie bierze liczbę n+1 i wynik z poprzedniego działania podmienia jako pierwsza n.


# fun_reduce2
def funk_reduce():
    print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))


# funk_reduce()
# list comprehension tworzenie listy z krótki for
def list_comp():
    lista1 = []
    for x in range(10):
        lista1.append(x ** 3)
    lista = [x ** 3 for x in range(10)]
    print(lista)
    print(lista1)


# list_comp()


def list_comp_z_if():
    nowa_lista = [x ** 2 for x in range(101) if x % 2 != 0]
    print(nowa_lista)


# list_comp_z_if()

def zbior_comp():
    zbior = {znak for znak in "abracadabra" if znak not in "abc"}
    print(zbior)


# zbior_comp()

def slownik_comp():
    tekst = "abracadabra"
    wystapienie = {znak: tekst.count(znak) for znak in tekst}
    c = {x: x ** 2 for x in (2, 4, 6)}
    print(c)
    print(wystapienie)


# print(slownik_comp())

## WYRAŻENIA GENERATOROWE !!! ##
def generator():
    # list_comp = [x ** 0.5 for x in range(1, 50000001)] # to od razu generuje się przez co długo sie wykonuje
    gene_expr = (x ** 0.5 for x in range(1,
                                         50000001))  # nie tworzy listy tworzy regułę która tworzy listę na życzenie !!! czyli jak się uruchomi kod

    sum = 0
    for x in gene_expr:
        sum += x
        if sum > 100:  # super bo jak tylko znajdzie taką wartość
            break
    print(sum)


def zad_lamda_f():
    lista = (1, 2, 3, 4, 5, 6, 6)
    lista2 = (2, 3, 4, 5, 6, 3)
    wartosc = list(map(lambda a, b: a + b, lista, lista2))
    print(wartosc)
    mnozenie = lambda x, y: x * y
    print(mnozenie(2, 3))


def zad_sord_second_arg_in_krotka():
    "Napisz program w Pythonie wsparcia sortowania listy krotek za pomocą lambda po drugim elemencie"
    subject_marks = [('Język angielski', 88),
                     ('Nauka', 90),
                     ('Matematyka', 97),
                     ('Nauki społeczne', 82)]

    wynik = sorted(subject_marks, key=lambda x: x[1])
    subject_marks.sort(key=lambda x: x[1])
    print(wynik)


def sort_dict_by_index(key):
    "Napisz program w Pythonie, aby posortować za pomocą lambda listę słowników po kluczu model lub kolor."
    models = [{'marka': 'Nokia', 'model': '3310', 'kolor': 'Czarny'},
              {'marka': 'Apple', 'model': '11', 'kolor': 'Złoty'},
              {'marka': 'Samsung', 'model': 'Galaxy', 'kolor': 'Srebrny'}]
    wynik = sorted(models, key=lambda x: x[key])
    print(wynik)
    # return models.sort(key = lambda x:x[key])


# sort_dict_by_index('kolor')

def find_P_letter():
    """Napisz program w Pythonie, aby sprawdzić, czy dany ciąg (str) zaczyna się od znaku ‘P’, używając lambda
    Podpowiedź: skorzystaj z funkcji (metody to jest to po kropce) startswith()"""
    did_start = lambda string: string.startswith("P")
    print(did_start("Python"))


def find_letter_lamda_use(x, y):
    starts_with = lambda x, y: x.startswith(y)
    return (starts_with(x, y))


# print(find_letter_lamda_use('Python','P'))
def show_year_month_day_time():
    from datetime import datetime

    now = datetime.now()
    year = lambda x: x.year
    month = lambda x: x.month
    day = lambda x: x.day
    time = lambda x: x.strftime("%H:%M:%S")  # formatowanie jako string czasu

    print(year(now))
    print(month(now))
    print(day(now))
    print(time(now))


# show_year_month_day_time()

"""Ćwiczenie
Napisz program w Pythonie, aby sprawdzić, czy dany ciąg jest liczbą, czy nie, używając lambda
Podpowiedź: przydatna metoda to
string.replace(oldvalue, newvalue, count)
Składnia parametrów:
oldvalue – Wymagany; ciąg do wyszukania
newvalue – Wymagany; ciąg znaków, który ma zastąpić starą wartość
count – Opcjonalny; liczba określająca, ile wystąpień starej wartości chcesz zastąpić; domyślnie są to wszystkie wystąpienia"""


def check_string_is_number():
    did_digit = lambda string_in: string_in.replace('.', '',
                                                    1).isdigit()  # daje to samo co PS po kropce robi kolejne metody
    is_num = lambda string_in: did_digit(string_in) if string_in[0] != '-' else did_digit(string_in[1:])
    # wykonaj coś(lambda x: did_digit(x)) IF jeśli źle to wykonaj coś innego
    print(is_num("-44.4"))
    print(is_num("44.4"))
    print(is_num("0000"))
    print(is_num("A00"))
    print(is_num("001"))
    print(is_num("-00A"))


def check_list_par(nums):
    """Napisz program w Pythonie do filtrowania listy liczb parzystych i nieparzystych całkowitych za pomocą lambda i filter
    """
    return list(filter(lambda x: x % 2 == 0, nums))


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(check_list_par(nums))

def find_all_in_two_list():
    """Napisz program w Pythonie, aby znaleźć przecięcie dwóch podanych list za pomocą lambda i filter
    array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
    array_nums2 = [1, 2, 4, 8, 9]"""
    array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
    array_nums2 = [1, 2, 4, 8, 9]
    return list(filter(lambda x: x in array_nums1, array_nums2))


print(find_all_in_two_list())
