class Algoritmos:

    @staticmethod
    def suma_gauss(n):
        return n * (n + 1) // 2

    @staticmethod
    def fibonacci_recursivo(n):
        if n <= 1:
            return n
        return Algoritmos.fibonacci_recursivo(n - 1) + Algoritmos.fibonacci_recursivo(n - 2)

    @staticmethod
    def fibonacci_iterativo(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    @staticmethod
    def fibonacci_memorizacion(n, memo=None):
        if memo is None:
            memo = {0: 0, 1: 1}
        if n not in memo:
            memo[n] = Algoritmos.fibonacci_memorizacion(n - 1, memo) + Algoritmos.fibonacci_memorizacion(n - 2, memo)
        return memo[n]

    @staticmethod
    def fibonacci_matrices(n):
        import numpy as np

        def matrix_mult(A, B):
            return np.dot(A, B).tolist()

        def matrix_pow(mat, p):
            result = [[1, 0], [0, 1]]  # Matriz identidad
            base = mat

            while p > 0:
                if p % 2 == 1:
                    result = matrix_mult(result, base)
                base = matrix_mult(base, base)
                p //= 2

            return result

        F = [[1, 1], [1, 0]]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = matrix_pow(F, n - 1)
            return result[0][0]

    @staticmethod
    def es_primo(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    @staticmethod
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            Algoritmos.merge_sort(L)
            Algoritmos.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    @staticmethod
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return Algoritmos.quick_sort(left) + middle + Algoritmos.quick_sort(right)

    @staticmethod
    def busqueda_binaria(arr, x):
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    @staticmethod
    def criba_eratostenes(n):
        primos = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if primos[p]:
                for i in range(p * p, n + 1, p):
                    primos[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primos[p]]

    @staticmethod
    def dijkstra(grafo, inicio):
        import heapq

        D = {v: float('inf') for v in grafo}
        D[inicio] = 0
        pq = [(0, inicio)]

        while pq:
            (dist, current_vertex) = heapq.heappop(pq)
            if dist > D[current_vertex]:
                continue
            for vecino, peso in grafo[current_vertex].items():
                distance = dist + peso
                if distance < D[vecino]:
                    D[vecino] = distance
                    heapq.heappush(pq, (distance, vecino))
        return D

def main():
    print("Suma Gauss de los primeros 10 números:", Algoritmos.suma_gauss(10))
    print("10º número de Fibonacci (Recursivo):", Algoritmos.fibonacci_recursivo(10))
    print("10º número de Fibonacci (Iterativo):", Algoritmos.fibonacci_iterativo(10))
    print("10º número de Fibonacci (Memorización):", Algoritmos.fibonacci_memorizacion(10))
    print("10º número de Fibonacci (Matrices):", Algoritmos.fibonacci_matrices(10))
    print("¿Es 29 un número primo?:", Algoritmos.es_primo(29))

    arr = [12, 11, 13, 5, 6, 7]
    Algoritmos.merge_sort(arr)
    print("Array ordenado con Merge Sort:", arr)

    arr = [12, 11, 13, 5, 6, 7]
    print("Array ordenado con Quick Sort:", Algoritmos.quick_sort(arr))

    arr = [2, 3, 4, 10, 40]
    x = 10
    result = Algoritmos.busqueda_binaria(arr, x)
    print("Elemento encontrado en el índice" if result != -1 else "Elemento no encontrado", result)

    print("Números primos menores que 30:", Algoritmos.criba_eratostenes(30))

    grafo = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    inicio = 'A'
    print("Distancias desde A:", Algoritmos.dijkstra(grafo, inicio))

if __name__ == "__main__":
    main()
