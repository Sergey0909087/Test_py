# number = 7
# divers = 0
# for i in range(1, number + 1):
#     if number % i == 0:
#         divers += 1
# print(divers)
# if divers == 2:
#     print('простое число')
# else:
#     print('число не простое')

# Задача 1
size = int(input("Enter size: "))
for i in range(size):
    print(' * ' * size)

#Задача 2
side_1 = int(input("Enter first side: "))
side_2 = int(input("Enter second side: "))
for i in range(side_1):
    print(' * ' * side_2)

# Задача 3
size = int(input("Enter size: "))
print(' * ' * (size))
for i in range(size - 2):
    print(' * ' + '   ' * (size - 2) + ' * ')
print(' * ' * (size))

# Задание 4

dlina_1 = int(input("введи длину: "))
shirina = int(input("введи ширину: "))
print(' * ' * (dlina_1))
for i in range(shirina - 2):
    print(' * ' + '   ' * (dlina_1 - 2) + ' * ')
print(' * ' * (dlina_1))