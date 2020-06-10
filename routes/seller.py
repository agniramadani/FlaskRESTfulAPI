"""
Defines the blueprint for the api
"""
from flask import Blueprint
from flask_restful import Api
from resources import SellerResource

SELLER_BLUEPRINT = Blueprint('seller', __name__)
Api(SELLER_BLUEPRINT).add_resource(SellerResource, '/seller', '/seller/<int:seller_id>')
