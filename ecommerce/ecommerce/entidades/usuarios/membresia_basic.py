from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_BASIC, ENVIO_BASIC
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_basic_strategy import DescuentoBasicStrategy
from ecommerce.patrones.strategy.impl.envio_basic_strategy import EnvioBasicStrategy


class MembresiaBasic(Membresia):
    """Membresía básica sin descuento y con costo de envío estándar."""

    def get_tipo(self) -> str:
        return "BASIC"

    def get_descuento(self) -> float:
        return DESCUENTO_BASIC

    def get_costo_envio(self) -> float:
        return ENVIO_BASIC

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoBasicStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioBasicStrategy()

    def __str__(self) -> str:
        return f"MembresiaBasic(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaBasic:
        return cls()
