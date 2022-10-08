from flask import Flask, render_template, send_from_directory, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import configure_uploads

from blog.forms import photos
from config import Config

db = SQLAlchemy()


def create_app():
    """Настройка приложения Flask."""

    app = Flask(__name__)
    app.config.from_object(Config)

    from admin.admin import admin
    from blog.blog import blog
    from feedback.feedback import feedback
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(feedback, url_prefix='/feedback')
    app.register_blueprint(blog, url_prefix='/blog')

    configure_uploads(app, photos)

    db.init_app(app)

    return app


app = create_app()


@app.route('/')
def home_view():
    """Отображение главной страницы сайта."""

    return render_template('home_page.html')


@app.route('/media/<filename>')
def get_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)


@app.errorhandler(404)
def page_not_found_view(error_text):
    """При получении ошибки 404 отобразит кастомный шаблон с информацией об ошибке. В консоль вернет 404 ошибку."""

    return render_template('404_page.html', error_text=error_text), 404


if __name__ == '__main__':
    app.run()
