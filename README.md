# CRUD-POSTGRES-FLASK


### Install requirements:
    pip install -r requiments.txt

# DataBase

#### install postgresql on linux
     sudo apt update
     sudo apt install postgresql postgresql-contrib

#### install flask and psycopg2 connector
     pip install Flask psycopg2-binary

#### acessar o postgre
    sudo -i -u postgres
    psql

### executar as configurações de superuser
    CREATE USER myuser WITH PASSWORD 'mypassword';
    ALTER USER myuser WITH SUPERUSER;
    CREATE DATABASE mydatabase;
    GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
    \q

### para ver os bancos de dados existentes
    \l

### databse access
    c\ mydatabase

### verify useruser
    sudo -i -u postgres
    psql
    \dn+

### exit of the shell from postgreSQL
    \q
    exit
