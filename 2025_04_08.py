# first_name = input('enter your name: ')
# last_name = input('enter your last name: ')
age = int(input(' enter your age: '))

if 0 < age < 7:
    print('ты слишком мал')
elif 0 < age < 18:
    print('вам доступны школьные ресурсы')
elif 0 < age <= 60:
    print('вам доступны курсы повышения квалификации')
elif 0 < age > 60:
    print('обратитесь в пенсионный фонд')
else:
    print('некорретно введены данные')
