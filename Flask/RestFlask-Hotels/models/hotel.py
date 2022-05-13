from sql_alchemy import db

class HotelModel(db.Model):
    __tablename__ = 'hoteis'

    hotel_id = db.Column(
        db.String, primary_key=True
    )

    nome = db.Column(
        db.String(80)
    )

    estrelas = db.Column(
        db.Float(precision=1)
    )

    diaria = db.Column(
        db.Float(precision=2)
    )

    cidade = db.Column(
        db.String(80)
    )

    def __init__(self, hotel_id, **kwargs):
        self.hotel_id = hotel_id
        self.nome = kwargs.get('nome')
        self.estrelas = kwargs.get('estrelas')
        self.diaria = kwargs.get('diaria')
        self.cidade = kwargs.get('cidade')

    def serialize(self):
        return {
            'hotel_id': self.hotel_id,
            'nome': self.nome,
            'estrelas': self.estrelas,
            'diaria': self.diaria,
            'cidade': self.cidade
        }

    @classmethod
    def get_or_none(cls, hotel_id):
        return cls.query.filter_by(hotel_id=hotel_id).first()

    @classmethod
    def get_queryset(cls, **kwargs):
        queryset = cls.query

        nome = kwargs.get('nome', '')
        if nome:
            queryset = queryset.filter_by(nome=nome)

        return queryset.all()

    def _save_instance(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def perform_save(cls, hotel_id, **data):
        new_hotel = cls(hotel_id, **data)
        new_hotel._save_instance()
        return new_hotel

    def perform_update(self, **data):
        self.nome = data.get("nome")
        self.estrelas = data.get("estrelas")
        self.diaria = data.get("diaria")
        self.cidade = data.get("cidade")
        self._save_instance()

    def remove(self):
        db.session.delete(self)
        db.session.commit()