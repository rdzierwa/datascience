class NazwaKlasy():
    """TEST DOKU
    obowiązkowy atrybut             x bez niego nie policzy
    można dodać dodatkowe atrybuty  y - korzystamy dalej """
    def __init__ (self,*args):
        self.rodzaj = args[0]

    def nazwa_metody(self):
        '''Korzysta z pierwsej danej przekazanej do klasy NazwaKlasy'''
        print (self.rodzaj)



C = NazwaKlasy('klocek','kot','zwierzak')

help(NazwaKlasy)