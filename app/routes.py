from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    theuser = {'username': 'Duoduo'}
    postnames = [
        {
            'author': {'username': 'duoduo'},
            'body': 'the principle of the world and nature'
        },
        {
            'author': {'username': 'JK.rolin'},
            'body': 'The harry port and magic stone'
        },
        {
            'author': {'username': 'Jane.Osting'},
            'body': 'Pride and Prejudice'
        }
    ]

    return render_template('index.html', title='flask miguel',user=theuser,posts=postnames)





