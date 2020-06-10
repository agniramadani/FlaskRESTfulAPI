"""
Define the REST verbs relative to the api
"""
from flask import request
from flask_restful import Resource
from repositories.administrator import AdministratorRepository


class AdministratorResource(Resource):
    @staticmethod
    def get(administrator_id=None):
        if administrator_id is not None:
            return AdministratorRepository.get_admin(administrator_id)
        return AdministratorRepository.get_admin(None)

    @staticmethod
    def post():
        AdministratorRepository.create_admin(request.json['name'], request.json['super_admin'])
        return 'Administrator is successfully created!'

    @staticmethod
    def put(administrator_id):
        AdministratorRepository.update_admin(administrator_id, request.json['name'], request.json['super_admin'])
        return 'Administrator is successfully updated!'

    @staticmethod
    def delete(administrator_id):
        AdministratorRepository.delete_admin(administrator_id)
        return 'Administrator is successfully deleted!'

