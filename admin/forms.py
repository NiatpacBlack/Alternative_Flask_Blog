from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length


class AdminLoginForm(FlaskForm):
    """Форма авторизации в админ-панели."""

    username = StringField(
        "Username",
        validators=[DataRequired(), Length(max=50)],
        render_kw={
            "class": "form-control",
            "placeholder": "Username",
        },
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control help",
            "placeholder": "Password",
        },
    )
    submit = SubmitField(
        "Войти",
        render_kw={"class": "btn btn-default"},
    )
