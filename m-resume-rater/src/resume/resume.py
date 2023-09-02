from src.resume.parts.id import Id
from src.resume.parts.part import Part


class Resume:
    SHORT_ABOUT_KEYS = ('short_about',)
    SPECIALIZATION_KEYS = ('specialization',)
    CV_KEYS = ('cv',)
    EDUCATION_KEYS = ('education',)
    REFRESHER_COURSES_KEYS = ('refresher_courses',)
    WORK_EXPERIENCE_KEYS = ('work_experience',)
    SKILLS_KEYS = ('skills',)

    def __init__(self, resume_id: Id, **kwargs):
        def extract(keys: tuple, args: dict) -> Part | None:
            for key in keys:
                if key in args and isinstance(args[key], Part):
                    return args[key]
            return None

        self._resume_id = resume_id
        self._short_about = extract(self.SHORT_ABOUT_KEYS, kwargs)
        self._specialization = extract(self.SPECIALIZATION_KEYS, kwargs)
        self._cv = extract(self.CV_KEYS, kwargs)
        self._education = extract(self.EDUCATION_KEYS, kwargs)
        self._refresher_courses = extract(self.REFRESHER_COURSES_KEYS, kwargs)
        self._work_experience = extract(self.WORK_EXPERIENCE_KEYS, kwargs)
        self._skills = extract(self.SKILLS_KEYS, kwargs)

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
