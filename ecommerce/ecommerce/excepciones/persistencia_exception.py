from .ecommerce_exception import EcommerceException

class PersistenciaException(EcommerceException):
    """Error leyendo o escribiendo datos en disco."""

    def __init__(self, path: str, operacion: str, cause: Exception | None = None):
        super().__init__(
            user_message="Ocurrió un error de almacenamiento.",
            technical_message=f"Persistencia fallida: {operacion} en '{path}'",
            cause=cause,
        )
        self._path = path
        self._operacion = operacion

    def get_path(self) -> str:
        return self._path

    def get_operacion(self) -> str:
        return self._operacion
