"""2) Создать список словарей с друзьями, где будет 5 полей (сделай на свой выбор, заполнить самостоятельно).
      То есть каждый словарик в списке - друг. Написать функцию, которая создаст xlsx,
      где первая строка "названия полей в словаре", а последующие - друзья"""
import pandas as pd

def exel_friends(*,info: list[dict]):
    df = pd.DataFrame(info)
    df.to_excel("./friends.xlsx", index=False)

if __name__ == "__main__":
    friends = [
        {
            "name": "Александр Петров",
            "age": 28,
            "nickname": "Саша",
            "address": "ул. Ленина, д.15, кв.42",
            "car": "Skoda Octavia"
        },
        {
            "name": "Екатерина Смирнова",
            "age": 24,
            "nickname": "Катя",
            "address": "пр. Победы, д.8, кв.17",
            "car": "Hyundai Solaris"
        },
        {
            "name": "Михаил Иванов",
            "age": 32,
            "nickname": "Миша",
            "address": "ул. Гагарина, д.33, кв.5",
            "car": "Toyota Camry"
        },
        {
            "name": "Ольга Козлова",
            "age": 29,
            "nickname": "Оля",
            "address": "бул. Космонавтов, д.12, кв.89",
            "car": "Kia Rio"
        },
        {
            "name": "Дмитрий Волков",
            "age": 35,
            "nickname": "Дима",
            "address": "пер. Центральный, д.3, кв.14",
            "car": "Lada Vesta"
        }
    ]

    exel_friends(info=friends)


