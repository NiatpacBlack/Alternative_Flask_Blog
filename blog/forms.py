from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length

photos = UploadSet("photos", IMAGES)


class CreatePostForm(FlaskForm):
    """Форма создания нового поста."""

    title = StringField(
        "Название статьи",
        validators=[DataRequired(), Length(max=100)],
        render_kw={
            "class": "form-control form-control-lg",
            "placeholder": "",
        },
    )
    image = FileField(
        "Картинка",
        validators=[
            DataRequired(),
            FileAllowed(photos, "Загрузить можно только изображение"),
        ],
        render_kw={
            "class": "form-control-file",
        },
    )
    description = TextAreaField(
        "Описание",
        validators=[DataRequired(), Length(max=255)],
        render_kw={
            "class": "form-control",
            "placeholder": "",
        },
    )
    text = TextAreaField(
        "Текст статьи",
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "",
        },
    )
    submit = SubmitField(
        "Создать",
        render_kw={"class": "btn my-3 btn-primary btn-block"},
    )
