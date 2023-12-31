from src.resume import Id as ResumeId, Part


class Request:
    def __init__(self, idx: int, resume_id: ResumeId, part: Part) -> None:
        self._idx = idx
        self._resume_id = resume_id
        self._part = part

    def __repr__(self) -> str:
        return f'Request {{id: {self.idx}, resume_id: {self.resume_id} }}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.idx == other.idx and self.resume_id == other.resume_id and self.part == other.part

    @property
    def idx(self) -> int:
        return self._idx

    @property
    def resume_id(self) -> ResumeId:
        return self._resume_id

    @property
    def part(self) -> Part:
        return self._part
