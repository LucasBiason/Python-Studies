
class HotelModel:

    def __init__(self, hotel_id, **kwargs):
        self.hotel_id = hotel_id
        self.nome = kwargs.get('nome')
        self.estrelas = kwargs.get('estrelas')
        self.diaria = kwargs.get('diaria')
        self.cidade = kwargs.get('cidade')

    def json(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }
