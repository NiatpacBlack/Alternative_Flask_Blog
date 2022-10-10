from flask import Blueprint, render_template

from feedback.forms import FeedbackForm

feedback = Blueprint("feedback", __name__)


@feedback.route("/")
def feedback_view():
    """Отображение страницы с формой обратной связи."""

    form = FeedbackForm()
    return render_template(
        "feedback/feedback_page.html",
        form=form,
        title="Обратная связь",
    )
