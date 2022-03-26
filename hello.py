import turtle

t = turtle.Turtle()
t.speed(-1)
t.setheading(90)
t.penup()
t.goto(0, -200)
t.pendown()


def gałąź(t, len):
    if len == 0: return
    nt = t.clone()
    nt.forward(50)
    nt.left(20)
    gałąź(nt, len - 1)
    nt.right(40)
    gałąź(nt, len - 1)





def szukaj(lista, cel, pozycja):
    if lista[pozycja] == cel:
        print("Znalazłem na pozycji", pozycja)
        return
    elif pozycja == len(lista) - 1:
        print("Nie znalazłam celu")
        return
    szukaj(lista, cel, pozycja + 1)




if __name__ == "__main__":
    #gałąź(t, 7)
    #window = turtle.Screen()
    #window.exitonclick()
    lista = [1, 3, 7, 11, 13, 17, 23]
    cel = 17
    szukaj(lista, cel, 0)
