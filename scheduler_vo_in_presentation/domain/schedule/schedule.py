from domain.schedule.schedule_id import ScheduleId
from domain.schedule.schedule_date import ScheduleDate
from domain.schedule.schedule_title import ScheduleTitle


class Schedule:
    def __init__(self,
                 schedule_id: ScheduleId,
                 schedule_date: ScheduleDate,
                 schedule_title: ScheduleTitle):
        self.schedule_id = schedule_id
        self.schedule_date = schedule_date
        self.schedule_title = schedule_title
