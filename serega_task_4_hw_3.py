earth_days, earth_hours = map(int, input('Введите земные дни и часы: ').split(', '))
sol = (earth_days + earth_hours / 24) * 1.02595675
sol_2 = round(sol, 2)
print('Количество солов: ', sol_2)
