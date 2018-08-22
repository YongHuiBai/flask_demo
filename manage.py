from flask_script import Manager, Server
from flask_migrate import MigrateCommand
from my_flask import create_app

app = create_app()
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(ssl_context='adhoc'))

if __name__ == '__main__':
    manager.run()
