from animal import Animal,Perro,Gato,Vaca,AnimalManager
from collections import deque, OrderedDict
# if __name__ == '__main__':
#     # Ejemplo de uso de la clase Perro y Animal
#     perro1 = Perro(nombre="Max", tamaño="Grande", edad=5, color="Negro", raza="Pastor Alemán")
#     perro2 = Perro(nombre="Buddy", tamaño="Pequeño", edad=3, color="Blanco", raza="Chihuahua")

#     perro1.set_nombre("Alex")
#     print(perro1.get_nombre())

#     print(perro1)

#     print(perro1 == perro2)  # Comprobar igualdad entre perro1 y perro2
#     print(perro1 < perro2)   # Comprobar si perro1 es menor que perro2 según la edad
#     print(perro1 > perro2)   # Comprobar si perro1 es mayor que perro2 según la edad

#     # Crear una lista de perros y convertirla en una tupla
#     lista_perros = []
#     lista_perros.append(perro1)
#     lista_perros.append(perro2)
#     tupla_perros = tuple(lista_perros)
#     print(tupla_perros)



if __name__ == '__main__':
    # Ejemplo de uso de listas para almacenar animales
    lista_animales = [
        AnimalManager.crear_animal("Max", "perro"),
        AnimalManager.crear_animal("Whiskers", "gato"),
        AnimalManager.crear_animal("Betsy", "vaca")
    ]

    # Iterar sobre la lista de animales y llamar a métodos específicos
    print("Lista de animales:")
    for animal in lista_animales:
        print(f"{animal.__class__.__name__} {animal._nombre} hace {animal.hacer_sonido()}")
    
    # Ejemplo de uso de una cola (deque) para almacenar animales
    cola_animales = deque()
    cola_animales.append(AnimalManager.crear_animal("Bruno", "perro"))
    cola_animales.append(AnimalManager.crear_animal("Whiskers", "gato"))
    cola_animales.append(AnimalManager.crear_animal("Daisy", "vaca"))

    # Procesar la cola de animales (eliminar el primero en entrar)
    print("\nCola de animales:")
    while cola_animales:
        animal = cola_animales.popleft()
        print(f"{animal.__class__.__name__} {animal._nombre} hace {animal.hacer_sonido()}")

    # Ejemplo de uso de una pila (stack) para almacenar animales
    pila_animales = []
    pila_animales.append(AnimalManager.crear_animal("Rex", "perro"))
    pila_animales.append(AnimalManager.crear_animal("Felix", "gato"))
    pila_animales.append(AnimalManager.crear_animal("Molly", "vaca"))

    # Procesar la pila de animales (eliminar el último en entrar)
    print("\nPila de animales:")
    while pila_animales:
        animal = pila_animales.pop()
        print(f"{animal.__class__.__name__} {animal._nombre} hace {animal.hacer_sonido()}")

    # Ejemplo de uso de un diccionario (hashmap) para almacenar animales
    diccionario_animales = {}
    diccionario_animales["Max"] = AnimalManager.crear_animal("Max", "perro")
    diccionario_animales["Whiskers"] = AnimalManager.crear_animal("Whiskers", "gato")
    diccionario_animales["Betsy"] = AnimalManager.crear_animal("Betsy", "vaca")

    # Acceder a un animal específico en el diccionario y llamar a métodos
    print("\nDiccionario de animales:")
    for nombre, animal in diccionario_animales.items():
        print(f"{animal.__class__.__name__} {nombre} hace {animal.hacer_sonido()}")

    # Ejemplo de uso de un set para almacenar nombres únicos de animales
    set_nombres_animales = set()
    set_nombres_animales.add("Max")
    set_nombres_animales.add("Whiskers")
    set_nombres_animales.add("Betsy")

    print("\nSet de nombres de animales:")
    for nombre in set_nombres_animales:
        print(nombre)

    # Ejemplo de simulación de TreeMap usando OrderedDict para almacenar animales ordenados por nombre
    tree_map_animales = OrderedDict()
    tree_map_animales["Betsy"] = AnimalManager.crear_animal("Betsy", "vaca")
    tree_map_animales["Max"] = AnimalManager.crear_animal("Max", "perro")
    tree_map_animales["Whiskers"] = AnimalManager.crear_animal("Whiskers", "gato")

    print("\nTreeMap simulado de animales (ordenado por nombre):")
    for nombre, animal in tree_map_animales.items():
        print(f"{animal.__class__.__name__} {nombre} hace {animal.hacer_sonido()}")



    # Ordenar por nombre
    lista_animales_por_edad = sorted(lista_animales, key=comparar_por_edad)