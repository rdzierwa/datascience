def sum_rek(number):
    if number == 0: return 0
    return number + sum_rek(number - 1)


"1: 3 + suma_rekurencyjna(2)" \
"2: 3 + 2 + suma_rekurencyjna(1)" \
"3: 3 + 2 + 1 + sume_rekurencjna(0)" \
"4: 3 + 2 + 1 + 0"


def find(list_in, search, scan_position=0):
    """Wyszukujemy pozycji na liście złożonej z n liczb paramemetry find (list_in, search, scan_position
    list_in = lista w której szukamy
    search = szukana wartość
    scan_posiont default 0, podajemy od której pozycji mamy sprawdzać offset
    """
    if list_in[scan_position] == search:
        print("Znalazłem na pozycji", scan_position)
        return
    elif scan_position == len(list_in) - 1:
        print("Nie znalazłam celu")
        return
    find(list_in, search, scan_position + 1)


def fib_rek(n):
    """
        Funkcja zwraca n-ty wyraz ciągu Fibonacciego.
    """
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fib_rek(n - 1) + fib_rek(n - 2)

def fibbonaci_number(n):
    wynik = []
    a, b = 0, 1
    # while a < n: # ponieważ a podaje pierwszą wartośc z ciągu fibbonaciego będącą najbliżej wartości n
    while len(wynik) < n:  # sprawdzamy długość dict i podajemy faktycznie n-tą wartość ciągu
        wynik.append(a)
        a, b = b, a + b
    return wynik


def list_max(list_in):
    list_in.sort()
    return list_in[len(list_in) - 1]


def list_max_for(list_in):
    temp_max = list_in[0]
    for number in list_in:
        if temp_max < number:
            temp_max = number
    return temp_max


def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


def find_two(lista):
    count = 0
    for n in lista:
        if str(n)[0] == str(n)[-1] and len(str(n)) == 3:
            count += 1
    return count

def keyselect(n):
    return n[-1]


def sort_krotka(tuples):
    # sortowanie krotki po wartosci key gdzie key musi być fukcja, wybieramy z listy krotek daną krotkę i sprawdzamy wzór z
    # keyselect
    return sorted(tuples, key=keyselect) # keyselect to musi byc funcja
def connect_leter(word):
    if len(word)>=2:
        print(word[0:2]+word[len(word)-2:len(word)])
    else:
        print("Za krótkie")
"""REKURENCEJE"""
def silnia(n):
    if n > 1:
        return n * silnia(n - 1)
    elif n in (0, 1):
        return 1
def silnia_second(n):
    if n == 0:
        return 1
    else:
        return n * silnia_second(n-1)

class FibonacciClass:

    def __init__(self):
        self.cache = {0:0, 1:1}

    def __call__(self, n):
        if n not in self.cache:
            self.cache[n] = self(n-1) + self(n-2)
        return self.cache[n]
def fib_cache(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fib_cache(n - 1) + fib_cache(n - 2)
    return cache[n]

# fibonacci = FibonacciClass()
# print ( fibonacci(10) )
# print ( fibonacci(200) )
# print ( fibonacci.cache )   # podgląd zapamiętanych wyników


if __name__ == "__main__":
    pass
    # print(list_max([-15, -200, -3, -444, -2000]))
    # print(list_max_for([-15, -200, -3, -444, -2000]))
    # print(fib_rek(10))
    #print(char_frequency('google.com'))
    #print(find_two(['aba', 'aaaa', 'bda', 1000, 'olo', 'aba']))
    #lista_krotek = [(1,3, 2), (2,2, 4), (2,3, 3), (0,4, 3)]
    #print(sort_krotka(lista_krotek))
    #connect_leter("Pyton")
    #print(silnia(1))
    #print(silnia_second(1))
    print(fib_cache(40)) # fibo z cache


