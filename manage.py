"""
The file introduces additional options for the flask CLI.

First usage (on Windows, replace export by set command):
> export FLASK_APP=manage.py
> export FLASK_ENV=development
> flask run

Useful commands:
> flask run
> flask db init
> flask db migrate
> flask db upgrade

"""

from smart_home import (create_app, db)
from smart_home.account.models import User
from flask_migrate import Migrate

app = create_app('config.py')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'User': User}
