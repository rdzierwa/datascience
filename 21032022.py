def tree_letter(str):
    '''Wyliczamy 3 znaki od środka'''
    cals = len(str1) // 2
    print(str[cals - 1:cals + 2])


def inside_string(str1, str2):
    '''Wyliczamy 3 znaki od środka'''
    cals = len(str1) // 2
    print(str1[:cals] + str2 + str1[cals:])


def connect_string(str1, str2):
    '''Biorąc pod uwagę 2 ciągi, s1 i s2 zwróć nowy ciąg złożony z pierwszego, środkowego i ostatniego znaku każdego ciągu wejściowego'''
    cals = len(str1) // 2
    cals2 = len(str2) // 2
    print(str1[0] + str2[0] + str1[cals] + str2[cals2] + str1[-1] + str2[-1])


def reverse(str1):
    '''odwróć ciąg znaków str1'''
    print(str1[::-1])


def reverse_tuple(tup1):
    '''odwróć krotkę tup1'''
    print(tup1[::-1])


def insede_tuple(tup1):
    middle = len(tup1) // 2
    middle_in = len(tup1[middle]) // 2
    print(tup1[middle][middle_in])


def list_sort(list1):
    len_list = len(list1)
    new_list = sorted(list1)
    print(f"Liczba elementów listy {len_list} a lista to {new_list}")

def list_to_dict(keys,values):
    '''dwie listy. konwertujący je na słownik w taki sposób, że pozycja z listy 1 jest kluczem, a pozycja z listy 2 jest wartością'''
    dictionary = dict(zip(keys, values)) # zip działa w każdym iterowalnym obiekcie
    print(dictionary)

if __name__ == '__main__':
    tup1 = (10, 20, 30, 40, 50)
    str1 = "America"
    str2 = "Japan"
    str3 = "FullStack"
    str4 = "Python"
    tup2 = ("Pomarańczowy", [10, 20, 30], (5, 15, 25))
    # insede_tuple(tup2)
    lista = ['Marta', 'Krzysztof', 'Hania', 'Andrzej', 'Katarzyna', 'Małgorzata', 'Łukasz', 'Dominik', 'Adam',
             'Martyna', 'Sebastian', 'Dominik', 'Tymoteusz', 'Rafał', 'Anna']
    #list_sort(lista)
    keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
    values = [10, 20, 30]
    #list_to_dict(keys,values)
    sample_set = {"Żółty", "Pomarańczowy", "Czarny",}
    sample_list = ["Niebieski", "Zielony", "Czerwony"]
    #print(sample_set)
    sample_set.update(sample_list) # Aktualizuje słownik
    x=5 if 2<1 else 0 #short dla ifa
    print (x)
    print(("tak","nie")[2>1]) # short dla ifa
    x = range(-11,200,3)
    for z in x:
        print (z)
    print (type(x))
