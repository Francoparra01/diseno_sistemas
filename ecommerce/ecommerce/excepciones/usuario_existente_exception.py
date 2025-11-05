from .ecommerce_exception import EcommerceException

class UsuarioExistenteException(EcommerceException):
    """Se intenta registrar un usuario ya existente (p.ej., por email)."""

    def __init__(self, email: str):
        super().__init__(
            user_message=f"El usuario con email '{email}' ya existe.",
            technical_message=f"Usuario duplicado: email={email}",
        )
        self._email = email

    def get_email(self) -> str:
        return self._email
