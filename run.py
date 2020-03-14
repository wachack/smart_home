"""
The file that is invoked to start up a development server.
"""

from smart_home import app


if __name__ == '__main__':
    app.run(host="127.0.0.1")
