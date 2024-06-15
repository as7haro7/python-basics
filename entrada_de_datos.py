import csv
import json
import mysql.connector
import pandas as pd

class EntradaDatos:
    @staticmethod
    def entrada_teclado():
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        print(f"Nombre: {nombre}, Edad: {edad}")

class Archivos:
    @staticmethod
    def leer_archivo(archivo):
        try:
            with open(archivo, 'r') as f:
                contenido = f.read()
                print(contenido)
        except FileNotFoundError:
            print("El archivo no existe.")
    
    @staticmethod
    def leer_hasta_eof(archivo):
        try:
            with open(archivo, 'r') as f:
                while True:
                    linea = f.readline()
                    if not linea:
                        break
                    print(linea, end='')
        except FileNotFoundError:
            print("El archivo no existe.")

class CRUDCSV:
    @staticmethod
    def crear_csv(archivo, data):
        with open(archivo, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Nombre", "Edad"])
            writer.writerows(data)

    @staticmethod
    def leer_csv(archivo):
        with open(archivo, mode='r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    
    @staticmethod
    def actualizar_csv(archivo, nombre, nueva_edad):
        df = pd.read_csv(archivo)
        df.loc[df['Nombre'] == nombre, 'Edad'] = nueva_edad
        df.to_csv(archivo, index=False)
    
    @staticmethod
    def eliminar_csv(archivo, nombre):
        df = pd.read_csv(archivo)
        df = df[df['Nombre'] != nombre]
        df.to_csv(archivo, index=False)

class CRUDJSON:
    @staticmethod
    def crear_json(archivo, data):
        with open(archivo, 'w') as f:
            json.dump(data, f)
    
    @staticmethod
    def leer_json(archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                print(data)
        except FileNotFoundError:
            print("El archivo no existe.")
    
    @staticmethod
    def actualizar_json(archivo, nombre, nueva_edad):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
            for item in data:
                if item['Nombre'] == nombre:
                    item['Edad'] = nueva_edad
            with open(archivo, 'w') as f:
                json.dump(data, f)
        except FileNotFoundError:
            print("El archivo no existe.")
    
    @staticmethod
    def eliminar_json(archivo, nombre):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
            data = [item for item in data if item['Nombre'] != nombre]
            with open(archivo, 'w') as f:
                json.dump(data, f)
        except FileNotFoundError:
            print("El archivo no existe.")

class CRUDMySQL:
    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="tu_base_de_datos"
        )
    
    @staticmethod
    def crear_tabla():
        conn = CRUDMySQL.conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255),
                edad INT
            )
        """)
        conn.close()

    @staticmethod
    def crear_persona(nombre, edad):
        conn = CRUDMySQL.conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO personas (nombre, edad) VALUES (%s, %s)", (nombre, edad))
        conn.commit()
        conn.close()
    
    @staticmethod
    def leer_personas():
        conn = CRUDMySQL.conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM personas")
        for (id, nombre, edad) in cursor:
            print(f"ID: {id}, Nombre: {nombre}, Edad: {edad}")
        conn.close()
    
    @staticmethod
    def actualizar_persona(nombre, nueva_edad):
        conn = CRUDMySQL.conectar()
        cursor = conn.cursor()
        cursor.execute("UPDATE personas SET edad = %s WHERE nombre = %s", (nueva_edad, nombre))
        conn.commit()
        conn.close()
    
    @staticmethod
    def eliminar_persona(nombre):
        conn = CRUDMySQL.conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM personas WHERE nombre = %s", (nombre,))
        conn.commit()
        conn.close()

def main():
    print("### Entrada de Datos ###")
    EntradaDatos.entrada_teclado()

    print("\n### Archivos ###")
    Archivos.leer_archivo("ejemplo.txt")
    print("\nLeer hasta EOF:")
    Archivos.leer_hasta_eof("ejemplo.txt")

    print("\n### CRUD CSV ###")
    data_csv = [["Juan", 30], ["Ana", 25], ["Pedro", 40]]
    CRUDCSV.crear_csv("personas.csv", data_csv)
    print("Contenido del CSV:")
    CRUDCSV.leer_csv("personas.csv")
    CRUDCSV.actualizar_csv("personas.csv", "Ana", 26)
    print("CSV después de actualizar:")
    CRUDCSV.leer_csv("personas.csv")
    CRUDCSV.eliminar_csv("personas.csv", "Pedro")
    print("CSV después de eliminar:")
    CRUDCSV.leer_csv("personas.csv")

    print("\n### CRUD JSON ###")
    data_json = [{"Nombre": "Juan", "Edad": 30}, {"Nombre": "Ana", "Edad": 25}, {"Nombre": "Pedro", "Edad": 40}]
    CRUDJSON.crear_json("personas.json", data_json)
    print("Contenido del JSON:")
    CRUDJSON.leer_json("personas.json")
    CRUDJSON.actualizar_json("personas.json", "Ana", 26)
    print("JSON después de actualizar:")
    CRUDJSON.leer_json("personas.json")
    CRUDJSON.eliminar_json("personas.json", "Pedro")
    print("JSON después de eliminar:")
    CRUDJSON.leer_json("personas.json")

    print("\n### CRUD MySQL ###")
    CRUDMySQL.crear_tabla()
    CRUDMySQL.crear_persona("Juan", 30)
    CRUDMySQL.crear_persona("Ana", 25)
    CRUDMySQL.crear_persona("Pedro", 40)
    print("Contenido de la tabla personas:")
    CRUDMySQL.leer_personas()
    CRUDMySQL.actualizar_persona("Ana", 26)
    print("Tabla después de actualizar:")
    CRUDMySQL.leer_personas()
    CRUDMySQL.eliminar_persona("Pedro")
    print("Tabla después de eliminar:")
    CRUDMySQL.leer_personas()

if __name__ == "__main__":
    main()
