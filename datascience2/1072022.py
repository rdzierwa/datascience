"""Napisz definicję klasy Point. Obiekty z tej klasy powinny mieć:
metodę show, aby wyświetlić współrzędne punktu,
metodę move, aby zmienić te współrzędne,
metodę dist, która oblicza odległość między 2 punktami.
Zwróć uwagę, jak można obliczyć odległość między 2 punktami p(p1, p2) i q(q1, q2):
"""
class Point():
    def __init__(self, x_, y_):
        self.x_ = x_
        self.y_ = y_
    def show(self):
        return (self.x_,self.y_)
    def move(self,xprim,yprim):
        self.x_ = self.x_ + xprim
        self.y_ = self.y_ + yprim
    def dist(self,point):
        return ((self.x_- point.x_)**2+(self.y_-point.y_)**2)**1/2

p1 = Point(1,2)
p2 = Point(2,3)

print(p1.show())
print(p2.show())
print(p1.dist(p2))

    