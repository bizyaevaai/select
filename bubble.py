import random
DIM = 20
arr = [random.randint(0, 100) for i in range(DIM)]
print("Исходный массив")
print(arr)
n = 1
alg_count = [0, 0]
while n < DIM:
    for i in range(DIM - n):
        alg_count[0] += 1
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            alg_count[1] += 1
    n += 1
print("\nУпорядоченный массив: метод пузырька")
print(arr)
print("\nЭлементов в массиве: ", DIM)
print("Сравнений: ", alg_count[1])
print("Перестановок: ", alg_count[0])
