import uuid


class ScheduleId:
    def __init__(self):
        self.schedule_id = None

    def publish(self):
        schedule_id = uuid.uuid1()
        self.schedule_id = schedule_id

        return ScheduleId
