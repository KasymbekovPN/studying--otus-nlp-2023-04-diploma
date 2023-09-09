from src.resume.parts.id import Id
from src.resume.parts.part import Part
from src.resume.entity.entity import Entity


class Resume:

    def __init__(self, resume_id: Id, **kwargs):
        def extract(entity: Entity, args: dict) -> Part | None:
            key = entity.value[1]
            return args[key] if key in args and isinstance(args[key], Part) else None

        self._resume_id = resume_id
        self._parts = {entity: extract(entity, kwargs) for entity in Entity}

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.resume_id == other.resume_id and self._parts and other._parts

    @property
    def resume_id(self) -> Id:
        return self._resume_id

    def get(self, entity: Entity) -> Part | None:
        return self._parts[entity]

    def set(self, entity: Entity, part: Part) -> None:
        self._parts[entity] = part
