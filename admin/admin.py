from flask import Blueprint, render_template, request, url_for, redirect, flash

from .services import login_admin, check_admin_is_logged, logout_admin
from .forms import AdminLoginForm

admin = Blueprint("admin", __name__, static_folder="static")


@admin.route("/")
def admin_page():
    """Отображает шаблон админ-панели, если пользователь прошел авторизацию."""

    if not check_admin_is_logged():
        return redirect(url_for(".admin_login"))

    return render_template(
        "admin/admin_panel.html",
        title="Админ-панель",
    )


@admin.route("/login", methods=["POST", "GET"])
def admin_login():
    """
    Отображает шаблон авторизации в админ панель, если пользователь еще не авторизован.

    При введении логина и пароля авторизует администратора в админ-панели.
    """

    if check_admin_is_logged():
        return redirect(url_for(".admin_page"))

    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "12345":
            login_admin()
            return redirect(url_for(".admin_page"))
        else:
            flash("Неверная пара логин/пароль", "danger")
    return render_template(
        "admin/admin_login.html",
        title="Админ-авторизация",
        form=AdminLoginForm(),
    )


@admin.route("/logout", methods=["POST", "GET"])
def admin_logout():
    """Удаляет запись о входе админа в админ-панель, и перемещает на страницу авторизации."""

    if check_admin_is_logged():
        logout_admin()

    return redirect(url_for(".admin_login"))
