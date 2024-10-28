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

**Paso 2** Inicializar PostgreSQL y crear una base de datos. Abrimos una terminal y ejecutamos (debemos tener el entorno DDSI activado):
```bash
mkdir <nombre_directorio_trabajo>
cd <nombre_directorio_trababajo>
initdb ./pgdata
pg_ctl -D ./pgdata -l logfile start
```

El comando `pg_ctl -D ./pgdata -l logfile start` indica a la herramienta `pg_ctl` el directorio donde se guardarán los archivos de configuración de PostgreSQL, el nombr de ./pgdata no es un requisito, inidicamos tambien donde se deben guardar los logs del servidor, archivo logfile e indicamos que queremos iniciar el servicio con `start`. Para detener abrimos una terminal y ejecutamos: 
```bash
pg_ctl -D ./pgdata stop # stops PostgreSQL
```

Ahora creamos un usuario en PostgreSQL y le asignamos permisos de superusuario. Abrimos una terminal y ejecutamos:
```bash
psql -l 
psql -d postgres
```

Dentro de PostgreSQL ejecutamos:
```bash
CREATE USER usuario WITH PASSWORD 'password'; # Create user
ALTER USER usuario WITH SUPERUSER; # Give superuser permission to the user
\q # exit
```

## Ejecutar proyecto

Para ejecutar el proyecto podemos simplemente clonar el repositorio y si no hemos replicado el entorno necesitaremos tener instalado en nuestro sistema todo lo anterior. En caso de tener el entorno deberemos inicializar el estado de la base de datos mediante los scripts .sql, que se encuentran en la carpeta `seminario1/sql`. 
```bash
psql -d postgres # Entrar en postgres para ejecutar comandos
\c postgres # Conectarse a la base de datos postgres
CREATE DATABASE stock; # Crear base de datos stock
\c stock # Conectarse a la base de datos stock
\i ./seminario1/sql/crear_stock.sql # Ejecutar script de SQL para crear tabla
```
No te olvides de modificar el fichero `.env` con los datos de tu usuario y contraseña de PostgreSQL.
