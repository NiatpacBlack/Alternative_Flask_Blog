from flask import Blueprint, render_template
from flask_login import login_required

from feedback.forms import FeedbackForm

feedback = Blueprint("feedback", __name__)


@feedback.route("/")
@login_required
def feedback_view():
    """Отображение страницы с формой обратной связи."""

    form = FeedbackForm()
    return render_template(
        "feedback/feedback_page.html",
        form=form,
        title="Обратная связь",
    )
