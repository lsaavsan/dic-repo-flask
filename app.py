from flask import Flask, render_template, request, redirect, url_for,abort
import sqlite3

""" Seleccionar el Intérprete de Python:
Presiona Ctrl+Shift+P y escribe "Python: Select Interpreter", luego selecciona el entorno virtual (env) que acabas de crear. """


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return render_template('index.html')

@app.route("/base", methods=["GET"])
def base():
    return render_template('base.html')

# Petición-get
@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')

@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')

# Obtener todos los post
@app.route("/post", methods=["GET"])
def get_all_posts():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('post/posts.html', posts=posts)


# solo para uno
@app.route("/post/<int:post_id>", methods=["GET"])
def get_one_post(post_id: int):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return render_template('post/post.html', post=post)


@app.route("/post/create", methods=["GET", "POST"])
def create_one_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
        conn.commit()
        conn.close()
        return redirect(url_for('get_all_posts'))
    elif request.method == "GET":
        return render_template('post/create.html')


@app.route("/post/edit/<int:post_id>", methods=["GET", "POST"])
def edit_one_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
 
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        conn = get_db_connection()
        conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
        conn.commit()
        conn.close()
        return redirect(url_for('get_all_posts'))
    if request.method == "GET":
        return render_template('post/edit.html', post=post)

@app.route("/post/delete/<int:post_id>", methods=["POST"])
def delete_one_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
   
    if post is None:
        abort(404)
 
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('get_all_posts'))





# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)