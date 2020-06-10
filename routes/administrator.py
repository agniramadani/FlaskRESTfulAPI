"""
Defines the blueprint for the api
"""
from flask import Blueprint
from flask_restful import Api
from resources import AdministratorResource

Administrator_BLUEPRINT = Blueprint('administrator', __name__)
Api(Administrator_BLUEPRINT).add_resource(AdministratorResource, '/administrator',
                                          '/administrator/<int:administrator_id>')

