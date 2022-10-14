from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import configure_uploads
from loguru import logger

from blog.forms import photos
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


@logger.catch
def create_app():
    """Настройка приложения Flask."""

    app = Flask(__name__)
    app.config.from_object(Config)

    from admin.admin import admin
    from blog.blog import blog
    from feedback.feedback import feedback
    from authentication.authentication import authentication
    from search.search import search

    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(feedback, url_prefix="/feedback")
    app.register_blueprint(blog, url_prefix="/blog")
    app.register_blueprint(authentication, url_prefix="/authentication")
    app.register_blueprint(search, url_prefix="/search")

    configure_uploads(app, photos)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        """Если наша база данных sqlite, выполняем миграции в пакетном режиме."""

        if db.engine.url.drivername == "sqlite":
            migrate.init_app(app, db, render_as_batch=True)
        else:
            migrate.init_app(app, db)

    return app


app = create_app()


@app.route("/")
@logger.catch
def home_view():
    """Отображение главной страницы сайта."""

    return render_template("home_page.html")


@app.errorhandler(404)
def page_not_found_view(error_text):
    """При получении ошибки 404 отобразит кастомный шаблон с информацией об ошибке. В консоль вернет 404 ошибку."""

    return render_template("404_page.html", error_text=error_text), 404


@app.after_request
def redirect_to_signin(response):
    """
    Перенаправляет на страницу авторизации и сохраняет в аргумент next и url страницы, на которую заходили.

    В случае если не авторизированный пользователь заходит на страницу, требующую авторизации.
    """

    if response.status_code == 401:
        flash(
            "Пожалуйста войдите в свой аккаунт или зарегистрируйтесь, чтобы попасть в данный раздел.",
            "success",
        )
        return redirect(url_for("authentication.sign_in_view", next_page=request.url))

    return response


if __name__ == "__main__":
    app.run()
