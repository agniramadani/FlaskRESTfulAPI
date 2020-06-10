"""
Define the REST verbs relative to the api
"""
from flask import request
from flask_restful import Resource
from repositories.car import CarRepository
from model.Model import *


class CarResource(Resource):
    @staticmethod
    def get(car_id=None):
        if car_id is not None:
            return CarRepository.get_car(car_id)
        return CarRepository.get_car(None)

    @staticmethod
    def post():
        seller = Seller.query.get(request.json['seller_id'])
        if seller:
            CarRepository.create_car(request.json['seller_id'], request.json['make'],
                                     request.json['model'], request.json['first_registration'],
                                     request.json['price'], request.json['fuel'])
            return 'Car is successfully created!'
        return 'This seller does not exist!'

    @staticmethod
    def put(car_id):
        CarRepository.update_car(car_id, request.json['make'],
                                 request.json['model'], request.json['first_registration'],
                                 request.json['price'], request.json['fuel'])
        return 'Car is successfully updated!'

    @staticmethod
    def delete(car_id):
        CarRepository.delete_car(car_id)
        return 'Car is successfully deleted!'
