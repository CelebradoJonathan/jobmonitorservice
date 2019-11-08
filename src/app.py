from flask import Flask

from .config import app_config
from .models import db
from .views.JobView import job_api as job_blueprint
from .views.JobIdView import jobid_api as jobid_blueprint


def create_app(env_name):
    """

    Create app

    """

    # app initiliazation

    app = Flask(__name__)

    app.config.from_object(app_config[env_name])

    db.init_app(app)
    app.register_blueprint(job_blueprint, url_prefix='/modulelog')
    app.register_blueprint(jobid_blueprint, url_prefix='/modulelogid')
    @app.route('/', methods=['GET'])
    def index():
        """

        example endpoint

        """

        return 'Congratulations! Your first endpoint is workin'

    return app