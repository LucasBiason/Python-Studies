from flask_restful import Resource, reqparse
from models import HotelModel


class Hoteis(Resource):
    param_args = reqparse.RequestParser()
    param_args.add_argument('nome')

    def get(self):
        dados = Hoteis.param_args.parse_args()
        queryset = HotelModel.get_queryset(**dados)
        return {'hoteis': self.serialize(queryset)}

    def serialize(self, queryset):
        return [ h.serialize() for h in queryset ]


class Hotel(Resource):
    param_args = reqparse.RequestParser()
    param_args.add_argument('nome', type=str, required=True, help="The field 'nome' cannot be left blank")
    param_args.add_argument('estrelas', type=float, required=True, help="The field 'estrela' cannot be left blank")
    param_args.add_argument('diaria')
    param_args.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.get_or_none(hotel_id)
        if hotel:
            return hotel.serialize(), 200
        return {'message': 'Hotel not found.'}, 401

    def post(self, hotel_id):
        hotel = HotelModel.get_or_none(hotel_id)
        if hotel:
            return {'message': f'Hotel id {hotel_id} already exists.'}, 401

        dados = Hotel.param_args.parse_args()
        try:
            novo_hotel = HotelModel.perform_save(hotel_id, **dados)
        except Exception:
            return {'message': 'An error ocurred tryint to save hotel.'}, 500
        return novo_hotel.serialize(), 200

    def put(self, hotel_id):
        hotel = HotelModel.get_or_none(hotel_id)
        if not hotel:
            return {'message': f'Hotel id {hotel_id} not found.'}, 401

        dados = Hotel.param_args.parse_args()
        try:
            novo_hotel = HotelModel.perform_update(hotel_id, **dados)
        except Exception:
            return {'message': 'An error ocurred tryint to save hotel.'}, 500
        return novo_hotel.serialize(), 201

    def delete(self, hotel_id):
        hotel = HotelModel.get_or_none(hotel_id)
        if not hotel:
            return {'message': f'Hotel id {hotel_id} not found.'}, 401
        try:
            hotel.remove()
        except Exception:
            return {'message': 'An error ocurred tryint to delete hoel.'}, 500
        return {'message': 'Hotel deleted.'}, 200