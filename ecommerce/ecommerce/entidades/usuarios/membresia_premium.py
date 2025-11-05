from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_PREMIUM, ENVIO_PREMIUM
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_premium_strategy import DescuentoPremiumStrategy
from ecommerce.patrones.strategy.impl.envio_premium_strategy import EnvioPremiumStrategy


class MembresiaPremium(Membresia):
    """Membresía Premium con descuento y costo de envío reducido."""

    def get_tipo(self) -> str:
        return "PREMIUM"

    def get_descuento(self) -> float:
        return DESCUENTO_PREMIUM

    def get_costo_envio(self) -> float:
        return ENVIO_PREMIUM

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoPremiumStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioPremiumStrategy()

    def __str__(self) -> str:
        return f"MembresiaPremium(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaPremium:
        return cls()
