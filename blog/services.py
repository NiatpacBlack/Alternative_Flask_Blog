from .models import PostModel, db


def add_post_in_post_model(post: dict[str]) -> None:
    """Добавляет данные из словаря post в таблицу PostModel."""

    db_object = PostModel(
        title=post["title"],
        image=post["image"],
        description=post["description"],
        text=post["text"],
        author=post["author"],
    )
    db.session.add(db_object)
    db.session.commit()


def get_all_posts_from_post_model():
    """Возвращает QuerySet и информацией о всех постах из таблицы PostModel."""

    return PostModel.query.all()[::-1]


def get_five_last_posts_from_posts_table(post_id: int):
    """Возвращает QuerySet пяти последних постов из таблицы PostModel без открытого поста с post_id."""

    return PostModel.query.filter(PostModel.id != post_id).limit(5)[::-1]


def get_post_from_post_model_where_id(post_id: int):
    """Возвращает QuerySet и информацией о посте из блога с id равным аргументу."""

    return PostModel.query.get(post_id)
