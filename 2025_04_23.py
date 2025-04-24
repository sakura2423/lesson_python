# def print_divisors(n: int) -> None:
#     for i in range(1, n + 1):
#         if n % i == 0:
#             print(i, end=' ')
# n = int(input())
# print_divisors(n)
# import random
#
#
# def guess_game() -> None:
#     secret = random.randint(1, 100)
#     print('Я загадал число от 1 до 100. Попробуй угадать!')
#     input_num = int(input('Твоя догадка: '))
#     n = 1
#     while secret != input_num:
#         if secret > input_num:
#             print('Слишком маленькое')
#         elif secret < input_num:
#             print('Слишком большое')
#         n += 1
#         input_num = int(input('Твоя догадка: '))
#     print(f'Правильно! Ты угадал с {n} попытки.')
# guess_game()


