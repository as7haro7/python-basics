# Definición de la superclase Animal
class Animal:
    def __init__(self, nombre=None, edad=None):
        self._nombre = nombre
        self._edad = edad

    def comer(self):
        print(f"{self._nombre} está comiendo")

    def dormir(self):
        print(f"{self._nombre} está durmiendo")

    def hacer_sonido(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre='{self._nombre}', edad={self._edad})"

    @staticmethod
    def comparar_por_edad(animal):
        if animal._edad is None:
            return float('inf')  # Colocar animales sin edad al final de la lista
        return animal._edad


# Definición de la subclase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre=None, tamaño=None, edad=None, color=None, raza=None):
        super().__init__(nombre, edad)  # Llamar al constructor de la superclase Animal
        self._tamaño = tamaño
        self._color = color
        self._raza = raza

    def hacer_sonido(self):
        return "¡Guau!"
    
    def __str__(self):
        return f"Perro(nombre='{self._nombre}', tamaño='{self._tamaño}', edad={self._edad}, color='{self._color}', raza='{self._raza}')"

    def __repr__(self):
        return f"Perro(nombre='{self._nombre}', tamaño='{self._tamaño}', edad={self._edad}, color='{self._color}', raza='{self._raza}')"

    def __eq__(self, other):
        if isinstance(other, Perro):
            return (self._nombre == other._nombre and
                    self._tamaño == other._tamaño and
                    self._edad == other._edad and
                    self._color == other._color and
                    self._raza == other._raza)
        return False

    def __lt__(self, other):
        if isinstance(other, Perro):
            if self._edad is None:
                return False
            if other._edad is None:
                return True
            return self._edad < other._edad
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Perro):
            if self._edad is None:
                return True
            if other._edad is None:
                return False
            return self._edad > other._edad
        return NotImplemented


# Definición de la subclase Gato que hereda de Animal
class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"


# Definición de la subclase Vaca que hereda de Animal
class Vaca(Animal):
    def hacer_sonido(self):
        return "¡Muu!"


class AnimalManager:
    @staticmethod
    def crear_animal(nombre, especie, edad=None):
        if especie.lower() == "perro":
            return Perro(nombre=nombre, edad=edad)
        elif especie.lower() == "gato":
            return Gato(nombre=nombre, edad=edad)
        elif especie.lower() == "vaca":
            return Vaca(nombre=nombre, edad=edad)
        else:
            raise ValueError("Especie no válida")

    @staticmethod
    def buscar_animal_por_nombre(animales, nombre):
        for animal in animales:
            if animal._nombre == nombre:
                return animal
        return None

    @staticmethod
    def ordenar_animales_por_edad(animales):
        return sorted(animales, key=Animal.comparar_por_edad)


if __name__ == '__main__':
    # Ejemplo de uso de AnimalManager para crear animales
    animales = [
        AnimalManager.crear_animal("Max", "perro", 5),
        AnimalManager.crear_animal("Whiskers", "gato", 3),
        AnimalManager.crear_animal("Betsy", "vaca", 7)
    ]

    # Buscar un animal por nombre
    nombre_a_buscar = "Max"
    animal_encontrado = AnimalManager.buscar_animal_por_nombre(animales, nombre_a_buscar)
    if animal_encontrado:
        print(f"Animal encontrado: {animal_encontrado}")
    else:
        print(f"No se encontró un animal con el nombre '{nombre_a_buscar}'")

    # Ordenar animales por edad
    animales_ordenados = AnimalManager.ordenar_animales_por_edad(animales)
    print("Animales ordenados por edad:")
    for animal in animales_ordenados:
        print(animal._edad)

    for animal in animales:
        print(f"{animal.__class__.__name__}: {animal.hacer_sonido()} {animal._edad}")
