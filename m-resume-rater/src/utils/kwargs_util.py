

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


# todo del
if __name__ == '__main__':

    default_str_value = 'default_value'
    default_int_value = 100
    default_float_value = 9.87

    data_ = {
        'key0': ArgDescription('key0', str, default_str_value),
        'key1': ArgDescription('key1', str, default_str_value),
        'key2': ArgDescription('key2', int, default_int_value),
        'key3': ArgDescription('key3', int, default_int_value),
        'key4': ArgDescription('key4', float, default_float_value),
        'key5': ArgDescription('key5', float, default_float_value)
    }

    data_1 = {
        'key0': 'value',
        'key1': [],
        'key2': 123,
        'key3': 1.23,
        'key4': 1.23,
        'key5': None
    }

    for key_, value in data_.items():
        print(f'{key_} <> {value}')
        result = check_type_and_get_or_default(data_1, value)
        print(f'result: {result}')

    print(f'+++ {check_type_and_get_or_default(data_1, ArgDescription("h", str, "xixixixix"))}')
