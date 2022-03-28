def file_open_main():
    file = open("text.txt", "r")

    line = file.readline()
    print(line)

    file.seek(0, 0)
    line = file.readline()

    print(file.tell())  # w którym miejscu w pliku jesteśmy
    file.seek(len(line) + 1,
              0)  # pierwsza liczba to numer elementu w pliku, druga liczba to od kąd liczymy, 0 od początku,
    # 1 bezwzględna, od końca
    line = file.readline()
    print(line)
    file.close()


def file_open_full(name):
    file = open(name, "r")
    data_from_file = file.read()
    file.close()
    return data_from_file



def file_to_list(name):
    with open(name,"r") as file:
        list_from_file = file.readlines()
    return list_from_file


#print(file_to_list("text.txt"))


def file_to_var(name):
    with open(name,"r") as file:
        var_from_file = file.read()
    return var_from_file


#print (file_to_var("text.txt"))
# value = list()
# with open("text.txt", "r") as file:
#     for line in file.readlines():
#         value.append(line)
# print(value)
def czytanie_pliku():
    content_array = []
    with open('text.txt') as fp:
        line = fp.readline()

        while line:
            content_array.append(line)
            line = fp.readline()
    print(content_array)

def read_file():
    value = list()
    with open("text.txt", "r") as file:
        for line in file.readlines():
            value.append(line)
    print(value)