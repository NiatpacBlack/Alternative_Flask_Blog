from .models import PostModel, db


def add_post_in_post_model(post: dict[str]) -> None:
    """Добавляет данные из словаря post в таблицу PostModel."""

    db_object = PostModel(
        title=post['title'],
        image=post['image'],
        description=post['description'],
        text=post['text'],
        author=post['author'],
    )
    db.session.add(db_object)
    db.session.commit()


def get_all_posts_from_post_model():
    """Возвращает QuerySet и информацией о всех постах из таблицы PostModel."""

    return PostModel.query.all()[::-1]


def get_post_from_post_model_where_id(post_id: int):
    """Возвращает QuerySet и информацией о посте из блога с id равным аргументу."""

    return PostModel.query.filter(id=post_id)
