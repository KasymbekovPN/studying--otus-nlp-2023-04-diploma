
# todo impl rate of resume
class Rate:
    def __init__(self, **kwargs):
        self._values = kwargs

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self._values == other._values

    @staticmethod
    def create_simple_rate(key: str, value: float):
        args = {key: value}
        return Rate(**args)

    @staticmethod
    def create_multi_rate(**kwargs):
        args = {key: value for key, value in kwargs.items() if isinstance(value, float)}
        return Rate(**args)

    @staticmethod
    def collect_rates(*args):
        rate_args = {}
        for arg in args:
            if isinstance(arg, Rate):
                rate_args = {**rate_args, **arg._values}
        return Rate(**rate_args)


# todo del
if __name__ == '__main__':

    r0 = Rate.create_simple_rate('default_we', 0.1)
    print(r0._values)

    r1 = Rate.create_multi_rate(default_we=0.9, default_skills=0.6)
    print(r1._values)

    r2 = Rate.collect_rates(r1, r0)
    print(r2._values)

    pass
