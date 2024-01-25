import random
n = 10
array = [0]*n
for i in range(n):
    array[i] = random.random()
    
Max = max(array)
print("Максимальное значение:", Max)

Min = min(array)
print("Минимальное значение:", Min)

Avg = sum(array) / len(array)
print("Среднее значение:", Avg)
