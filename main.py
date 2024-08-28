from flask import Flask, render_template, redirect, jsonify, request, url_for, flash
import psycopg2
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente
load_dotenv()

def connect_database():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = connect_database()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users;")
            users = cursor.fetchall()
            cursor.close()
            conn.close()
            return render_template("index.html", users=users)
        else:
            return jsonify({"error": "Failed to connect to the database"}), 500

    except Exception as e:
        print(f"Erro ao obter os usuários: {e}")
        return jsonify({"error": "Failed to connect to the database"}), 500
    
@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == "POST":
        conn = connect_database()
        cursor = conn.cursor()
        name = request.form['name']
        idade = request.form['idade']

        cursor.execute('INSERT INTO users (name, age) VALUES (%s, %s)', (name, idade))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add_person.html')

@app.route('/delete_person/<int:id>', methods=['POST'])
def delete_person(id):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))
    

@app.route('/update_person/<int:id>', methods=["GET", "POST"])
def update_person(id):
    conn = connect_database()
    cursor = conn.cursor()
    
    # Obter os dados do usuário para preencher o formulário
    cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
    user = cursor.fetchone()
    
    if request.method == "POST":
        print(request.form)  # Adicione esta linha para imprimir o conteúdo de request.form
        
        name = request.form.get('name')
        idade = request.form.get('idade')

        if not name or not idade:
            return render_template('update_person.html', user=user)
        
        cursor.execute('UPDATE users SET name = %s, age = %s WHERE id = %s', (name, idade, id))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))
    
    cursor.close()
    conn.close()
    return render_template('update_person.html', user=user)


if __name__ == "__main__":
    app.run(debug=True)
