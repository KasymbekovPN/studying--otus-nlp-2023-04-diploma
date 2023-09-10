from enum import Enum


class UserState(Enum):
    NONE = -1, 'none-state'
    INIT = 0, 'initial-state'
    EXEC = 1, 'execution-state'


# todo test
class User:
    def __init__(self, user_id: int) -> None:
        self._id = user_id
        self._state = UserState.NONE

    def __repr__(self) -> str:
        return f'Useer {{ id: {self.user_id}, state: {self.state.value[1]} }}'

    @property
    def user_id(self) -> int:
        return self._id

    @property
    def state(self) -> UserState:
        return self._state

    @state.setter
    def state(self, state: UserState) -> None:
        self._state = state
