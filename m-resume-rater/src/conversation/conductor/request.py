from src.resume import Resume


class Request:
    def __init__(self, idx: int, resume: Resume) -> None:
        self._idx = idx
        self._resume = resume

    def __repr__(self) -> str:
        return f'Request {{id: {self._idx}}}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.idx == other.idx and self.resume == other.resume

    @property
    def idx(self) -> int:
        return self._idx

    @property
    def resume(self) -> Resume:
        return self._resume
