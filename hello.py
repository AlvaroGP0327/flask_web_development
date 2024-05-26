from flask import Flask,request, make_response, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lalita'

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

@app.route('/formulario',methods=['GET','POST'])
def formulario():
    #Formulario de ingreso nombre y boton submit.
    name= None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data= ''
    return render_template('form.html',form=form,name=name)


#WebForms
class NameForm(FlaskForm):
    name = StringField('Cual es tu nombre:',validators=[DataRequired()])
    submit = SubmitField('Ingresar')


