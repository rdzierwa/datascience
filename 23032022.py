def pobierzliczby():
    i1 = input("Podaj pierwszą liczę: ")
    i2 = input("podaj drugą liczbę: ")
    dict = [i1, i2]
    print(dict[0])
    return dict


def dzielenie():
    x = 5
    while x != "0":
        x = input(
            "Co chcesz zrobić: \n 0. Wyjdź \n 1. Policz resztę z dzielenia \n 2. Podziel bez reszty \n 3. Podziel \n:")
        if x != "0":
            liczby = pobierzliczby()
        if x == "3":
            print("Iloraz to:" + str(int(liczby[0]) / int(liczby[1])))
        if x == "2":
            print("Wynik dzielenia bez reszty to:" + str(int(liczby[0]) // int(liczby[1])))
        if x == "1":
            print("Resta z dzielenia to:" + str(int(liczby[0]) % int(liczby[1])))


def cw2():
    """
    Ćwiczenie instrukcji if
    Przypisz 8 do zmiennej x i 15 do zmiennej y
    Utwórz 2 instrukcje warunkowe
    Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”, jeśli x jest większe niż 3 lub y jest parzyste
    Niech drugi wypisze „Żaden warunek nie jest spełniony”, jeśli x jest mniejsze lub równe 3, a y jest nieparzyste
    Zmień wartości przypisane do x i y i ponownie uruchom komórkę, aby sprawdzić, czy kod nadal działa
    """
    x, y = 3, 15
    if x > 3 or y % 2 == 0:
        print("Co najmniej jeden z warunków jest spełniony")
    if x <= 3 and y % 2 != 0:
        print("Żaden warunek nie jest spełniony")
    x, y = y, x
    if x > 3 or y % 2 == 0:
        print("Co najmniej jeden z warunków jest spełniony")
    if x <= 3 and y % 2 != 0:
        print("Żaden warunek nie jest spełniony")


def women_search(lista):
    lista.sort()
    count = 0
    for i in lista:
        if i[-1] == "a":
            count += 1
    print(f"W tej liście jest {count} kobiet")


def for_rols():
    dane = (1, 2)
    for i in dane:
        if i == 3:
            break
    else:
        print("Pęta poszła wszystkie elementy przetworzono")
    print("Poza pętlą")


def build_dict():
    keys = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
    values = [10, 20, 30]
    słownik = dict()
    for i in range(len(keys)):
        słownik.update({keys[i]: values[i]})
    print(słownik)


def dziel7wielokrotnosc5(lista):
    liczby = list()
    for i in range(len(lista)):
        if lista[i] % 7 == 0 and lista[i] % 5 == 0:
            liczby.append(lista[i])
    return liczby
def dodawaj_liczby():

    s=0
    n = input("Podaj ile liczb chcesz:")
    for count in range(int(n)):
        ni= input(f"Podaj liczbę {count+1}: ")
        s = s + int(ni)
    print (f"Suma liczb to: {s}")

def dodawanie_n1():
    """
    Dokumentacja Funkcji
    Utwórz zmienną s = 0, aby przechowywać sumę wszystkich liczb
    Użyj wbudowanej funkcji input() Pythona 3, aby pobrać dane wejściowe od użytkownika
    Konwertuj dane wejściowe użytkownika na typ całkowity za pomocą konstruktora int() i zapisz je w zmiennej n
    Uruchom pętlę n razy, używając pętli for i funkcji range()
    W każdej iteracji pętli dodaj bieżącą liczbę (i) do zmiennej s
    Użyj funkcji print(), aby wyświetlić zmienną s na ekranie
    """
    # s: przechowuj sumę wszystkich liczb
    s = 0
    n = int(input("Wpisz numer "))
    # uruchom pętlę n razy
    # stop: n+1 (ponieważ range nigdy nie zawiera numeru stopu w wyniku)
    for i in range(1, n + 1, 1):
        # dodaj bieżącą liczbę do zmiennej sumy
        s += i
    print("\n")
    print("Suma to:", s)
def tabliczkazn():
    liczby = list()
    n = int(input("Podaj liczbę dla mnożenia do 10:"))
    for i in range(1, 11):
        liczby.append(n * i)
    print(liczby)

if __name__ == "__main__":
    lista = ['Marta', 'Krzysztof', 'Hania', 'Andrzej', 'Katarzyna', 'Małgorzata', 'Łukasz', 'Dominik', 'Adam',
             'Martyna', 'Sebastian', 'Dominik', 'Tymoteusz', 'Rafał', 'Anna']
# women_search(lista)

# lista = list(range(1500, 2701))
# print(dziel7wielokrotnosc5(lista))
# tabliczkazn()


