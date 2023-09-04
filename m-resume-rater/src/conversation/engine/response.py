from src.resume import Id as ResumeId, Entity
from src.rate import Rate


class Response:
    def __init__(self,
                 idx: int,
                 resume_id: ResumeId,
                 rate: Rate,
                 entity: Entity,
                 label: str) -> None:
        self._idx = idx
        self._resume_id = resume_id
        self._rate = rate
        self._entity = entity
        self._label = label

    def __repr__(self) -> str:
        return f'Response {{id: {self.idx}, resume_id: {self.resume_id}, entity: {self.entity}, label: {self.label} }}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.idx == other.idx \
            and self.resume_id == other.resume_id \
            and self.rate == other.rate \
            and self.entity == other.entity \
            and self.label == other.label

    @property
    def idx(self) -> int:
        return self._idx

    @property
    def resume_id(self) -> ResumeId:
        return self._resume_id

    @property
    def rate(self) -> Rate:
        return self._rate

    @property
    def entity(self) -> Entity:
        return self._entity

    @property
    def label(self) -> str:
        return self._label
