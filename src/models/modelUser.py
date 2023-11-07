from models.entities.User import User
    
'''
Con ModelUser vamos a realizar la autentificación de los usuarios

dabataseConnection --> Instancia de la clase DatabaseConnection
user --> Instancia de la clase User que contendra la informacion del usuario ingresada por el formulario de LOGIN

'''        

class ModelUser(): 

    mensaje = "Hola desde el modelo"

    @classmethod    
    def login(self, dabataseConnection, user):
        try:
            cursor = dabataseConnection.connection.cursor() #Cursor que nos permite interactuar con la base de datos
            sqlSentence = f""" SELECT userId, userName, userPassword, userFullName FROM users WHERE username = '{user.username}' """ #Consulta SQL en donde retorno los registros que coincidan con el username ingresado
            cursor.execute(sqlSentence) 
            row = cursor.fetchone()     #Me retorna una tupla con los datos de la consulta. Es una única tupla porque el username es único en la base de datos
            print(f"Registro obtenido de la base de datos: {row}")
            if row != None:            #Si el username existe en la base de datos... 
                userInstace = User(row[0], row[1], User.check_password(row[2], user.password), row[3]) #Atento a como es que se llama el método check_password (el prefijo User. es porque el método es de la clase User)
                return userInstace
            else:
                return None
        
        except Exception as ex: 
            raise Exception(ex)