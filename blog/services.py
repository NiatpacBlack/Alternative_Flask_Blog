from loguru import logger

from authentication.models import UserModel
from .models import PostModel, db, CommentModel


@logger.catch
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


@logger.catch
def get_all_posts_from_post_model_on_page(page: int):
    """Возвращает QuerySet и информацией о постах из таблицы PostModel которые соответствуют текущей странице page."""

    return PostModel.query.order_by(PostModel.id.desc()).paginate(page=page, per_page=5)


@logger.catch
def get_five_last_posts_from_posts_table(post_id: int):
    """Возвращает QuerySet пяти последних постов из таблицы PostModel без открытого поста с post_id."""

    return PostModel.query.filter(PostModel.id != post_id).limit(5)[::-1]


@logger.catch
def get_post_from_post_model_where_id(post_id: int):
    """Возвращает QuerySet и информацией о посте из блога с id равным аргументу."""

    return PostModel.query.get(post_id)


@logger.catch
def add_comment_in_comments_table(comment: dict[str]) -> None:
    """Добавляет данные из словаря comment в таблицу CommentModel."""

    db_object = CommentModel(
        post_id=comment["post_id"],
        user_id=comment["user_id"],
        text=comment["text"],
    )
    db.session.add(db_object)
    db.session.commit()


@logger.catch
def get_comments_from_comments_table_where_post_id(post_id: int):
    """
    Возвращает QuerySet из всех комментариев под постом с id post_id в обратном порядке.

    В данной функции реализуется объединение таблицы всех комментариев к посту с таблицей пользователей, чтобы
    выводить их username над комментарием в шаблоне.
    """

    return db.session.query(UserModel, CommentModel).join(CommentModel, UserModel.id == CommentModel.user_id).filter_by(
        post_id=post_id
    )[::-1]
