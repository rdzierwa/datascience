
import math
from math import pi



class Figura:

    def obwod(self):  # L
        """Obliczanie obwodu."""
        raise NotImplementedError

    def pole(self):  # S/P
        """Obliczanie pola powierzchni."""
        raise NotImplementedError

class Kolo(Figura):

    def __init__(self,promien):
        super().__init__()
        self.promien = promien

    def obwod(self):
        return f'Obwód to: {2* pi * self.promien}'

    def pole(self):
        return f'Pole koła to {pi* self.promien**2}'
        


class Kwadrat(Kolo):

    def __init__(self, a, b, promien):
        super().__init__(promien)
        self.a = a
        self.b = b

    def pole_kola(self):
        return f'{super().pole()}'

    def pole(self):
        return f'{self.a*self.b}'

# kolo = Kolo(5)
# print(kolo.obwod())
# print(kolo.pole())

# kw = Kwadrat(4,5,10)

# print(kw.pole_kola())
# print(kw.pole())
