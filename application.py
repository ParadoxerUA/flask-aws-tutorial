from flask import Flask
from application import db
from application.views import bp
# from application.models import Data


def create_app(config):
    application = Flask(__name__)
    application.config.from_object(ProductionConfig)
    db.init_app(application)
    application.register_blueprint(bp)
    application.app_context().push()
    application.debug=True
    db.create_all()
    return application


if __name__ == '__main__':
    from config import ProductionConfig

    application = create_app(ProductionConfig)
    application.run(host='0.0.0.0', port=8000)
