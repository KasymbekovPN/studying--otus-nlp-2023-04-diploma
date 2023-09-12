from src.resume import Entity


# todo test
class Rate:
    def __init__(self, entity: Entity, label: str, value=0.0, description=''):
        self._entity = entity
        self._label = label
        self._value = value
        self._description = description

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value and \
            self.description == other.description and \
            self.entity == other.entity and \
            self.label == other.label

    @property
    def entity(self) -> Entity:
        return self._entity

    @property
    def label(self) -> str:
        return self._label

    @property
    def value(self) -> float:
        return self._value

    @property
    def description(self) -> str:
        return self._description


# todo test
class Rates:
    def __init__(self):
        self._rates = {}

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rates):
            return False
        return self.rates == other.rates

    @property
    def rates(self) -> dict:
        return self._rates

    def add(self, rate: Rate):
        entity = rate.entity
        if entity not in self._rates:
            self._rates[entity] = {}
        self._rates[entity][rate.label] = rate
