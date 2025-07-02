''' 5) Создать вручную txt файл с несколькими строчками, не забудь цифры спрятать среди строк.
Написать функцию, которая считает файл и возьмем только цифры оттуда и сложит их, вернет сумму.
'''


def sum_txt(*,
            file_name: str) -> int:
    summa = 0
    with open("./" + file_name, "r") as file:
        info = file.read()
        for element in info:
            if element.isdigit():
                summa += int(element)

    return summa


if __name__ == "__main__":
    file_name = "file.txt"
    summa = sum_txt(file_name=file_name)

    print(summa)
