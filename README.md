# Seminario 1 Diseño y Desarrollo de SI

Esto es un proyecto de la asignatura DDSI de la Universidad de Granada (UGR). Se desarrolló con motivación de comenzar a familizarse con el uso de PostgreSQL, Anaconda y Python para la creación y uso de bases de datos en el modelado de un Sistema de Información (SI).

## Replicar el entorno del proyecto (PostgreSQL en Anaconda)

**Paso 1** Crear el entorno virtual de Anaconda. Podemos instalar Anaconda desde la página oficial [aquí](https://www.anaconda.com/products/individual) (recomiendo usar un correo desechable para recibir el software crearlo [aquí](https://temp-mail.org/es/)). Una vez instalado, abrir una terminal y ejecutar los siguientes comandos:
```bash
conda create -n DDSI python=3.9
conda activate DDSI
conda install -c anaconda postgresql
conda install -c anaconda psycopg2 
```

En caso de recibir el siguiente error: `CondaError: Run 'conda init' before 'conda activate'`. 
Deberá ejecutar lo siguiente:
```bash
source activate base
conda activate DDSI
```
Temdreis que añadir si no esta añadido al PATH de nuestro sistema las siguiente rutas (dependiendo de donde tengamos instalado la carpeta de anaconda):
```bash
export PATH ="$HOME/anaconda3/bin:$HOME/anaconda3/condabin:$PATH"

```
**Paso 2** Inicializar PostgreSQL y crear una base de datos. Abrimos una terminal y ejecutamos (debemos tener el entorno DDSI activado):
```bash
mkdir <nombre_directorio_trabajo>
cd <nombre_directorio_trabajo>
initdb ./pgdata
pg_ctl -D ./pgdata -l logfile start
```

El comando `pg_ctl -D ./pgdata -l logfile start` indica a la herramienta `pg_ctl` el directorio donde se guardarán los archivos de configuración de PostgreSQL, el nombr de ./pgdata no es un requisito, inidicamos tambien donde se deben guardar los logs del servidor, archivo logfile e indicamos que queremos iniciar el servicio con `start`. Para detener abrimos una terminal y ejecutamos: 
```bash
pg_ctl -D ./pgdata stop 
```

Ahora creamos un usuario en PostgreSQL y le asignamos permisos de superusuario. Abrimos una terminal y ejecutamos:
```bash
psql -l 
psql -d postgres
```

Dentro de PostgreSQL ejecutamos (el nombre de usuario y la contraseña deben corresponder con las que aparecen en el .env):
```bash
CREATE USER ddsi WITH PASSWORD 'seminario,DDSI'; # Crea el usuario
ALTER USER ddsi WITH SUPERUSER; # Darle permisos de super usuario al usuario
\q # salir
```

## Ejecutar proyecto

Para ejecutar el proyecto podemos simplemente clonar el repositorio y tener instalado en nuestro sistema todas las herramientas. En caso de haber replicado el entorno deberemos, clonar el repositorio para tener todos los archivos e inicializar el estado de la base de datos mediante los scripts .sql, que se encuentran en la carpeta `seminario1/sql`. 
```bash
psql -d postgres # Entrar en postgres para ejecutar comandos
\c postgres # Conectarse a la base de datos postgres
CREATE DATABASE paqueteria; # Crear base de datos paqueteria (B2-SEUR si quereis) 
\c paqueteria # Conectarse a la base de datos stock
\i ~/ddsi_seminario/seminario1/sql/crear_stock.sql # Ejecutar script de SQL para crear tabla (en caso de haber clonado el repositorio en el home)
```

No te olvides de modificar el fichero `.env` con los datos de tu usuario y contraseña de PostgreSQL, puedes usar los mismos que vienen por defecto.
Además serán útiles los sigueintes comandos para moverse por el entorno de PostgreSQL se pueden encontrar todos buscando en Google.
```bash
\c nombre_bd # Te conecta a la base de datos con nombre nombre_bd
\dt # Una vez conectado a una base de datos te lista las tablas 
SELECT * FROM nombre_tabla; # Te muestra todas las filas de una tabla (util para ver si las inserciones han sido correctas)
\h # Te muestra todas las ordenes que se pueden mandar a la base de datos
```

El archivo .env es ignorado por git según nuestro .gitignore y se debe por tanto crear para el correcto funcionamiento, abrir terminal dentro de la carpeta del proyecto y ejecutar:
```bash
touch .env
echo "DB_USER=tu_usuario
DB_PASSWD=tu_contraseña
DB_SUPERUSER=tu_superusuario
DB_HOST=localhost
DB_NAME=paqueteria" > .env 
cat .env
```

La última instrucción deberia mostrar lo siguiente:
```bash
DB_USER=tu_usuario
DB_PASSWD=_tu_contraseña
DB_SUPERUSER=tu_superusuario
DB_HOST=localhost
DB_NAME=paqueteria
```

Y todo debería funcionar correctamente
