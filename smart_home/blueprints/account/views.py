from flask import Blueprint, render_template


account = Blueprint('account',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    url_prefix='/account')


@account.route('/login')
def login():
    return render_template('account/login.html')
