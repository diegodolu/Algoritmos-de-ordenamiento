import time
import random
import matplotlib.pyplot as plt

# Selection Sort

# Complejidad de tiempo: O(n^2)
# Complejidad de tiempo: O(1)

# Complejidad de tiempo: Θ(n^2)
# Complejidad de tiempo: Θ(1)

# Complejidad de tiempo: Ω(n^2)
# Complejidad de tiempo: Ω(1)

array = [3,8,10,12,4,1,19,0]

def selectionSort(array):
    for i in range(len(array)-1):
        min = i

        for j in range(i+1,len(array)):
            if array[j] < array[min]:
                min = j
        
        temp = array[i]
        array[i] =  array[min]
        array[min] = temp


print(array)
selectionSort(array)
print(array)






# Benchmarking:

# Se crearan arrays con contenido aleatorio con números del 1 al 100,el tamaño 
# será de 100, 200, 400, 800, 1600, 3200, 6400, 12800 y 25600 valores, a los
# cuales se les aplicará el Selection Sort.

# arr = []
# inicio = 0
# fin = 0
# length = 0

# for i in range(14):
#     for j in range(0,pow(2,i)):
#         arr.append(random.randint(1,100))
#     length = len(arr)


#     # Cálculo del tiempo:
#     inicio = time.time()
#     selectionSort(arr)
#     fin = time.time()


#     # Vaciando el array
#     arr.clear()

#     # Calculando el tiempo de ejecución
#     tiempo = fin-inicio
#     print(f'Longitud del array: {length}')
#     print ("{0:.15f}".format(tiempo))




""" Implementación Matplotlib"""

# array_sizes = [10, 100, 1000, 5000]
# best_case_times = []
# worst_case_times = []

# for size in array_sizes:
#     arr_best = list(range(size))
#     arr_worst = list(range(size, 0, -1))

#     # Mejor de los casos
#     start_time = time.time()
#     selectionSort(arr_best)
#     end_time = time.time()
#     best_case_times.append(end_time - start_time)

#     # El peor de los casos
#     start_time = time.time()
#     selectionSort(arr_worst)
#     end_time = time.time()
#     worst_case_times.append(end_time - start_time)

# plt.plot(array_sizes, best_case_times, label='Mejor de los casos')
# plt.plot(array_sizes, worst_case_times, label='El peor de los casos')
# plt.xlabel('Tamaño del array')
# plt.ylabel('Tiempo (segundos)')
# plt.title('Selection Sort el mejor y peor caso')
# plt.legend()
# plt.show()