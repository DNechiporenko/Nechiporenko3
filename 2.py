import random
amount1=int(input("Введите размерность первого массива: "))
amount2=int(input("Введите размерность второго массива: "))
arra=[]
arrb=[]
for i in range(amount1):
    arra.append(random.randint(0,100))
for x in range(amount2):
    arrb.append(random.randint(0,100))
print("Общие элементы массивов:")
for m in (arra):
    if m in arrb:
        print(m)
print("Если числа не появились на экране, значит общих элементов нет")
