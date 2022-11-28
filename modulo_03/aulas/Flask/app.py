import os
from flask import Flask, render_template
from form import NameForm 

template_dir = os.path.abspath('./templates')

app = Flask(__name__, template_folder=template_dir)

app.config['SECRET_KEY'] = 'AFASFAOJkkljfasf~ç3219-0fm'

@app.route('/', methods = ['GET', 'POST'])
def index():
  name = None
  form = NameForm()
  
  if form.validate_on_submit():
    name = form.name.data
    form.name.data = ''
    
  return render_template('index.html', name = name, form = form)
  
@app.route('/user')
@app.route('/user/<name>')
def user(name=None):
  return render_template('user.html', name=name)