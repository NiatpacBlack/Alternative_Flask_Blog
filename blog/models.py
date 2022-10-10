from datetime import datetime

from app import db


class PostModel(db.Model):
    """Модель поста. Из подобных постов будет состоять блог."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    created_data = db.Column(db.DateTime, default=datetime.utcnow)

    def __int__(self, title, description, text, author):
        self.title = title
        self.description = description
        self.text = text
        self.author = author

    def __repr__(self):
        """При помощи этого метода мы будем получать соответствующую запись из базы данных."""

        return f"<PostModel {self.id}>"
