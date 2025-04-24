# объявление функции
def function_name(arg_1, arg_2):
    # инструкции(код функции)
    return None # это возврат функции


# функция запроса ввода пользователя
def function_userinput() -> tuple:
    name = input('enter your name: ')
    age = int(input('enter your age: '))
    return name, age


def age_checker(age: int) -> str:
    if age % 10 == 1 and age % 100 // 10 != 1:
        return 'год'
    elif 1 < age % 10 < 5 and age % 100 // 10 != 1:
        return 'года'
    else:
        return 'лет'


def user_info(user_data: tuple) -> None:
    print(f'имя пользователя: {user_data[0]}')
    print(f'возраст пользователя: {user_data[1]} {age_checker(user_data[1])}')


user = function_userinput()

user_info(user)
user_info(user)
user_info(user)
