# Importaciones de las librerias
from flask import Flask, render_template, url_for, redirect, session

# Estas importaciones tendran uqe ver con la creacion de formularios

from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

# Esta importacion se hace con el objetivo de tener una variable de entorno 
# como llave secreta
from config import SECRET_KEY

# Esta sera la instancia de la libreria de flask, el __name__ tiene como objetivo poner el nombre del modulo
app = Flask(__name__)

# Esta configuracion permitira una mayor seguridad haceiendo uso de llaves de seguridad
# Recuerda que una buena practica de programación es guardar la llave en 
# una variable de entorno que luego sera llamada SECRET_KEY

# set SECRET_KEY=tu_llave_secreta_aqui
# import os
# from flask import Flask

# app = Flask(__name__)
# app.secret_key = os.environ.get('SECRET_KEY')

# Esta es otra forma en la cual podemos guardarla directamente en el codigo, aunque no es una buena
# practica
# app.config['SECRET_KEY'] = 'mysecretkey'

app.secret_key = SECRET_KEY

# Aquí se define la clase MyForm que hereda de FlaskForm
class MyForm(FlaskForm):
    # se define un campo de formulario llamado name utilizando el tipo de campo StringField
    # El argumento de 'name' funciona como un identificador
    nombre = StringField('Nombre:') # El validator es para poner una petición minima
    edad = BooleanField('¿Eres mayor de Edad?:') # Segun el tipo de campo existe una función
    comentarios = TextAreaField('Comentarios:')
    # La opcion de choice obliga elegir almens uno para poder enviar informacion
    sexo = RadioField('Sexo:', choices=[('Female', 'Mujer'), ('Male', 'Hombre')])
    boton = SubmitField('Enviar')


# Ruta que lo redireccionara a la pgina de datos personales
@app.route('/informacion')
def info():
    return render_template('info.html')


@app.route('/datosPersonales', methods=['POST', 'GET'])
def datosPersonales():
    # Instancia que nos permitira trabajar formularios
    formulario = MyForm()

    # Validara si el usuario realizo el submit o envio del formualrio
    if formulario.validate_on_submit():
        # Aqui vamos a recibir los datos que haya ingresado y los guardaremos en sesiones
        session['nombre'] = formulario.nombre.data
        session['edad'] = formulario.edad.data
        session['sexo'] = formulario.sexo.data
        session['comentarios'] = formulario.comentarios.data
        session['boton'] = formulario.boton.data

        # Redireccionamos a una funcion que lo llevara a una pagina donde encontrara los datos que ingreso
        return redirect(url_for('info'))
    
    return render_template('datosPersonales.html', formulario=formulario)


# Direcciones o Rutas o Endpoints
@app.route('/', methods=['GET', 'POST'])
def inicio():
    # Variables para el respectivo logeo
    nombre=''
    estado=False

    # Instancia que nos permitira trabajar formularios
    formulario = MyForm()

    # Validara si el usuario realizo el submit o envio del formualrio
    if formulario.validate_on_submit():
        estado = True #Reactualizamos el estado
        nombre = formulario.nombre.data #Traemos el dato del formulario
        formulario.nombre.data = '' #Vaciamos el campo

    return render_template('inicio.html', estado = estado, nombre = nombre, formulario = formulario) 

if __name__ == '__main__':
    app.run(debug=True)