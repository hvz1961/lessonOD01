def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Флаг для оптимизации: если за проход не было обменов, массив уже отсортирован
        swapped = False
        # Последние i элементов уже отсортированы, поэтому их не рассматриваем
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Если не было обменов, массив уже отсортирован
        if not swapped:
            break

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Отсортированный массив:", arr)

# def quicksort(arr):
#     # Базовый случай: если массив пуст или содержит один элемент, он уже отсортирован
#     if len(arr) <= 1:
#         return arr
#
#     # Выбираем опорный элемент (pivot)
#     pivot = arr[len(arr) // 2]
#
#     # Разделяем массив на три части:
#     # 1. Элементы меньше опорного
#     # 2. Элементы равные опорному
#     # 3. Элементы больше опорного
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#
#     # Рекурсивно применяем сортировку к левой и правой частям
#     return quicksort(left) + middle + quicksort(right)
#
# # Пример использования
# arr = [3, 6, 8, 10, 1, 2, 1]
# sorted_arr = quicksort(arr)
# print("Отсортированный массив:", sorted_arr)

# def selection_sort(arr):
#     # Проходим по всем элементам массива
#     for i in range(len(arr)):
#         # Находим индекс минимального элемента в оставшейся части массива
#         min_idx = i
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#
#         # Меняем местами найденный минимальный элемент с текущим элементом
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Пример использования
# arr = [64, 25, 12, 22, 11]
# selection_sort(arr)
# print("Отсортированный массив:", arr)
#

# def insertion_sort(arr):
#     # Проходим по всем элементам массива, начиная со второго
#     for i in range(1, len(arr)):
#         key = arr[i]  # Текущий элемент, который нужно вставить в отсортированную часть
#         j = i - 1
#
#         # Сдвигаем элементы отсортированной части, которые больше key, вправо
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#
#         # Вставляем key в правильную позицию
#         arr[j + 1] = key
#
# # Пример использования
# arr = [12, 11, 13, 5, 6]
# insertion_sort(arr)
# print("Отсортированный массив:", arr)