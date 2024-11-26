# dic-repo-flask

1.clonar repositorio
```bash
git clone https://github.com/lsaavsan/dic-repo-flask.git
cd dic-repo-flask
code .
```
2.Activar entorno virtual

```bash
pip install virtualenv
virtualenv .venv
source .venv/Scripts/activate
pip freeze > requirements.txt
pip install -r requirements.txt
```
# 1️⃣ Clonar el repositorio y navegar al directorio
git clone https://github.com/lsaavsan/dic-repo-flask.git
cd dic-repo-flask

# 2️⃣ Abrir el proyecto en Visual Studio Code (opcional)
code .

# 3️⃣ Instalar virtualenv si aún no está instalado
pip install virtualenv

# 4️⃣ Crear y activar el entorno virtual
# En Windows:
virtualenv .venv
source .venv/Scripts/activate
# En Linux/macOS:
# virtualenv .venv
# source .venv/bin/activate

# 5️⃣ Instalar dependencias desde requirements.txt
pip install -r requirements.txt

# 6️⃣ (Opcional) Si agregas nuevas dependencias, actualiza requirements.txt
pip freeze > requirements.txt