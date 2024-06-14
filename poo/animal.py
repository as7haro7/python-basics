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


    def comparar_por_edad(animal):
        if animal._edad is None:
            return float('inf')  # Colocar animales sin edad al final de la lista
        return animal._edad





# Definición de la subclase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre=None, tamaño=None, edad=None, color=None, raza=None):
        super().__init__(nombre)  # Llamar al constructor de la superclase Animal
        self._tamaño = tamaño
        self._edad = edad
        self._color = color
        self._raza = raza

    # Métodos getters y setters para los atributos
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_tamaño(self):
        return self._tamaño
    
    def set_tamaño(self, nuevo_tamaño):
        self._tamaño = nuevo_tamaño

    def get_edad(self):
        return self._edad
    
    def set_edad(self, nueva_edad):
        self._edad = nueva_edad

    def get_color(self):
        return self._color
    
    def set_color(self, nuevo_color):
        self._color = nuevo_color

    def get_raza(self):
        return self._raza
    
    def set_raza(self, nueva_raza):
        self._raza = nueva_raza

    def hacer_sonido(self):
        return "¡Guau!"
    
    # Método especial para representar el objeto como una cadena
    def __str__(self):
        return f"Perro(nombre='{self._nombre}', tamaño='{self._tamaño}', edad={self._edad}, color='{self._color}', raza='{self._raza}')"

    # Método especial para representar el objeto cuando se llama a repr()
    def __repr__(self):
        return f"Perro(nombre='{self._nombre}', tamaño='{self._tamaño}', edad={self._edad}, color='{self._color}', raza='{self._raza}')"

    # Métodos especiales de comparación
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
            return self._edad < other._edad
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Perro):
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
    def crear_animal(nombre, especie):
        if especie.lower() == "perro":
            return Perro(nombre)
        elif especie.lower() == "gato":
            return Gato(nombre)
        elif especie.lower() == "vaca":
            return Vaca(nombre)
        else:
            raise ValueError("Especie no válida")

if __name__ == '__main__':
    # Ejemplo de uso de AnimalManager para crear animales
    animales = [
        AnimalManager.crear_animal("Max", "perro"),
        AnimalManager.crear_animal("Whiskers", "gato"),
        AnimalManager.crear_animal("Betsy", "vaca")
    ]

    for k in animales:
        print(k)

    for animal in animales:
        print(f"{animal.__class__.__name__}: {animal.hacer_sonido()}")
