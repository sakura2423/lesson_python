# n = int(input())
# count = 0
# for i in range(0,n):
#     o = int(input())
#     if o % 2 == 0:
#         count += 1
# print(count)


import random
random_n = random.randint(1,100)
n = int(input())
while n != random_n:
    if n < random_n:
        print('искомое число больше')
    elif n > random_n:
        print('искомое число меньше')
    n = int(input())
print('вы выиграли! искомое число', random_n)

