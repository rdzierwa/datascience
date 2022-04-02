class NazwaKlasy():
    """TEST DOKU
    obowiązkowy atrybut             x bez niego nie policzy
    można dodać dodatkowe atrybuty  y - korzystamy dalej """

    def __init__(self, *args):
        self.rodzaj = args[0]

    def nazwa_metody(self):
        '''Korzysta z pierwsej danej przekazanej do klasy NazwaKlasy'''
        print(self.rodzaj)


class Parrot:

    # atrybuty instancji
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # metoda instancji
    def sing(self, song):
        return self.name + " śpiewa " + song

    def dance(self):
        return self.name + " teraz tańczy"


blu = Parrot("Blu", 10)
print(blu.sing("'Happy'"))
print(blu.dance())


class Person():
    def __init__(self, name,
                 age):  # nie musi się nazywać jako self, po prostu musi być pierwszy ale wzorce mówią że ma być self
        self.name = name
        self.age = age


class PersonSecond():
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(self):
        print(f'{self.name} ma lat {self.age}')


p1 = PersonSecond('Jan', 31)
# del(p1.age) # usuwa każdy obiekt !!!ggg

p1.myfunc()
p1.myfunc()


class MyClass():
    x = 5


p1 = MyClass()
print(p1.x)
print(MyClass().x)


class BankAccount():
    def __init__(self, name, stan=0):
        self.name = name
        self.stan = stan

    def info(self):
        print(f"Nazwa konta:{self.name}")
        print(f"Stan konta:{self.stan}")

    def pay_in(self, amount):
        self.stan += amount

    def pay_out(self, amount):
        self.stan -= amount


jk = BankAccount("USZATEK", 1000)
jk.info()
jk.pay_in(1000)
jk.info()


class Jets:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.origin = kwargs['country']


first_item = Jets(name="F16", country="USA")
print(first_item.origin)


class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.name = name
        self.origin = country


first_item = Jets("F16", "USA")

a = first_item.name
b = first_item.origin

print(f"{a} zakupione od {b}")
