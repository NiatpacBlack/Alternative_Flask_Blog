from blog.models import PostModel


def find_query_in_posts_table_on_page(query: str, page: int):
    """
    Возвращает QuerySet всех постов на странице page из таблицы PostModel, где были найдены соответствия query.

    Соответствия ищутся в заголовке title и контенте поста text.
    """

    return PostModel.query.order_by(PostModel.id.desc()).filter(
        PostModel.text.like(f'%{query}%') | PostModel.title.like(f'%{query}%')
    ).paginate(page=page, per_page=5)
