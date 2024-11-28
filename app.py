from flask import Flask, render_template

""" Seleccionar el Intérprete de Python:
Presiona Ctrl+Shift+P y escribe "Python: Select Interpreter", luego selecciona el entorno virtual (env) que acabas de crear. """

app = Flask(__name__)

# primer endpoint
@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
