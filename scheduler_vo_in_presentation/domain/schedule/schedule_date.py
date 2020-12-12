from datetime import date


class ScheduleDate:
    def __init__(self, year, month, day):
        try:
            date(year, month, day)
        except ValueError as e:
            raise e

        self.year = year
        self.month = month
        self.day = day
