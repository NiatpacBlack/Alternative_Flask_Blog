from datetime import datetime

from pytz import timezone

from app import db


class PostModel(db.Model):
    """Таблица, описывающая поля поста. Из подобных постов будет состоять блог."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('user_model.id', ondelete="CASCADE"))
    created_data = db.Column(db.DateTime, default=datetime.now(timezone('Europe/Minsk')))

    def __int__(self, title, description, text, author):
        self.title = title
        self.description = description
        self.text = text
        self.author = author

    def __repr__(self):
        return f"<PostModel {self.id}>"


class CommentModel(db.Model):
    """Таблица, хранящая данные о комментариях под конкретным постом блога."""

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post_model.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('user_model.id', ondelete="CASCADE"))
    text = db.Column(db.Text, nullable=False)
    created_data = db.Column(db.DateTime, default=datetime.now(timezone('Europe/Minsk')))

    def __repr__(self):
        return f"<CommentModel {self.id}>"
