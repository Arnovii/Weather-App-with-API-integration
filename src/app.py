from flask import Flask
from config import configuration
from view import views
app = Flask(__name__, template_folder="templates")

if __name__ == "__main__":
    app.config.from_object(configuration['development']) # <--- Para utilizar la configuración de desarrollo en config.py

    ''' ---------- ROUTES ---------- '''
    app.add_url_rule('/', view_func=views.login)


    app.run()