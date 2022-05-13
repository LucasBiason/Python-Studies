from flask_restful import Resource, reqparse
from models import HotelModel

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 420.34,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'beta',
        'nome': 'Beta Hotel',
        'estrelas': 4.7,
        'diaria': 390.99,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'gama',
        'nome': 'Gama Hotel',
        'estrelas': 4.5,
        'diaria': 320.30,
        'cidade': 'Santa Catarina'
    }
]

class Hoteis(Resource):

    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('estrelas')
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return False

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        #novo_hotel = {'hotel_id': hotel_id, **dados}
        novo_hotel = HotelModel(hotel_id, **dados)
        novo_hotel = novo_hotel.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        #novo_hotel = {'hotel_id': hotel_id, **dados}
        novo_hotel = HotelModel(hotel_id, **dados)
        novo_hotel = novo_hotel.json()

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hotel = Hotel.find_hotel(hotel_id)
        if not hotel:
            return {'message': 'Hotel not found.'}, 404
        hoteis.remove(hotel)
        return {'message': 'Hotel deleted.'}, 200