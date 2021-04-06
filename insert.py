import random
DIM = 20
arr = [random.randint(0, 100) for i in range(DIM)]
print("Исходный массив")
print(arr)
alg_count = [0, 0]
for i in range(1, DIM):  # Основной цикл со 2-го элемента право
    temp = arr[i]  # Запомним элемент для сравнения
    j = i - 1
    while j >= 0:  # Ищем влево ближайший меньший
        alg_count[0] += 1  # Считаем операции сравнения
        if arr[j] > temp:
            alg_count[1] += 1  # Считаем операции перестановки
            arr[j + 1] = arr[j]  # Сдвигаем элемент влево, а на его место ставим наименьший
            arr[j] = temp
        j -= 1
print("\nУпорядоченный массив: метод простой вставки")
print(arr)
print("\nЭлементов в массиве: ", DIM)
print("Сравнений: ", alg_count[1])
print("Перестановок: ", alg_count[0])
