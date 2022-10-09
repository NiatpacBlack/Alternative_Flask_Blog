from flask import Blueprint, render_template, request, url_for, redirect, flash

from authentication.forms import SignUpForm
from authentication.services import add_new_user_in_user_table
from werkzeug.security import generate_password_hash, check_password_hash

authentication = Blueprint('authentication', __name__)


@authentication.route('/sign_in')
def sign_in_view():
    """Представление страницы авторизации пользователя."""

    return render_template('authentication/login_page.html', title='Вход')


@authentication.route('/sign_out')
def sign_out_view():
    """Представление страницы выхода пользователя из своего профиля."""

    pass


@authentication.route('/sign_up', methods=['POST', 'GET'])
def sign_up_view():
    """Представление страницы регистрации пользователя."""

    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        add_new_user_in_user_table(
            username=request.form['username'],
            email=request.form['email'],
            hash_password=generate_password_hash(request.form['password']),
        )
        return redirect(url_for('home_view'))

    return render_template(
        'authentication/registration_page.html',
        form=form,
        title='Регистрация',
    )
