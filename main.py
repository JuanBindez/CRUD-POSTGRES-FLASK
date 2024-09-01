"""

CREATE USER myuser WITH PASSWORD 'mypassword';
ALTER USER myuser WITH SUPERUSER;
CREATE DATABASE mydatabase;
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;

CREATE TABLE users (id SERIAL PRIMARY KEY, nome VARCHAR(100) NOT NULL, idade INT NOT NULL);
"""

from flask import Flask, render_template, redirect, jsonify, request, url_for, flash
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def connect_database():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    return conn

app = Flask(__name__)


@app.route("/")
def index():
    try:
        conn = connect_database()
        if conn:
            cursor = conn.cursor()
            
            search = request.args.get('search')
            
            if search:
                query = "SELECT * FROM users WHERE nome ILIKE %s;"
                cursor.execute(query, ('%' + search + '%',))
            else:
                cursor.execute("SELECT * FROM users;")
            
            users = cursor.fetchall()
            print("Connection to database ok")
            return render_template("index.html", users=users)
        else:
            return jsonify({"Error 01": "Failed to connect to the database"})
        
    except Exception as e:
        return jsonify({"Error 02": f"Failed to connect to the database: {str(e)}"})


@app.route("/add_person", methods=["GET", "POST"])
def add_person():
    if request.method == "POST":
        conn = connect_database()
        cursor = conn.cursor()
        nome = request.form["nome"]
        idade = request.form["idade"]
        cursor.execute('INSERT INTO users (nome, idade) VALUES (%s, %s)', (nome, idade))
        cursor.close()
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    return render_template("add_person.html")

@app.route("/delete_person/<int:id>", methods=["POST"])
def delete_person(id):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (id,))
    cursor.close()
    conn.commit()
    conn.close()

    return redirect(url_for("index"))

@app.route("/update_person/<int:id>", methods=["GET", "POST"])
def update_person(id):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cursor.fetchone()

    if request.method == "POST":
        nome = request.form["nome"]
        idade = request.form["idade"]

        cursor.execute('UPDATE users SET nome = %s, idade = %s WHERE id = %s', (nome, idade, id))
        cursor.close()
        conn.commit()
        conn.close()
        return redirect(url_for("index"))
    
    cursor.close()
    conn.close()
    return render_template("update_person.html", user=user)

if __name__ == "__main__":
    app.run(debug=True)