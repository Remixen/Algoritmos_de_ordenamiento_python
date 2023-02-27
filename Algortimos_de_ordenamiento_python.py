from random import randint
from timeit import repeat

#Algoritmo de la Burbuja       
def bubble_sort(array):
    n = len(array)
    # Contadores
    comparisons = 0
    assignments = 0

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            comparisons += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                assignments += 1

                already_sorted = False
                
        if already_sorted:
            break
    
    return array
#--------------------------------------------------------------------------------------------------------------------------------------
#Algortimo de Insercion
def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array
#---------------------------------------------------------------------------------------------------------------------------------------------------
#Algortimo de Fusion merge_sort
def merge(left, right):
   
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
       
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))
#----------------------------------------------------------------------------------------------------------------------------------------    
#Algortimo de Seleccion
def selection_sort(array):
    
    tamaño = len(array)
    for i in range(0, tamaño-1):
        minimo = i
        for j in range(i+1, tamaño):
            if array[minimo] > array[j]:
                minimo = j
    auxiliar = array[minimo]
    array[minimo] = array[i]
    array[i] = auxiliar
#----------------------------------------------------------------------------------------------------------------------------------------------
#Algoritmo de ordenamiento rapido Quick_sort
def quick_sort(array):
    
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
    
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quick_sort(low) + same + quick_sort(high)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#Funcion de ejecucion para el algortimo de ordenamiento seleccionado
def run_sorting_algorithm(algorithm, array):
    
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algoritmo: {algorithm}. Tiempo minimo de ejecucion: {min(times)} Segundos ")
    
#Aqui establecemos tanto el algoritmo a ejecutar "algorithm" al igual que el array (array = f = content_list)o archivo a ejecutar de los tres posibles (entrada-800.txt, 8000, 80000).

if __name__ == "__main__":
    f=open("D:\Documentos\Proyectos de Universidad para Github\Algortimia y Complejidad\Laboratorio_1_algoritmos_de_ordenacion\Datos_de_entrada\Entrada-800.txt", "r")
      
    content_list = f.readlines()
    run_sorting_algorithm(algorithm="bubble_sort", array=content_list)
    
    
    
     
   
    