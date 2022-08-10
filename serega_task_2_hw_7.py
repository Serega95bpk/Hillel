month_number = int(input('Какой месяц вас интересует:\n'))
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]


def season(month):
        if month in winter:
            return 'Зима'
        elif month in spring:
            return 'Весна'
        elif month in summer:
            return 'Лето'
        elif month in autumn:
            return 'Осень'


print(season(month_number))