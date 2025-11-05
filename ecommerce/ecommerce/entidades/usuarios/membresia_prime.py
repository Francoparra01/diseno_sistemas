from __future__ import annotations
from ecommerce.entidades.usuarios.membresia import Membresia
from ecommerce.constantes import DESCUENTO_PRIME, ENVIO_PRIME
from ecommerce.patrones.strategy.descuento_strategy import DescuentoStrategy
from ecommerce.patrones.strategy.envio_strategy import EnvioStrategy
from ecommerce.patrones.strategy.impl.descuento_prime_strategy import DescuentoPrimeStrategy
from ecommerce.patrones.strategy.impl.envio_prime_strategy import EnvioPrimeStrategy


class MembresiaPrime(Membresia):
    """Membresía Prime con descuento y envío gratuito."""

    def get_tipo(self) -> str:
        return "PRIME"

    def get_descuento(self) -> float:
        return DESCUENTO_PRIME

    def get_costo_envio(self) -> float:
        return ENVIO_PRIME

    def get_descuento_strategy(self) -> DescuentoStrategy:
        return DescuentoPrimeStrategy()

    def get_envio_strategy(self) -> EnvioStrategy:
        return EnvioPrimeStrategy()

    def __str__(self) -> str:
        return f"MembresiaPrime(Descuento: {self.get_descuento()}, Envío: {self.get_costo_envio()})"

    def __repr__(self) -> str:
        return self.__str__()

    @classmethod
    def from_dict(cls, data: dict) -> MembresiaPrime:
        return cls()
