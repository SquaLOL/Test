import math


# def min_value(a,b):
#     if a < b:
#         return a
#     else:
#         return b
#
#
#
# print(min_value(3,2))
#
# array = [10,4,5,1,8]
array = [8,3,5,12,25]

def array_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j + 1] < array[j]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array



array.append(123)
array.pop()
array.append(27)
print(array_sort(array))
#
#
# # num1 = int(input("Введите первое число: "))
# #
# # num2 = int(input("Введите второе число: "))
# #
# # print("Result", num1 * num2)
#
#
# user_data = int(input("Введите число"))

# if user_data != 5:
#     print("All Good")
#     if user_data > 6:
#         print("Number is bigger than 5")

# Написать функцию которая возвращает число фибоначи по N elemet()!!!


# def anti (n):
#     if n < 2:
#         return n
#     return anti(n - 1) + anti(n - 2)

def fibo (n):
    if n == 0:
        return 0
    elif n == 1 or n == -1:
        return 1
    if n > 0:
        return fibo(n - 1) + fibo(n - 2)
    else:
        return (-1)**((n * -1) + 1) * fibo(n * -1)

print(fibo(-10))


# Палиндром

abs = "alla"
qat = "Nicolas"

def pld (abs):
    abs = abs.lower()
    return abs == abs[::-1]

print(pld(abs))

# n = 1
# *
#
# n = 2
#  *
# ***
#
# n = 3
#   *
#  ***
# *****
#
# n = 4
#    *
#   ***
#  *****
# *******


def star_tree(n):
    for i in range(n):
        print(i)


print(star_tree(1))


# data = input()
#
# numer = 5 if data == "Five" else 0
# # if data == "Five":
# #     number = 5
# # else:
# #     number = 0
#
# print(numer)



def find_symbol(a, word):
    found = None
    for i in word:
     if i == a:
        found = True
        break
     else:
        found = False
    return found

print(find_symbol("k", 'koa,'))


arr = [5, 6, 7, 8, True ]
# arr.insert(1, "hi")
arr.sort()
arr.pop()
arr.remove(5)
# arr.clear()
print(arr)

for i in arr:
    print(i)

word = "Football,bastketball,skate"

print(word.split(','))


data = (4,6,7,3,6,True,5.6 , "Hello")
# data[0] = 5 -- NO
for i in data:
    print(i)







country = {"code": 'US', 'name': 'Russian'}
# country = dict(code='RU', name='Russian')
# country.pop('name')

print(country.items())

person = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Bobby',
        'age': 56,
        'address': ('Moscow', 'red square street' , '45'),
        'gredes': { 5 }
    },
    'user_2': {
    }
}


print(person['user_1']['address'][0])