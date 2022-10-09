from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email


class FeedbackForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(),
            Length(max=255),
        ],
        render_kw={
            'class': 'form-control',
            "placeholder": "Ваше имя",
        },
    )
    email = StringField(
        'Email',
        validators=[
            Email(message='Введенный email некорректен'),
            DataRequired(),
            Length(max=255),
        ],
        render_kw={
            'class': 'form-control',
            "placeholder": "Ваш email",
        },
    )

    description = PasswordField(
        'Description',
        validators=[DataRequired(), Length(max=255)],
        render_kw={
            'class': 'form-control help',
            "placeholder": "Описание",
        },
    )
    content = TextAreaField(
        'Content',
        validators=[DataRequired()],
        render_kw={
            'class': 'form-control help',
            "placeholder": "Текст сообщения",
        },
    )
    submit = SubmitField(
        "Отправить",
        render_kw={'class': 'btn btn-info'},
    )
