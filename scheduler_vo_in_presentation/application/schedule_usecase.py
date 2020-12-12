import inject

from domain.schedule.schedule import Schedule
from domain.schedule.schedule_id import ScheduleId
from domain.schedule.schedule_date import ScheduleDate
from domain.schedule.schedule_title import ScheduleTitle
from domain.schedule_reposotory import IScheduleRepository


class ScheduleUsecase:
    @inject.params(repository=IScheduleRepository)
    def __init__(self, repository: IScheduleRepository):
        self.repository = repository

    def register_schedule(self, schedule_date: ScheduleDate, schedule_title: ScheduleTitle):
        try:
            schedule_id = ScheduleId()
            schedule_id.publish()
            schedule = Schedule(schedule_id, schedule_date, schedule_title)
        except Exception as e:
            print(e)
            raise Exception

        self.repository.save(schedule)
