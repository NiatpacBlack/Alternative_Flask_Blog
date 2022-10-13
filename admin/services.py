from flask import session
from loguru import logger


@logger.catch
def login_admin() -> None:
    """В сессии создается записать со значением 1, означающую, что админ вошел в админ панель."""

    session["admin_logged"] = 1


@logger.catch
def check_admin_is_logged() -> bool:
    """Проверяет, вошел ли администратор в админ-панель."""

    return True if session.get("admin_logged") else False


@logger.catch
def logout_admin() -> None:
    """Удаляет запись об авторизации админа из сессии."""

    session.pop("admin_logged", None)
