#ввод данных
#4 функции(+-/*)
vvod = input()


def addition(a:int, b:int) -> int:
    return a + b
    
def subtraction(a:int, b:int) -> int:
    return a - b

def multiplication(a:int, b:int) -> int:
    return a * b

def division(a:int, b:int) -> int:
    return a / b


def sepor(string:str, seporator:str) -> list:
    ans = string.split(seporator)
    for i in range(len(ans)):
        ans[i] = float(ans[i])
    return ans

#TODO отделить простые дейстивия от сложнных 
if '+' in vvod:
    numbers = sepor(vvod, '+')
    if len(numbers) == 2:
        print(addition(numbers[0], numbers[1]))
elif '-' in vvod:
    numbers = sepor(vvod, '-')
    if len(numbers) == 2:
        print(subtraction(numbers[0], numbers[1]))
elif '*' in vvod:
    numbers = sepor(vvod, '*')
    if len(numbers) == 2:
        print(multiplication(numbers[0], numbers[1]))
elif '/' in vvod:
    numbers = sepor(vvod, '/')
    if len(numbers) == 2:
        print(division(numbers[0], numbers[1]))
else:
    print('Неверный ввод, попробуйте ещё раз')



