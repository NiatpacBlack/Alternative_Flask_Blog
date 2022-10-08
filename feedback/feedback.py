from flask import Blueprint, render_template

feedback = Blueprint('feedback', __name__)


@feedback.route('/')
def feedback_view():
    """Отображение страницы с формой обратной связи."""

    return render_template('feedback/feedback_page.html', title='Обратная связь')
