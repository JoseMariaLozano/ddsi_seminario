# Reparto del trabajo

El proyecto nada más clonarlo y montar el entorno para tener PostgreSQL, python 3.9 y psycopg2. Tenemos que hacer lo siguiente:
Los scripts sql están todos hechos y queda por implementar el main.py. Debemos por tanto hacer el menu y el código que ejecute lo que vamos a hacer. (seguir el ejemplo del profesor que está [aquí](https://github.com/Franblueee/ddsi_examples/blob/main/seminario1/ejemplo.py). 

## Tareas por hacer

**Tarea 1** Función borrado_creación, es la opción 1 del menu (persona_encargada=Jose Maria Lozano Umbria)

**Tarea 2** Función dar_alta_pedido, es la opción 2 del menu (persona_encargada=elegidla vosotros y decidlo por el grupo de Whatsapp para que cambie esto), esta tarea a su vez tiene 4 tareas internas que son las que tendrán que hacer ROLLBACK, COMMIT y estas cosas. Yo si teneis alguna duda decidme y lo miro pero repartiroslo entre vosotros.

**Tarea 3** Funcion mostrar_tablas, es la opción 3 del menu (persona_encargada=elegidla vosotros y decidlo por el grupo de Whatsapp para que cambie esto)

**Tarea 4** Función salir, es la opción 4 del menu (persona_encargada=Jose Maria Lozano Umbria) ya está hecho

**Tarea 5** Una vez la función menu esté completamente implementada dentro del fichero main.py cambiar (lo puede hacer cualquiera) tened en cuenta que si lo cambiais y luego ejecutais python main.py y la función menu no está completamente implementada no funcionará correctamente. Ahora mismo el resultado al ejecutar es `Hola Mundo`.
```python
if __name__ == '__main__'
    menu() (en vez de print("Hola Mundo"))
```
