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


# todo del
if __name__ == '__main__':
    # r0 = Rate.create_simple_rate('default_we', 0.1)
    # print(r0._values)
    #
    # r1 = Rate.create_multi_rate(default_we=0.9, default_skills=0.6)
    # print(r1._values)
    #
    # r2 = Rate.collect_rates(r1, r0)
    # print(r2._values)
    rate_ = Rate(Entity.CV, 'default')
    rates_ = Rates()
    rates_.add(rate_)
    pass
