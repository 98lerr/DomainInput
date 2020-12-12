from abc import ABCMeta, abstractmethod
from domain.schedule.schedule import Schedule


class IScheduleRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, schedule: Schedule):
        raise NotImplementedError
