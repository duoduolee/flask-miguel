from flask import render_template,flash, redirect,url_for
from app import app
from app.forms import LoginForm




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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


