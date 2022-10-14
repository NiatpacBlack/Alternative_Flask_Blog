from flask import Blueprint, render_template, request
from loguru import logger

from search.services import find_query_in_posts_table_on_page

search = Blueprint("search", __name__)


@search.route("/", methods=["GET"])
@logger.catch
def search_view():
    """Отображение страницы с формой поиска постов в блоге."""

    page = request.args.get("page")
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    search_result = ""
    if request.args.get("query"):
        search_result = find_query_in_posts_table_on_page(
            query=request.args.get("query"),
            page=page,
        )

    return render_template(
        "search/search_page.html",
        title="Найти статью",
        search_result=search_result,
        query=request.args.get("query"),
    )
