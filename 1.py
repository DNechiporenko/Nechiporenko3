import random
amount=int(input("Введите количество чисел в массиве: "))
if amount==0 or amount<0:
    print("Вы ввели ноль или отрицательное число для количества чисел в массиве. Пожалуйста, перезупустите программу и введите положительное число.")
arr=[]
for i in range(amount):
    arr.append(random.randint(0,100))
if amount>0:
    mx=0
    for i in arr:
        if i>mx:
            mx=i
    m=mx
    arr=arr[:arr.index(m) +1 ]+[0]*(len(arr)-len(arr[:arr.index(m) +1 ]))
    print(arr)
