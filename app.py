from flask import Blueprint
import routes
from model.Model import *


@app.errorhandler(404)
def page_not_found(e):
    return {'message': str(e)}, 404


for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        app.register_blueprint(blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run()
