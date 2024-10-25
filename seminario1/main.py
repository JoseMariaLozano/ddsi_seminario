import psycopg2 as pg
from dotenv import load_dotenv
import os


# Cargar las variables de entorno del archivo .env.
def cargar_configuracion():
    load_dotenv('../.env') 

# Obtener las variables de entorno necesarias para la conexión.
def obtener_variables_entorno():
    return {
        'db_host': os.getenv('DB_HOST'),
        'db_name': os.getenv('DB_NAME'),
        'db_user': os.getenv('DB_USER'),
        'db_passwd': os.getenv('DB_PASSWD')
    }

# Establecer la conexión con la base de datos y crear el cursor.
def conectar_base_datos(db_host, db_name, db_user, db_passwd):
    conn = pg.connect(
        database=db_name,
        user=db_user,
        password=db_passwd,
        host=db_host
    )
    conn.autocommit = False
    cur = conn.cursor()
    return conn, cur

# Cerrar la conexión y el cursor.
def cerrar_conexion(conn, cur):
    cur.close()
    conn.close()

# Funcionalidades del menú

def borrado_creacion() :
    
    return

def dar_alta_pedido() :

    # 1.- Añadir detalle al producto
    #....

    # 2.- Eliminar todos los detalles de un producto
    #....

    # 3.- Cancelar pedido
    #....

    # 4.- Finalizar pedido
    #....

    return

def mostrar_tablas() :

    return

def salir() :

    return

# Fin funcionalidades del menú


# Menú, ejecución del programa (como un main)
def menu() :

    cargar_configuracion()  # Carga la configuración
    variables_db = obtener_variables_entorno()  # Obtiene las variables de entorno
    conn, cur = conectar_base_datos(**variables_db)  # Conecta a la base de datos

    cur.execute("BEGIN;")
    cur.execute("SAVEPOINT s1;")
    
    while True:
        print("\n--- Menú ---")
        print("1. Borrado y creación de tablas")
        print("2. Dar de alta nuevo pedido")
        print("3. Mostrar contenido de las tablas")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            borrado_creacion(cur)
        elif opcion == "2":
            dar_alta_pedido(cur)
        elif opcion == "3":
            mostrar_tablas(cur)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

    cerrar_conexion(conn, cur)  # Cierra la conexión al finalizar

    # 1.- Borrado y creación de las tablas e inserción de 10 tuplas predefinidas en el código en la tabla Stock.
    # .... implementación en una funcion

    # 2.- Dar de alta nuevo pedido
    # ... implementación en una función

    # 3.- Mostrar contenido de las tablas de la BD
    # ... implementación en una función

    # 4.- Salir del programa y cerrar conexión con la BD
    # ... implementación en una función

    return

if __name__ == '__main__':
    print("Hola mundo")
