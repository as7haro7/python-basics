class EstructurasDeDatos:

    @staticmethod
    def listas():
        lista = [1, 2, 3, 4, 5]
        lista.append(6)
        lista.insert(2, 2.5)
        lista.remove(2.5)
        lista.sort()
        lista.reverse()
        longitud = len(lista)
        elemento = lista[2]

        print("Lista:", lista)
        print("Longitud de la lista:", longitud)
        print("Elemento en la posición 2:", elemento)

    @staticmethod
    def colas():
        from collections import deque
        cola = deque([1, 2, 3, 4, 5])
        cola.append(6)
        cola.popleft()
        longitud = len(cola)
        primero = cola[0]

        print("Cola:", list(cola))
        print("Longitud de la cola:", longitud)
        print("Primer elemento:", primero)

    @staticmethod
    def pilas():
        pila = [1, 2, 3, 4, 5]
        pila.append(6)
        pila.pop()
        longitud = len(pila)
        superior = pila[-1]

        print("Pila:", pila)
        print("Longitud de la pila:", longitud)
        print("Elemento superior:", superior)

    @staticmethod
    def conjuntos():
        conjunto = {1, 2, 3, 4, 5}
        conjunto.add(6)
        conjunto.remove(6)
        longitud = len(conjunto)
        esta_en_conjunto = 3 in conjunto

        print("Conjunto:", conjunto)
        print("Longitud del conjunto:", longitud)
        print("¿El 3 está en el conjunto?:", esta_en_conjunto)

    @staticmethod
    def diccionarios():
        diccionario = {'a': 1, 'b': 2, 'c': 3}
        diccionario['d'] = 4
        del diccionario['d']
        longitud = len(diccionario)
        valor = diccionario['a']
        claves = list(diccionario.keys())
        valores = list(diccionario.values())

        print("Diccionario:", diccionario)
        print("Longitud del diccionario:", longitud)
        print("Valor de la clave 'a':", valor)
        print("Claves del diccionario:", claves)
        print("Valores del diccionario:", valores)

    @staticmethod
    def cadenas():
        cadena = "Hola, mundo!"
        longitud = len(cadena)
        caracter = cadena[1]
        partes = cadena.split(", ")
        reemplazada = cadena.replace("mundo", "Python")
        mayusculas = cadena.upper()
        minusculas = cadena.lower()
        sin_espacios = cadena.strip()
        empieza_con = cadena.startswith("Hola")
        termina_con = cadena.endswith("mundo!")

        print("Cadena original:", cadena)
        print("Longitud de la cadena:", longitud)
        print("Carácter en la posición 1:", caracter)
        print("Partes de la cadena:", partes)
        print("Cadena reemplazada:", reemplazada)
        print("Cadena en mayúsculas:", mayusculas)
        print("Cadena en minúsculas:", minusculas)
        print("Cadena sin espacios en blanco:", sin_espacios)
        print("¿Empieza con 'Hola'?:", empieza_con)
        print("¿Termina con 'mundo!'?:", termina_con)

    @staticmethod
    def busqueda_secuencial(lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    @staticmethod
    def busqueda_binaria(lista, x):
        l, r = 0, len(lista) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if lista[mid] == x:
                return mid
            elif lista[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    @staticmethod
    def ordenamiento_burbuja(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    @staticmethod
    def ordenamiento_insercion(lista):
        for i in range(1, len(lista)):
            key = lista[i]
            j = i - 1
            while j >= 0 and key < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = key
        return lista

    @staticmethod
    def ordenamiento_seleccion(lista):
        for i in range(len(lista)):
            min_idx = i
            for j in range(i + 1, len(lista)):
                if lista[min_idx] > lista[j]:
                    min_idx = j
            lista[i], lista[min_idx] = lista[min_idx], lista[i]
        return lista

    @staticmethod
    def ordenamiento_rapido(lista):
        if len(lista) <= 1:
            return lista
        pivot = lista[len(lista) // 2]
        left = [x for x in lista if x < pivot]
        middle = [x for x in lista if x == pivot]
        right = [x for x in lista if x > pivot]
        return EstructurasDeDatos.ordenamiento_rapido(left) + middle + EstructurasDeDatos.ordenamiento_rapido(right)

def main():
    print("### Listas ###")
    EstructurasDeDatos.listas()
    print("\n### Colas ###")
    EstructurasDeDatos.colas()
    print("\n### Pilas ###")
    EstructurasDeDatos.pilas()
    print("\n### Conjuntos ###")
    EstructurasDeDatos.conjuntos()
    print("\n### Diccionarios ###")
    EstructurasDeDatos.diccionarios()
    print("\n### Cadenas ###")
    EstructurasDeDatos.cadenas()

    lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("\n### Búsqueda Secuencial ###")
    print("Índice del 9 en la lista:", EstructurasDeDatos.busqueda_secuencial(lista, 9))

    lista_ordenada = sorted(lista)
    print("\n### Búsqueda Binaria ###")
    print("Índice del 9 en la lista ordenada:", EstructurasDeDatos.busqueda_binaria(lista_ordenada, 9))

    print("\n### Ordenamiento Burbuja ###")
    print("Lista ordenada con Burbuja:", EstructurasDeDatos.ordenamiento_burbuja(lista[:]))

    print("\n### Ordenamiento por Inserción ###")
    print("Lista ordenada con Inserción:", EstructurasDeDatos.ordenamiento_insercion(lista[:]))

    print("\n### Ordenamiento por Selección ###")
    print("Lista ordenada con Selección:", EstructurasDeDatos.ordenamiento_seleccion(lista[:]))

    print("\n### Ordenamiento Rápido ###")
    print("Lista ordenada con Quick Sort:", EstructurasDeDatos.ordenamiento_rapido(lista[:]))

if __name__ == "__main__":
    main()
