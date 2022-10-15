import random
arr=[]
amount=int(input("Введите количество элементов в массиве: "))
for x in range(amount):
    arr.append(random.randint(0,100))
delta=int(input("Введите любое число от 2 до 50: "))
mn=99999
for i in arr:
    if mn>i:
        mn=i
k=0
for i in range(len(arr)):
    if i==mn+delta:
        k+=1
print(arr,mn)
print(k)

    
