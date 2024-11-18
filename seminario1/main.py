import psycopg2 as pg
from dotenv import load_dotenv
import os

# Guardar las rutas de los scripts en una lista
path_scripts_sql = [
    '/home/jmlu/work/ddsi_seminario/seminario1/sql/crear_stock.sql',
    '/home/jmlu/work/ddsi_seminario/seminario1/sql/crear_pedido.sql',
    '/home/jmlu/work/ddsi_seminario/seminario1/sql/crear_detalle_pedido.sql'
]

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

# Funcionalidades del menú, (eliminar los return cuando se haga la implementacion)
def borrado_creacion(conn, cur, path_scripts_sql) :

    try:
        # Selecionamos cada uno de los scripts
        for sql_script in path_scripts_sql:
            # Leemos cada path y ejecutamos el script
            with open(sql_script) as script: # No hay que cerrar explicitamente ya que with llama a __exit__
                sql_script = script.read()

            cur.execute(sql_script)
            
            conn.commit() # Comiteamos los cambios ya que la creacion de las tablas ha sido correcta
            print("Tablas creadas")

    except Exception as e:
        print(f"Hubo un error creando las tablas {e}")
        conn.execute("ROLLBACK TO s1;") # Volveria al SAVEPOINT s1 creado antes de mostrar el menu
    
    # mostrar_tablas(cur)

    
# Fin de la funcion borrado_creacion


def dar_alta_pedido(cur) :

    try:
        # Savepoint inicial antes de comenzar a insertar el pedido
        cur.execute("SAVEPOINT inicio_pedido;")

        # Obtener un nuevo ID de pedido
        cur.execute("SELECT COALESCE(MAX(cpedido), 0) + 1 FROM pedido")
        nuevo_cpedido = cur.fetchone()[0]
        
        ccliente = int(input("Ingrese el código del cliente: "))
        
        # Insertar el nuevo pedido en la tabla pedido
        cur.execute("INSERT INTO pedido (cpedido, ccliente) VALUES (%s, %s)", (nuevo_cpedido, ccliente))
        
        # Savepoint tras insertar el pedido
        cur.execute("SAVEPOINT despues_de_insertar_pedido;")

        while True:
            print("\nOpciones de gestión del pedido:")
            print("1. Añadir detalle al pedido")
            print("2. Eliminar todos los detalles de un producto")
            print("3. Cancelar pedido")
            print("4. Finalizar gestión del pedido")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                os.system("clear")

                # Añadir detalle al producto
                cproducto = int(input("Ingrese el código del producto: "))
                cantidad = int(input("Ingrese la cantidad deseada: "))

                # Verificar si hay suficiente stock
                cur.execute("SELECT cantidad FROM stock WHERE cproducto = %s", (cproducto,))
                stock_disponible = cur.fetchone()

                if stock_disponible and stock_disponible[0] >= cantidad:
                    try:
                        # Savepoint antes de añadir detalle de producto
                        cur.execute("SAVEPOINT antes_detalle_pedido;")

                        # Insertar en detalle_pedido, pero NO actualizar el stock aún
                        cur.execute("INSERT INTO detalle_pedido (cpedido, cproducto, cantidad) VALUES (%s, %s, %s)", 
                                    (nuevo_cpedido, cproducto, cantidad))
                        print(f"Producto {cproducto} agregado al pedido.")
                        
                    except Exception as e:
                        # Revertimos al savepoint antes de agregar el detalle si hay algún error
                        print(f"Error al agregar el producto al pedido: {e}")
                        cur.execute("ROLLBACK TO antes_detalle_pedido;")
                else:
                    print("Stock insuficiente para el producto.")
                
                # Mostrar tablas después de cada acción
                mostrar_tablas(cur)

            elif opcion == "2":
                try:
                    # Savepoint antes de eliminar los detalles de un producto
                    cur.execute("SAVEPOINT antes_eliminar_detalles;")
                    cproducto = int(input("Ingrese el código del producto a eliminar de todos los pedidos: "))
                    cur.execute("DELETE FROM detalle_pedido WHERE cpedido = %s AND cproducto = %s", (nuevo_cpedido, cproducto))
                    print(f"Se han eliminado los detalles del producto con código {cproducto} en el pedido actual.")

                except Exception as e:
                    # Revertimos al savepoint antes de eliminar si hay algún error
                    print(f"Error al eliminar detalles del producto: {e}")
                    cur.execute("ROLLBACK TO antes_eliminar_detalles;")
                
                # Mostrar tablas después de cada acción
                mostrar_tablas(cur)

            elif opcion == "3":
                os.system("clear")
                # Cancelar el pedido: eliminamos el pedido y sus detalles y volvemos al menú principal
                try:
                    # Savepoint antes de cancelar todo el pedido
                    cur.execute("SAVEPOINT antes_de_cancelar_pedido;")
                    cur.execute("DELETE FROM detalle_pedido WHERE cpedido = %s", (nuevo_cpedido,))
                    cur.execute("DELETE FROM pedido WHERE cpedido = %s", (nuevo_cpedido,))
                    cur.connection.commit()
                    print("Pedido cancelado y revertido exitosamente.")
                    
                except Exception as e:
                    print(f"Error al cancelar el pedido: {e}")
                    cur.execute("ROLLBACK TO antes_de_cancelar_pedido;")
                
                # Mostrar tablas después de cada acción
                mostrar_tablas(cur)
                return  # Salir de la función al menú principal

            elif opcion == "4":
                os.system("clear")
                # Confirmar si el usuario quiere hacer permanentes los cambios
                confirmacion = input("¿Está seguro de hacer permanentes los cambios? (s/n): ").lower()

                if confirmacion == "s":
                    # Aquí actualizamos el stock antes de confirmar el pedido
                    cur.execute("""
                        SELECT cproducto, cantidad FROM detalle_pedido WHERE cpedido = %s
                    """, (nuevo_cpedido,))
                    detalles = cur.fetchall()
                    for detalle in detalles:
                        cproducto, cantidad = detalle
                        cur.execute("UPDATE stock SET cantidad = cantidad - %s WHERE cproducto = %s", (cantidad, cproducto))

                    # Confirmar todos los cambios
                    cur.connection.commit()  
                    print("Pedido registrado y gestión completada con éxito.")
                    break  # Salir del bucle y volver al menú principal

                elif confirmacion == "n":
                    print("Los cambios no se han realizado. Volviendo al estado anterior.")
                    cur.execute("ROLLBACK TO despues_de_insertar_pedido;")  # Revertir cambios a después de insertar el pedido
                else:
                    print("Opción no válida, por favor responda con 'sí' o 'no'.")

            else:
                print("Opción no válida.")

    except Exception as e:
        # Rollback total al savepoint inicial si hay un error no controlado
        print(f"Error al gestionar el pedido: {e}")
        cur.execute("ROLLBACK TO inicio_pedido;")




