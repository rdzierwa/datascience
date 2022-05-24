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


class DebetAccount(BankAccount):
    """ TO JEST DOCK STRING - TU WPISUJEMY DOKUMENTACJE"""
    def __init__(self,name, stan=0,limit=0):
        #BankAccount.__init__(self,name,stan) # super() po prostu bierze klasę rodzica nie trzeba wpisywać konkretnej nazwy
        # należy usunąc self wtedy
        super().__init__(name,stan)
        self.limit = limit
    def pay_out(self, amount):
        if (self.stan - amount)<(-self.limit):
            print("brak środków")
        else:
            BankAccount.pay_out(self,amount)

account = DebetAccount("USZATEK",0,1000)

class A:
    """Rodzic pierwszy"""

    def __init__(self):
        #super().__init__()
        self.a = "A"

    def fa(self):
        print("a:", self.a)


class B:
    """Rodzic drugi"""

    def __init__(self):
        super().__init__() # musi być żeby nadpisać się, gdyż B dziedziczy po A w pochodna
        self.b = "B"


    def fb(self):
        print("b:", self.b)


class Pochodna(B, A):
    """Dziecko"""

    def __init__(self):
        super().__init__()

#child = Pochodna()
#print(child.b)

import math


class Figura:
    def obwod(self):  # L
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        raise NotImplementedError














