

class ArgDescription:
    def __init__(self, name: str, expected_type, default_value) -> None:
        self._name = name
        self._expected_type = expected_type
        self._default_value = default_value

    def __repr__(self) -> str:
        return f'ArgDescription {{ name: {self.name}, type: {self.expected_type}, default: {self.default_value} }}'

    @property
    def name(self) -> str:
        return self._name

    @property
    def expected_type(self):
        return self._expected_type

    @property
    def default_value(self):
        return self._default_value


def check_type_and_get_or_default(data: dict, descr: ArgDescription):
    key = descr.name
    return data[key] if key in data and isinstance(data[key], descr.expected_type) else descr.default_value
