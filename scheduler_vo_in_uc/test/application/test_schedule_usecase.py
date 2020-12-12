import pytest

from domain.schedule_reposotory import IScheduleRepository
from infrastructure.inmemory_schedule_repository import InMemoryScheduleRepository

from application.schedule_usecase import ScheduleUsecase


def inject_config(binder):
    binder.bind(IScheduleRepository, InMemoryScheduleRepository())


class TestScheduleUsecase:
    @pytest.mark.parametrize(
        "year, month, day, title",
        [
            (2020, 12, 1, "Event")
        ]
    )
    def test_register(self, year, month, day, title):
        use_case = ScheduleUsecase()
        use_case.register_schedule(year, month, day, title)

        assert True
