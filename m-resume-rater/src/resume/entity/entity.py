from enum import Enum


class Entity(Enum):
    CV = 0, 'cv'
    EDUCATION = 1, 'education'
    REFRESHER_COURSES = 2, 'refresher_courses'
    SHORT_ABOUT = 3, 'short_about'
    SKILLS = 4, 'skills'
    SPECIALIZATION = 5, 'specialization'
    WORK_EXPERIENCE = 6, 'work_experience',
    POSITION = 7, 'position'
