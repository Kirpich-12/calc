#ввод данных
#4 функции(+-/*)
vvod = input()
operants = []

def addition(a:int, b:int) -> int:
    return a + b
    
def subtraction(a:int, b:int) -> int:
    return a - b

def multiplication(a:int, b:int) -> int:
    if a == 0:
        a = 1
    return a * b

def division(a:int, b:int) -> int:
    if a == 0:
        a = 1
    return a / b


def sepor(string:str, seporator:str) -> list:
    ans_s =[]
    ans = string.split(seporator)
    for i in range(len(ans)):
        if ans[i] != '':
            ans_s.append(ans[i])            
    for i in range(len(ans_s)):
        ans_s[i] = float(ans_s[i])
    return ans_s




while ('-' in vvod) or ('+' in vvod) or ('*'in vvod)  or ('/' in vvod):
    print('True')
    for i in vvod :                     #Разделение строки на числа
        if i =='+' or i=='-' or i=='*' or i=='/':
            operants.append(i)
            vvod = vvod.replace(i, '')
    numbers = vvod
    print(vvod)
    print(operants)

list_num = sepor(numbers, ' ')

amount = len(list_num)
final_i = 0
print(list_num)

fn = 1
n2 = numbers[0]

for operant in operants:
    i = 1
    if operant == '+':
        fn = addition(fn, list_num[i])
        i += 1
    elif operant == '-':
        fn = subtraction(fn, list_num[i])
        i += 1
    elif operant == '*':
        fn = subtraction(fn, list_num[i])
        i += 1
    elif operant == '/':
        fn = division(fn, list_num[i])
        i += 1
    print(fn)
print(fn)
        
        


