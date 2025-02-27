#Calculator
#==========

#Libs import
import string

def add(a, b):         #Сложение
    return a+b

def multiply(a, b):    #Умножение
    return a*b

def division(a, b):    #Деление
    return a/b

def subtract(a, b):    #Вычитание
    return a-b

def degree(a, b):      #Степень
    final=a
    for i in range (1, b):
        final=final*a
    return final

def factorial(a):       #Факториал
    a=int(a)
    final1=1
    print(a)
    for i in range (1, a+1):
        final1=final1*i
        print(i)
        print(final1)
    return final1

def main():
    #Input block
    print("Введите то, что надо найти:")
    inp=input()
    inplen=len(inp)

    #Dividing into symbs block
    list_1=[]
    for i in range (0, inplen):
        list_1.append(inp[i])
    kol=0
    for i in list_1:
        if i == '+' or i == '-' or i == '*' or i == '/' or i == '^' or i == '!':
            kol+=1
    list_z=[0]*kol
    list_c=[0]*(kol+1)
    z=0
    c=0
    for i in list_1:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
            list_c[c]=list_c[c]*10+int(i)
        elif i == '+' or i == '-' or i == '*' or i == '/' or i == '^' or i == '!':
            c+=1
            list_z[z]=i
            z+=1

    #Searching for factorial block(not working)
    c=0
    fact=0
    for i in list_z:
        if i == '!' :
            fact=1
            c+=1 
            break
        else: c+=1
    #print(c)

    #String==>Float
    kol=len(list_c)
    for i in range(0, kol):
        list_c[i]=float(list_c[i])

    #Using functions block
    final=54531534351146131365446121316541
    if fact == 1 :
        final=factorial(list_c[c])
    else:
            final=list_c[0]
            z=0
            listclen=len(list_c)
            for c in range (1, listclen):
                if list_z[z] == '+': final=add(final, list_c[c])
                elif list_z[z] == '-': final=subtract(final, list_c[c])
                elif list_z[z] == '*': final=multiply(final, list_c[c])
                elif list_z[z] == '/': final=division(final, list_c[c])
                z+=1
    
    #Output block
    final=str(final)
    finallen=len(final)
    final_new=final
    if final[finallen-1]=='0' : final_new=final[:-2]
    if final=='54531534351146131365446121316541' : final_new="Ты че, чучело, вводи нормально"
    print('Результат вашего действия:', final_new)

if __name__=='__main__':
    main()