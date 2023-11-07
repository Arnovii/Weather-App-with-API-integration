from flask import render_template, request, redirect, url_for, flash
#from app import dataBaseConnection #<-- We can use the dataBaseConnection object from app.py.  without prefix
import app as myAplication#<-- We can use the dataBaseConnection object from app.py. with prefix myAplication.dataBaseConnection

#Importamos el paquete ModelUser
from models.ModelUser import ModelUser
#print(ModelUser.mensaje) #<-- Con esto podemos acceder a los atributos de la clase ModelUser

#importamos el modulo entities
from models.entities.User import User

def index():
    return redirect(url_for('login'))

def login():
    if request.method == 'POST':
        print(request.form['usernameLogin'])
        print(request.form['passwordLogin'])

        #Creamos una instancia de la clase User
        defaultId = 0
        user = User(defaultId, username=request.form['usernameLogin'], password=request.form['passwordLogin']) #(id,username,password,fullname) --> fullname es opcional, parámetro por defecto en ""
        loggedUser = ModelUser.login(myAplication.dataBaseConnection, user)

        if loggedUser != None: #Si el usuario existe en la base de datos (se supone que en ModelUser ya ha ocurrido la autentificación [tanto el username como el password son correctos]) #falta incorporar la validacion del password.
            
            if loggedUser.password == True:
                print("El usuario existe en la base de datos")
                #En este punto, el usuario es completamente válido. Se puede crear una sesión para el usuario
                return redirect(url_for('home'))
            else:
                flash("Contraseña incorrecta")
                return redirect(url_for('login'))

        else:
            flash("El usuario no existe")
            return redirect(url_for('login'))

        return "<h1>POST</h1>"
    else: # GET
        return render_template('auth/login.html')
    

def home():
    return render_template('home.html')