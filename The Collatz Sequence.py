def collatz(number):
    if number % 2 == 0:
        result = number // 2

    if number % 2 == 1:
        result = 3 * number + 1
    return result


try:
    number = int(input())

    while True:
        if number != 1:
            number = collatz(number)
            print(number)
        else:
            break
except ValueError:
    print('Strings are not allowed')
