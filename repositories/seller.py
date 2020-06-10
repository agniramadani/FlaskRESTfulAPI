from model.Model import *


class SellerRepository:
    """ The repository for the seller model """
    @staticmethod
    def create_seller(name, phone_number):
        seller = Seller(name=name, phone_number=phone_number)
        db.session.add(seller)
        db.session.commit()

    @staticmethod
    def get_seller(seller_id):
        return Seller.get_delete_put_post(seller_id)

    @staticmethod
    def update_seller(seller_id, name, phone_number):
        seller = Seller.query.get(seller_id)
        seller.name = name
        seller.phone_number = phone_number
        db.session.commit()

    @staticmethod
    def delete_seller(seller_id):
        cars_of_this_seller = Car.query.filter_by(seller_id=seller_id).all()
        for car in cars_of_this_seller:
            db.session.delete(car)
            db.session.commit()
        return Seller.get_delete_put_post(seller_id)
