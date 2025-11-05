from __future__ import annotations

class EcommerceException(Exception):
    """Excepción base del dominio E-commerce.

    Atributos:
        user_message: Mensaje claro para el usuario.
        technical_message: Detalle técnico para logs.
    """

    def __init__(self, user_message: str, technical_message: str | None = None, cause: Exception | None = None):
        super().__init__(technical_message or user_message)
        self._user_message = user_message
        self._technical_message = technical_message or user_message
        if cause is not None:
            self.__cause__ = cause

    def get_user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        return f"{self._user_message} | {self._technical_message}"
