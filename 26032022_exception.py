def first_try(num1, num2):
    try:
        c = num1 / num2
    except ArithmeticError:
        return "Nie dzieli się przez zero"
    except BaseException as err:
        return err
    if c == 2:
        raise NameError("Znalazłem 2 kę :( ")
    return c


# raise podnosi/ wywołuje nasz personalizowany wyjątek mimo dobrze działającego programu, czyli po prostu zwróci błąd od razu np wyjątki pobawić się, mimo że kod się wykona dobrze to można podnieśc error
# print(first_try(2,1))
# try:
#     print(first_try(4,2))
# except NameError as err:
#     print(err)
def dodawanie_error():
    while True:
        try:
            first_number = int(input("Podaj liczbę: "))
            second_number = int(input("Podaj drugą liczbę: "))
            print(first_number + second_number)
            break
        except BaseException as err:
            print(err)


# dodawanie_error()
def mnozenie_error():
    while True:
        try:
            first_number = float(input("Podaj liczbę: "))
            second_number = float(input("Podaj drugą liczbę: "))
            print(first_number / second_number)
            break
        except ZeroDivisionError:  # dzielenie przez zero
            print("Nie możesz podzielić przez 0")
        except ValueError as err:
            print("Błąd wartości wymagana wartosc Rzeczywista, użyj . zamiast ,")


# mnozenie_error()
def error_counting():
    list = [1, 2, 3]
    try:
        print(list[0:2])  # matematycznie to oznacza <0,2) czyli ostatni index to granica ale bez niego
    except IndexError:
        print("NIE MA TAKIEGO ELEMENTU")


def open_file(file_name):
    try:
        file = open(file_name, "r")
    except IOError as err:
        print(f"Błąd {err}")
    else:
        print(f"Plik {file_name} posiada {len(file.readline())} wierszy")
        file.close()
#open_file("main.py")

def write_string_file(file_name,string):
    try:
        file = open(file_name, "a+")
        file.writelines(string)
    except IOError as err:
        print(f"Nie można zapisać pliku {file_name}")
    finally:
        file.close()

#write_string_file("text.txt","test\n")



