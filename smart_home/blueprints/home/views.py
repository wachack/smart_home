from flask import Blueprint, render_template


home = Blueprint('home',
                 __name__,
                 template_folder='templates',
                 static_folder='static',
                 url_prefix='/home')


@home.route('/')
def login():
    return render_template('home/home.html')
