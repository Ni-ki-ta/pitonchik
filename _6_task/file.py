''' 6) Задача со *, реализовать функцию создания такого файлика кодом,
    где можно задать кол-во строк в файле и кол-во цифр.'''
import random


def create_file(*,
                file_name: str, line_amount_c: int, digit_amount_c: int) -> None:
    remaining_digits = digit_amount_c
    digit_amount_line = int(remaining_digits / line_amount_c)
    print(digit_amount_line)
    with open("./" + file_name, "w") as file:
        for line in range(line_amount_c):
            if line != 0:
                file.write('\n')
            if remaining_digits > 0:
                if line == line_amount_c - 1:
                    digit_amount_line = remaining_digits

                for _ in range(digit_amount_line):
                    file.write(str(random.randint(0, 9)))



            remaining_digits -= digit_amount_line





if __name__ == "__main__":
    file_name = "txt_file.txt"
    create_file(file_name=file_name, line_amount_c=10, digit_amount_c=15)
