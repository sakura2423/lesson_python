# choice = input('что вы хотите вычислить? 1 - катет 2 - гипотинуза: ')
# if choice == '1':
#     katet = float(input('введите длину катета: '))
#     gipotenuza = float(input('введите длину гипотенузы: '))
#     print((gipotenuza ** 2 - katet ** 2) ** 0.5)
# elif choice == '2':
#     katet_1 = float(input('введите длину катета_1: '))
#     katet_2 = float(input('введите длину катета_2: '))
#     print((katet_1 ** 2 + katet_2 ** 2) ** 0.5 )
# else:
#     print('нет такого варианта ответа')

i = 0
while i <= 100:
    if i % 2 == 0 and i % 4 == 0 and i % 8 == 0 and i % 16 == 0:
        print(i)
    i += 1