def mostrar_tablas(cur) :

    try:
        # Obtener todos los nombres de tablas en la base de datos
        cur.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public';
        """)
        tablas = cur.fetchall()

        # Mostrar los datos de cada tabla
        for (tabla,) in tablas:
            print(f"\nContenido de la tabla '{tabla}':")
            cur.execute(f"SELECT * FROM {tabla};")
            registros = cur.fetchall()
            
            # Imprimir los registros de la tabla
            if registros:
                for registro in registros:
                    print(registro)
            else:
                print("La tabla está vacía.")
    except Exception as e:
        print(f"Hubo un error al mostrar las tablas: {e}")
        
    return

def salir(conn, cur) :

    cerrar_conexion(conn, cur)
# Fin de la función salir


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
            os.system("clear")
            borrado_creacion(conn, cur, path_scripts_sql)
        elif opcion == "2":
            os.system("clear")
            dar_alta_pedido(cur)
        elif opcion == "3":
            os.system("clear")
            mostrar_tablas(cur)
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

    salir(conn, cur)  # salir del menu

    # 1.- Borrado y creación de las tablas e inserción de 10 tuplas predefinidas en el código en la tabla Stock. (HECHO)
    # .... implementación en una funcion

    # 2.- Dar de alta nuevo pedido
    # ... implementación en una función

    # 3.- Mostrar contenido de las tablas de la BD
    # ... implementación en una función

    # 4.- Salir del programa y cerrar conexión con la BD (HECHO)
    # ... implementación en una función

    return

if __name__ == '__main__':
    menu() #la funcionalidad esté implementada
