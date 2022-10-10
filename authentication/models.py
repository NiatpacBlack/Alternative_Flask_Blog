from datetime import datetime

from app import db


class UserModel(db.Model):
    """Модель пользователя."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), default="user")
    registration_data = db.Column(db.DateTime, default=datetime.utcnow)

    def __int__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        """При помощи этого метода мы будем получать соответствующую запись из базы данных."""

        return f"<UserModel {self.id}>"
