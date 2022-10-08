from flask import session


def login_admin() -> None:
    """В сессии создается записать со значением 1, означающую, что админ вошел в админ панель."""

    session['admin_logged'] = 1


def check_admin_is_logged() -> bool:
    """Проверяет, вошел ли администратор в админ-панель."""

    return True if session.get('admin_logged') else False


def logout_admin() -> None:
    """Удаляет запись об авторизации админа из сессии."""

    session.pop('admin_logged', None)
