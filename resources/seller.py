"""
Define the REST verbs relative to the api
"""
from flask import request
from flask_restful import Resource
from repositories.seller import SellerRepository


class SellerResource(Resource):
    @staticmethod
    def get(seller_id=None):
        if seller_id is not None:
            return SellerRepository.get_seller(seller_id)
        return SellerRepository.get_seller(None)

    @staticmethod
    def post():
        SellerRepository.create_seller(request.json['name'], request.json['phone_number'])
        return 'Seller is successfully created!'

    @staticmethod
    def put(seller_id):
        SellerRepository.update_seller(seller_id, request.json['name'], request.json['phone_number'])
        return 'Seller is successfully updated!'

    @staticmethod
    def delete(seller_id):
        SellerRepository.delete_seller(seller_id)
        return 'Seller is successfully deleted!'
