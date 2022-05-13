from sql_alchemy import db

class UserModel(db.Model):
    __tablename__ = 'usuarios'

    user_id = db.Column(
        db.Integer, primary_key=True
    )

    login = db.Column(
        db.String(40)
    )

    password = db.Column(
        db.String(40)
    )

    def __init__(self, **kwargs):
        self.login = kwargs.get('login')
        self.password = kwargs.get('password')

    def serialize(self):
        return {
            'user_id': self.user_id,
            'login': self.login
        }

    @classmethod
    def get_or_none(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    @classmethod
    def get_by_login(cls, login):
        return cls.query.filter_by(login=login).first()

    @classmethod
    def get_queryset(cls, **kwargs):
        queryset = cls.query

        login = kwargs.get('login', '')
        if login:
            queryset = queryset.filter_by(login=login)

        return queryset.all()

    def _save_instance(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def perform_save(cls, **data):
        new_hotel = cls(**data)
        new_hotel._save_instance()
        return new_hotel

    def perform_update(self, **data):
        self.login = data.get("login")
        if data.get("password"):
            self.password = data.get("password")
        self._save_instance()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod()
