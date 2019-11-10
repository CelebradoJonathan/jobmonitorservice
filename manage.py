import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from src.app import create_app, db
from src.models import JobModel, JobIdModel


env_name = "development"

app = create_app(env_name)

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()