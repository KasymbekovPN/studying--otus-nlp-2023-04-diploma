from src.resume import Id as ResumeId
from src.rate import Rate, Rates


class Response:
    def __init__(self, idx: int, resume_id: ResumeId, rates: Rates) -> None:
        self._idx = idx
        self._resume_id = resume_id
        self._rates = rates

    def __repr__(self) -> str:
        return f'Request {{id: {self.idx}}}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.idx == other.idx and self.resume_id == other.resume_id and self.rates == other.rates

    @property
    def idx(self) -> int:
        return self._idx

    @property
    def resume_id(self) -> ResumeId:
        return self._resume_id

    @property
    def rates(self) -> Rates:
        return self._rates
