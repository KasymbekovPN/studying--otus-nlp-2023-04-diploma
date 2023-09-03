
# todo impl rate of resume
class Rate:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value
