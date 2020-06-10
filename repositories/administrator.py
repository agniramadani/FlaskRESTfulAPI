from model.Model import *


class AdministratorRepository:
    """ The repository for the administrator model """

    def __init__(self):
        pass

    @staticmethod
    def create_admin(name, super_admin):
        admin = Administrator(name=name, super_admin=super_admin)
        db.session.add(admin)
        db.session.commit()

    @staticmethod
    def get_admin(administrator_id):
        return Administrator.get_delete_put_post(administrator_id)

    @staticmethod
    def update_admin(administrator_id, name, super_admin):
        admin = Administrator.query.get(administrator_id)
        admin.name = name
        admin.super_admin = super_admin
        db.session.commit()

    @staticmethod
    def delete_admin(administrator_id):
        return Administrator.get_delete_put_post(administrator_id)