def procent(inwestycja, lata, oprocentowanie):
    a = 0
    per = oprocentowanie / 100
    try:
        while a < lata:
            inwestycja = inwestycja + (inwestycja * per)
            a = a + 1
    except:
        inwestycja = "Błędne dane"
    return inwestycja


def whatyourename(name, lata):
    print(f"Cześć {name} Cieszę się że masz: {lata}")


if __name__ == '__main__':
    # name = input("Jak masz na imie: ")
    # lata = input("Ile masz lat: ")
    # whatyourename(name, int(lata))
    inwestycja = input("podaj kwotę: ")
    lata = input("podaj lata: ")
    oprocentowanie = input("podaj oprocentowanie jako XX %: ")
    oprocentowanie = oprocentowanie.replace(',', '.')
    if (oprocentowanie and lata and inwestycja):
        print(procent(float(inwestycja), int(lata), float(oprocentowanie)))
    else:
        print("nie podałeś wszystkich danych")
