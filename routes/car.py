"""
Defines the blueprint for the api
"""
from flask import Blueprint
from flask_restful import Api
from resources import CarResource

CAR_BLUEPRINT = Blueprint('car', __name__)
Api(CAR_BLUEPRINT).add_resource(CarResource, '/car', '/car/<int:car_id>')
