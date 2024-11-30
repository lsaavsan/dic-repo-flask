from flask import Flask, render_template
import sqlite3
""" Seleccionar el Intérprete de Python:
Presiona Ctrl+Shift+P y escribe "Python: Select Interpreter", luego selecciona el entorno virtual (env) que acabas de crear. """


def get_db_connection():
    conn=sqlite3.connect("database.db")

    #Genera un diccionario cuya clave son los nombre de la columna
    conn.row_factory=sqlite3.Row
    return conn

app = Flask(__name__)

# primer endpoint
@app.route("/", methods=["GET"])
def root():
    return render_template('index.html')

# segundo endpoint
@app.route("/home", methods=["GET"])
def home():
    return render_template('home.html')

# tercer endpoint
@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html')

# cuarto endpoint
@app.route("/base", methods=["GET"])
def base():
    return render_template('base.html')

@app.route("/posts",methods=["GET"])
def get_all_posts():
    conn=get_db_connection()  
    # modelo
    posts=conn.execute('SELECT * FROM posts').fetchall()
    #print(posts)
    #print(conn)
    conn.close()
    #view
    return render_template("post/posts.html",posts=posts)




@app.route("/post/<int:post_id>",methods=["GET"])
def get_one_posts(post_id:int):
    conn=get_db_connection()    
    # modelo
    post=conn.execute('SELECT * FROM posts WHERE id = ?',(post_id,)).fetchone() 
    #print(posts)
    #print(conn)
    conn.close()
    #view
    return render_template("post/post.html",post=post)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
