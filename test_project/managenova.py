# num = int(input('Enter num: '))
# choice = int(input('1 - count \n2 - summa \n3 - average \n4 - number of zeros \nChoice: '))
# while choice not in range(1, 5):
#     print('\nВыберите из предлож вариантов: ' )
#     choice = int(input('1 - count of numbers\n2 - summa\n3 - average\n4 - number of zeros\nChoice: '))
# count = 0
# summa = 0
# zeros = 0
# while num != 0:
#     c = num % 10
#     summa += c
#     count += 1
#     if c == 0:
#         zeros += 1
#     num = num // 10
# if choice == 1:
#     print('Count:', count)
# elif choice == 2:
#     print('Summa:', summa)
# elif choice == 3:
#     print('Average:', summa / count)
# elif choice == 4:
#     print('Zeros:', zeros)


# task 2
# size = int(input('Enter size: '))
# for j in range(8):
#     for i in range(size):
#         if j % 2 == 0:
#             print((' * ' * size + ' _ ' * size) * 4) 
#         else:
#             print((' _ ' * size + ' * ' * size) * 4)

# task 3
from random import randint
choice = int(input('1 - easy\n2 - medium\n3 - hard'))
score = 0
if choice == 1:
    for i in range(3):
        n1 = randint(1, 10)
        n2 = randint(1, 10)
        print(n1, '*', n2, '=', end=' ')
        answer = int(input())
        if answer == n1 * n2:
            print('всё решено правильно')
            score += 1
        else:
            print('что решено не правильнонеправильно')
    print(score)
if choice == 2:
    for i in range(3):
        n1 = randint(1, 10)
        n2 = randint(1, 5)
        print(n1, '**', n2, '=', end=' ')
        answer = int(input())
        if answer == n1 ** n2:
            print('всё решено')
            score += 1
        else:
            print('что-то не правильно')
    print(score)

if choice == 3:
    for i in range(3):
        n1 = randint(1, 10)
        n2 = randint(1, 5)
        print(n1, '%', n2, '=', end=' ')
        answer = int(input())
        if answer == n1 % n2:
            print('всё решено')
            score += 1
        else:
            print('что-то не правильно')
    print(score)