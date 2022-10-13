from flask import Blueprint, render_template, request, url_for, redirect, abort
from flask_login import login_required, current_user
from loguru import logger

from blog.forms import CreatePostForm, photos, CreateCommentForm
from blog.services import (
    add_post_in_post_model,
    get_all_posts_from_post_model,
    get_post_from_post_model_where_id,
    get_five_last_posts_from_posts_table, add_comment_in_comments_table, get_comments_from_comments_table_where_post_id,
    get_all_posts_from_post_model_on_page,
)

blog = Blueprint("blog", __name__)


@blog.route("/", methods=["GET", "POST"])
@logger.catch
def blog_view():
    """Отображение страницы блога со всеми статьями."""

    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    return render_template(
        "blog/blog_page.html",
        title="Блог",
        posts_for_page=get_all_posts_from_post_model_on_page(page=page),
    )


@blog.route("/create_post", methods=["GET", "POST"])
@login_required
@logger.catch
def create_post_view():
    """Отображение страницы с формой создания поста."""

    form = CreatePostForm()

    if request.method == "POST":
        post = {
            "title": request.form["title"],
            "image": photos.save(form.image.data),
            "description": request.form["description"],
            "text": request.form["text"],
            "author": current_user.id,
        }
        add_post_in_post_model(post)
        return redirect(url_for("blog.blog_view"))

    return render_template(
        "blog/create_post_page.html",
        title="Создать пост",
        form=form,
    )


@blog.route("/post-<int:post_id>", methods=["GET", "POST"])
def post_page_view(post_id):
    """
    Страница отображающая полную информацию из определенной статьи блога.

    Дополнительно на странице отображаются пять последних постов из таблицы PostModel без текущего поста.
    """

    comment_form = CreateCommentForm()

    if not get_post_from_post_model_where_id(post_id):
        abort(404)

    if request.method == "POST" and comment_form.validate_on_submit():
        comment = {
            "post_id": post_id,
            "user_id": current_user.id,
            "text": request.form.get('text'),
        }
        add_comment_in_comments_table(comment)
    return render_template(
        "blog/post_page.html",
        post=get_post_from_post_model_where_id(post_id),
        five_last_posts=get_five_last_posts_from_posts_table(post_id),
        comment_form=comment_form,
        all_comments=get_comments_from_comments_table_where_post_id(post_id),
    )
