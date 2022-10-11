from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required

from blog.forms import CreatePostForm, photos
from blog.services import (
    add_post_in_post_model,
    get_all_posts_from_post_model,
    get_post_from_post_model_where_id,
    get_five_last_posts_from_posts_table,
)

blog = Blueprint("blog", __name__)


@blog.route("/")
def blog_view():
    """Отображение страницы блога со всеми статьями."""

    return render_template(
        "blog/blog_page.html",
        title="Блог",
        posts_for_page=get_all_posts_from_post_model(),
    )


@blog.route("/create_post", methods=["GET", "POST"])
@login_required
def create_post_view():
    """Отображение страницы с формой создания поста."""

    form = CreatePostForm()

    if request.method == "POST":
        post = {
            "title": request.form["title"],
            "image": photos.save(form.image.data),
            "description": request.form["description"],
            "text": request.form["text"],
            "author": "Unknown",
        }
        add_post_in_post_model(post)
        return redirect(url_for("blog.blog_view"))

    return render_template(
        "blog/create_post_page.html",
        title="Создать пост",
        form=form,
    )


@blog.route("/post-<int:post_id>")
def post_page_view(post_id):
    """
    Страница отображающая полную информацию из определенной статьи блога.

    Дополнительно на странице отображаются пять последних постов из таблицы PostModel без текущего поста.
    """

    five_last_posts = get_five_last_posts_from_posts_table(post_id)
    post = get_post_from_post_model_where_id(post_id)
    return render_template(
        "blog/post_page.html",
        title=post.title,
        post=post,
        five_last_posts=five_last_posts,
    )
