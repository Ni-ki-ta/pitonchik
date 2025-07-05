# 3) Написать функцию, которая позволяет посчитать сумму цифр числа, двумя способами (через str и через while)

def while_sum(*, number: int) -> int:
    summa = 0
    while number > 0:
        k = number % 10
        summa += k
        number = int(number / 10)
    return summa

def str_sum(*, number: str) -> int:
    number = list(number)
    summa = [int(digit) for digit in number]
    return sum(summa)


if __name__ == "__main__":
    num = 123456
    print(while_sum(number=num))
    num = str(num)
    print(str_sum(number=num))


