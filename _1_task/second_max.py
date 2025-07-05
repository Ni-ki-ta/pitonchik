""" 1) Создать список с рандомными числами (пусть размером 10) с помощью random библиотеки, вывести результат.
Затем найти ВТОРОЙ максимум (если максимум 9, то найти следующее по размеру после 9) и также вывести.
"""
import random
from copy import deepcopy

def main():
    listok = [random.randint(0, 10) for x in range(10)]
    first_max_element = max(listok)
    
    copied_list = deepcopy(listok)
    copied_list.sort(reverse=True)

    for index in range(0, len(copied_list)):
        max_element = copied_list[index]
        if index == 0 or max_element == first_max_element:
            continue
        else:
            break


    print(listok)
    print(max_element)




if __name__ == "__main__":
    main()