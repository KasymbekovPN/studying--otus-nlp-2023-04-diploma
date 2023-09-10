from src.resume import Id as ResumeId
from src.rate import Rate


class Response:
    def __init__(self,
                 idx: int,
                 resume_id: ResumeId,
                 rate: Rate) -> None:
        self._idx = idx
        self._resume_id = resume_id
        self._rate = rate

    def __repr__(self) -> str:
        return f'Response {{id: {self.idx}, resume_id: {self.resume_id}, entity: {self.rate.entity}, label: {self.rate.label} }}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.idx == other.idx \
            and self.resume_id == other.resume_id \
            and self.rate == other.rate

    @property
    def idx(self) -> int:
        return self._idx

    @property
    def resume_id(self) -> ResumeId:
        return self._resume_id

    @property
    def rate(self) -> Rate:
        return self._rate
