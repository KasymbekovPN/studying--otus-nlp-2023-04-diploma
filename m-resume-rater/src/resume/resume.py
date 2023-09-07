from src.resume.parts.id import Id
from src.resume.parts.part import Part
from src.resume.entity.entity import Entity


class Resume:
    SHORT_ABOUT_KEYS = ('short_about',)
    SPECIALIZATION_KEYS = ('specialization',)
    CV_KEYS = ('cv',)
    EDUCATION_KEYS = ('education',)
    REFRESHER_COURSES_KEYS = ('refresher_courses',)
    WORK_EXPERIENCE_KEYS = ('work_experience',)
    SKILLS_KEYS = ('skills',)
    POSITION = ('position',)

    def __init__(self, resume_id: Id, **kwargs):
        def extract(keys: tuple, args: dict) -> Part | None:
            for key in keys:
                if key in args and isinstance(args[key], Part):
                    return args[key]
            return None

        self._resume_id = resume_id
        # todo move it to dict !!!
        self._short_about = extract(self.SHORT_ABOUT_KEYS, kwargs)
        self._specialization = extract(self.SPECIALIZATION_KEYS, kwargs)
        self._cv = extract(self.CV_KEYS, kwargs)
        self._education = extract(self.EDUCATION_KEYS, kwargs)
        self._refresher_courses = extract(self.REFRESHER_COURSES_KEYS, kwargs)
        self._work_experience = extract(self.WORK_EXPERIENCE_KEYS, kwargs)
        self._skills = extract(self.SKILLS_KEYS, kwargs)
        self._position = extract(self.POSITION, kwargs)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.resume_id == other.resume_id \
            and self.short_about == other.short_about \
            and self.specialization == other.specialization \
            and self.cv == other.cv \
            and self.education == other.education \
            and self.refresher_courses == other.refresher_courses \
            and self.work_experience == other.work_experience \
            and self.skills == other.skills \
            and self.position == other.position

    @property
    def resume_id(self) -> Id:
        return self._resume_id

    @property
    def short_about(self) -> Part | None:
        return self._short_about

    @property
    def specialization(self) -> Part | None:
        return self._specialization

    @property
    def cv(self) -> Part | None:
        return self._cv

    @property
    def education(self) -> Part | None:
        return self._education

    @property
    def refresher_courses(self) -> Part | None:
        return self._refresher_courses

    @property
    def work_experience(self) -> Part | None:
        return self._work_experience

    @property
    def skills(self) -> Part | None:
        return self._skills

    @property
    def position(self) -> Part | None:
        return self._position

    # todo remake & test
    def get(self, entity: Entity) -> Part | None:
        if entity == Entity.CV:
            return self.cv
        elif entity == Entity.EDUCATION:
            return self.education
        elif entity == Entity.REFRESHER_COURSES:
            return self.refresher_courses
        elif entity == Entity.SHORT_ABOUT:
            return self.short_about
        elif entity == Entity.SKILLS:
            return self.skills
        elif entity == Entity.SPECIALIZATION:
            return self.specialization
        elif entity == Entity.WORK_EXPERIENCE:
            return self.work_experience
        elif entity == Entity.POSITION:
            return self.position
        return None

    # todo remake & test
    def set(self, entity: Entity, part: Part) -> None:
        if entity == Entity.CV:
            self._cv = part
        elif entity == Entity.EDUCATION:
            self._education = part
        elif entity == Entity.REFRESHER_COURSES:
            self._refresher_courses = part
        elif entity == Entity.SHORT_ABOUT:
            self._short_about = part
        elif entity == Entity.SKILLS:
            self._skills = part
        elif entity == Entity.SPECIALIZATION:
            self._specialization = part
        elif entity == Entity.WORK_EXPERIENCE:
            self._work_experience = part
        elif entity == Entity.POSITION:
            self._position = part
