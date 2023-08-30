
class Status:
    def __init__(self, template: str, **kwargs):
        self._template = template
        self._args = kwargs

    def __repr__(self):
        return f'Status {{ template: {self._template}, args: {self._args} }}'

    @property
    def template(self):
        return self._template

    @property
    def args(self):
        return self._args


class Result:
    pass