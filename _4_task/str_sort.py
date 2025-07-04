""" 4) Создать самостоятельно список с 10ю строчками различной длины, отсортировать по длине строки.
 Вывести результат до и после. Затем, сделать каждую строчку в списке, чтобы она начиналась с большой буквы.
 В этом задании 2е функции реализуй """
import random


def sort_list_str(*,
                  listok: list[str]) -> list[str]:
    listok.sort(key=lambda element: len(element))

    return listok


def frst_up(*,
            listok: list[str]) -> list[str]:
    helper = ''
    listek = []
    for element in listok:
        helper = element.capitalize()
        listek.append(helper)
        helper = ''

    return listek


if __name__ == "__main__":
    listek = []
    element = ''
    for j in range(10):
        amount = random.randint(5, 20)
        for i in range(amount):
            element += chr(random.randint(97, 122))
        listek.append(element)
        element = ''

    print(listek)
    sort_list_str(listok=listek)
    print(listek)

    listek = frst_up(listok=listek)
    print(listek)
