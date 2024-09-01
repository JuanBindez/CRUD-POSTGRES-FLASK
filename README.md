# CRUD-postgreSQL-Flask


### Install requirements:
    pip install -r requiments.txt

## DataBase

#### install postgresql on linux
     sudo apt update
     sudo apt install postgresql postgresql-contrib

#### install flask and psycopg2 connector
     pip install Flask psycopg2-binary

#### access postgre
    sudo -i -u postgres
    psql

### run superuser settings
    CREATE USER myuser WITH PASSWORD 'mypassword';
    ALTER USER myuser WITH SUPERUSER;
    CREATE DATABASE mydatabase;
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
    \q

### to see existing databases
    \l

### database access
    c\ mydatabase

### verify useruser
    sudo -i -u postgres
    psql
    \dn+

### exit of the shell from postgreSQL
    \q
    exit
