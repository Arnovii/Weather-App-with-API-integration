from flask import Flask
from flask_mysqldb import MySQL
from config import configuration
#from view.views import *    <-- with this we can use the functions without the prefix views.
#from view import views      <-- with this we can use the functions with the prefix
import view.views as views  #<-- with this we can use the functions with the prefix

app = Flask(__name__, template_folder="templates")
dataBaseConnection = MySQL(app) # <--- With this, we can use the MySQL connection in the app. To use CRUD operations, we need to use the cursor object.

app.config['MYSQL_HOST'] = configuration['development'].MYSQL_HOST
app.config['MYSQL_USER'] = configuration['development'].MYSQL_USER
app.config['MYSQL_PASSWORD'] = configuration['development'].MYSQL_PASSWORD
app.config['MYSQL_DB'] = configuration['development'].MYSQL_DB
app.config['MYSQL_PORT'] = configuration['development'].MYSQL_PORT

if __name__ == "__main__":
    app.config.from_object(configuration['development']) # <--- We can use the configuration object in the app.

    ''' ---------- ROUTES ---------- '''
    app.add_url_rule('/', view_func=views.index)
    app.add_url_rule('/login', view_func=views.login, methods=['GET', 'POST'])
    app.add_url_rule('/home', view_func=views.home)

    ''' ----------------------------- '''

    app.run()