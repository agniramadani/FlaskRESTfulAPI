from model.Model import *


class CarRepository:
    @staticmethod
    def create_car(seller_id, make, model, first_registration, price, fuel):
        car = Car(seller_id=seller_id, make=make, model=model,
                  first_registration=first_registration,
                  price=price, fuel=fuel)
        db.session.add(car)
        db.session.commit()

    @staticmethod
    def get_car(car_id):
        return Car.get_delete_put_post(car_id)

    @staticmethod
    def update_car(car_id, make, model, first_registration, price, fuel):
        car = Car.query.get(car_id)
        car.make = make
        car.model = model
        car.first_registration = first_registration
        car.price = price
        car.fuel = fuel
        db.session.commit()

    @staticmethod
    def delete_car(car_id):
        return Car.get_delete_put_post(car_id)
