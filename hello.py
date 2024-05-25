from flask import Flask,request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    response =  make_response('<h1>Se agrego una cookie a la respuesta</h1>')
    response.set_cookie('cookie','Contenido de la cookie')
    return response

@app.route('/user/<name>')
def user(name):
    response = make_response(f'<p>Hola,{name}</p>')
    response.set_cookie('cookie_id','cookie de usuario')
    return response
