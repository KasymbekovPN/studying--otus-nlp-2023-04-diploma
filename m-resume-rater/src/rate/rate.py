
# todo test
class Rate:
    def __init__(self, value=0.0, description=''):
        self._value = value
        self._description = description

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value and self.description == other.description

    @property
    def value(self):
        return self._value

    @property
    def description(self):
        return self._description


# todo test
class Rates:
    def __init__(self):
        self._rates = {}

    def add(self, label: str, rate: Rate):
        self._rates[label] = rate


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
    pass
