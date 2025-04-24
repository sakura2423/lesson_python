# a = input()
# for i in a:
#     print(i, end=' ')


# result = ["" for i in range(1,21) ]
# for i in range(1,21):
#     for j in range(0,20):
#         result[j] += f"{i} x {j + 1} = {i * (j + 1)}"
#         if i * (j + 1) // 10 == 0:
#             result[j] += '   | '
#         elif i * (j + 1) // 100 == 0:
#             result[j] += '  | '
#         else:
#             result[j] += ' | '
# for i in result:
#     print(i)


s1 = input()
x, y = s1.split(' ')
x = int(x)
y = int(y)

if (x == -2 or x == 2) and (-3 <= y <= 5):
    print('B')
elif (y == -3 or y == 5) and (-2 <= x <= 2):
    print('B')
elif (x == -4 or x == 4) and (-4 <= y <= -3):
    print('B')
elif (y == -4 or y == -3) and (-4 <= x <= 4):
    print('B')
elif x ** 2 + (y-5) ** 2 == 25 and y >= 5:
    print('B')
elif x ** 2 + (y-5) ** 2 < 25 and y > 0:
    print('R')
elif -2 < x < 2 and -3 < y < 5:
    print('Y')
elif -4 < x < 4 and -4 < y < -3:
    print('B')
else:
    print("W")
