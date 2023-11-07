#Esta clase es un reflejo de la tabla user de la base de datos
#Funcionará para manejar las entidades de tipo usuario
#Funcionará para realizar la autentificación
class User():
    def __init__(self, id, username, password, fullname=""):
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    #método para comprobar si la contraseña ingresada es la misma que la que está en la base de datos
    @classmethod 
    def check_password(self, databasePassword, inputtedPassword):
        #print(self.password) <-- Intentar utilizar los atributos (self) de la clase User en el momento en que se comprueba la contraseña nos da un error, esto debido a que se intenta acceder a un atributo de una instancia que no se a creado.
        if databasePassword == inputtedPassword: # <-- Aquí se comprueba la contraseña que está en la base de datos con la contraseña ingresada
            return True
        else:
            return False

