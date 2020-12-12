from domain.schedule_reposotory import IScheduleRepository
from domain.schedule.schedule import Schedule


class InMemoryScheduleRepository(IScheduleRepository):
    def save(self, schedule: Schedule):
        pass
