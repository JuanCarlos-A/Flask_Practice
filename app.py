# Importamos del modulo de FLASK
from flask import Flask
# Traemos las librerias necesarias
from flask import render_template, redirect, url_for, request
# Creamos la instancia de Flask dentro de una variable. El primer argumento es el nombre del módulo o paquete de la aplicación
app =Flask(__name__)

# Endpoints o Routing
@app.route("/")
def hello_world():
    return "<p>Hello, World</p>"

@app.route("/hello")
def hello():
    return "Hello"

# En esta URL se ingresara un nombre, no se necesita parsear porque por el valor por defecto es un string
@app.route("/saludar/<nombre>")
def saludar(nombre):
    # Puedo usar metodos de python para alterar los resultados
    return f'Hola {nombre.upper()}, este mensaje es de la URL'

# En esta URL se ingresara un numero, por esto debe ser parseada
@app.route("/llamar/<int:cel>")
def llamar(cel):
    return f'<h3>Se esta llamando al celular {cel+1}<h3>'

# Haremos uso de un template que se redireccionara al html
@app.route("/mostrar/<nombre>")
def mostrar_nombre(nombre):
    return render_template("mostrar.html", name = nombre)

@app.route("/redirect")
def mi_redirect():
    # Con este redirect podemos redireccionar a la función que queramos, en este caso la funcion de hello_world o pagina principal
    # Haciendo uso del url_for
    return redirect(url_for('hello_world'))

# Vamos a manejar los errorres, (en este caso el 404) con ayuda de las funciones que tiene Flask
@app.errorhandler(404)
# Este argumento va a ser el error que reciba la funcion
def pagina_error(error):
    # Renderizamos a la pagina del error y enviamos el tipo de error y el mensaje de error
    return (render_template('404.html', error = error), 404)

# Esta seccion va a ser una tarea 
# Cuando se ingrese esta URL con los argumentos necesarios se ejecutara la funcion
@app.route('/ingreso/<user>/<password>')
# Recibimos los argumentos
def ingreso(user, password):
    # Realizamos una condicional que rediregira a una pagina con un mensaje de exito solo en caso de true
    if (user == 'Juan' and password == 'hola1234'):
        return render_template('login.html', mensaje = 'Acertado')
    else:
        return render_template('login.html', mensaje = 'Incorrecto')

# Esta seccion va a ser otra seccion
# Aqui se recibe los numeros en una url(en una se transforma a int y en otra se recibe un string)
@app.route('/suma/<int:num1>/<num2>')
def sumar(num1, num2):
    # Aqui paresamos el numero que se recibio como un string
    result=num1+int(num2)
    return render_template('result.html', num1=num1, num2=num2, result=result)

@app.route('/resta/<int:num1>/<num2>')
def restar(num1,num2):
    # Parseamos el numero resivido como string
    result = num1 - int(num2)
    # Funciona de ambas formas
    # return '<h1> La resta de {} y {} es {}</h1>'.format(num1,num2,result)
    return f'<h1> La resta de {num1} y {num2} es {result}</h1>'

@app.route('/login')
def log():
    return render_template('log.html')


@app.route('/index')
def index():
    name = 'Imagen'
    tamano = 200
    # De esta forma vamos a poder enviar variables a nuestras paginas al momento de ser renderizadas
    return render_template('index.html', name=name, tamano=tamano)

@app.route('/diccionario')
def diccionario():
    dic = {
        'nombre':'Juan',
        'edad':'22',
        'pais':'Mexico'
        }
    # Aunque ya hallamos usado este template antes, no lo vamos a necesitar mas
    return render_template('index.html', dic = dic)

# Vamos a trabajar con Bucles
@app.route('/listasPersonas')
def listaPersona():
    personas=['Martin','Pedro','Karla']
    return render_template('bucle.html', personas=personas)


# Aqui utilizaremos una ruta para dirigirnos a la condicional
@app.route("/condicion/<contrasena>")
def condition(contrasena):
    return render_template('condicional.html', password = contrasena)

# Aqui vamos a utilizar la herencia de templates usando Jinja 2
@app.route("/perfil")
def perfil():
    return render_template('perfil.html')

@app.route("/blog")
def blog():
    return render_template('blog.html')

# Ahora vamos a usar los formularios
@app.route("/form")
def form():
    return render_template('formulario.html')

@app.route("/bienvenido")
def bienvenido():
    # Aqui vamos a recibir los argumentos con ayuda de la libreria importada request
    # Al enviar un diccionario nosotros podemos usar un get y obtenerlo por la llave
    # Usamos el request para traer como argumentos los datos del formulario

    ans = request.args.get('ans')
    name = request.args.get('user')
    password = request.args.get('pass')

    if ans != "false":
        name_validator='Juan'
        pass_validator='123'
        # Validamos los datos con un condicional
        if name == name_validator and password == pass_validator:
            # En caso correcto entonces se guiara a una pagina de bienvenida
            return render_template('bienvenido.html', name, password)
        else:
            # Sino mostrara un mensaje
            return '<h1>Ingreso de usuario o de contraseña invalido</h1>'
    elif ans == "false":
        return f'<h1>El usuario {name} fue registrado correctamente</h1>'


    

    


# Verifica que si el archivo es el pricipal, se corra la aplicacion con el depurador activo
if __name__ == '__main__':
    # Con esta linea de codigo tenemos el modo depurador encendido al momento de correr el archivo
    app.run(debug=True)