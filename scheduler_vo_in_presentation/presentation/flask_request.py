from japanera import Japanera, EraDate
from datetime import datetime
import traceback

from domain.schedule.schedule_date import ScheduleDate
from domain.schedule.schedule_title import ScheduleTitle


class FlaskRequest:
    def __init__(self):
        self.request = {}

    def no_convert(self, schedule_year: str, schedule_month: str, schedule_day: str, schedule_title: str):
        self.request["schedule_year"] = int(schedule_year)
        self.request["schedule_month"] = int(schedule_month)
        self.request["schedule_day"] = int(schedule_day)
        self.request["schedule_title"] = schedule_title

    def convert_from_wareki(self,
                            schedule_year: str,
                            schedule_month: str,
                            schedule_day: str,
                            schedule_title: str):
        schedule_date = self._convert_from_wareki_to_date(schedule_year,
                                                          schedule_month,
                                                          schedule_day)

        self.request["schedule_year"] = int(schedule_date.year)
        self.request["schedule_month"] = int(schedule_date.month)
        self.request["schedule_day"] = int(schedule_date.day)
        self.request["schedule_title"] = schedule_title

        domain_schedule_date = ScheduleDate(self.request["schedule_year"],
                                            self.request["schedule_month"],
                                            self.request["schedule_day"]
                                            )
        domain_schedule_title = ScheduleTitle(self.request["schedule_title"])
        return domain_schedule_date, domain_schedule_title

    @staticmethod
    def _convert_from_wareki_to_date(year: str, month: str, day: str) -> datetime:
        input_year_month_day = "{}年{}月{}日".format(year, month, day)
        japanera = Japanera()

        try:
            converted_date = japanera.strptime(input_year_month_day, "%-E%-O年%m月%d日")[0]

        except TypeError as e:
            traceback.print_exc()
            raise e
        except ValueError as e:
            traceback.print_exc()
            raise e
        except IndexError as e:
            traceback.print_exc()
            raise e

        return converted_date

    def to_dict(self):
        return {
            "schedule_year": self.request.get("schedule_year"),
            "schedule_month": self.request.get("schedule_month"),
            "schedule_day": self.request.get("schedule_day"),
            "schedule_title": self.request.get("schedule_title")
        }
