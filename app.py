from flask import Flask, render_template

""" Seleccionar el Intérprete de Python:
Presiona Ctrl+Shift+P y escribe "Python: Select Interpreter", luego selecciona el entorno virtual (env) que acabas de crear. """

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
