# -*- coding: utf-8 -*-
import pytest

from presentation.flask_interface import app
from presentation.flask_request import FlaskRequest
from datetime import datetime


class TestFlaskInterface:
    @pytest.mark.parametrize(
        "schedule_year, schedule_month, schedule_day, schedule_title",
        [
            ("令和二", "二", "一", "イベント"),
            ("令和2", "12", "1", "イベント")
        ]
    )
    def test_和暦登録(self, schedule_year, schedule_month, schedule_day, schedule_title):
        with app.test_client() as client:
            response = client.post(
                "/wareki-register",
                json={
                    "schedule-year": schedule_year,
                    "schedule-month": schedule_month,
                    "schedule-day": schedule_day,
                    "schedule-title": schedule_title
                }
            )

        from pprint import pprint
        pprint(response.json)
        assert(response.status_code < 400)


class TestFlaskRequest:

    @pytest.mark.parametrize("year, month, day",
                             [
                                 ("令和2", "4", "1"),
                                 ("令和二", "4", "1"),
                                 ("令和二", "四", "一")
                             ])
    def test_和暦を受けてプリミティブ型にする(self, year, month, day):
        # request = presentation.FlaskRequest.FlaskRequest()
        request = FlaskRequest()
        request.convert_from_wareki(
            year, month, day, "タイトル"
        )
        assert request.request.get("schedule_year") == 2020
        assert request.request.get("schedule_month") == 4
        assert request.request.get("schedule_day") == 1

    @pytest.mark.parametrize("year, month, day",
                             [
                                 ("令和2", "4", "1"),
                                 ("令和二", "4", "1"),
                                 ("令和二", "四", "一")
                             ])
    def test_和暦を変換(self, year, month, day):
        # response = pyesentation.FlaskRequest.FlaskRequest._convert_from_wareki_to_date(
        response = FlaskRequest._convert_from_wareki_to_date(
                year, month, day
        )
        assert_ideal = datetime(2020, 4, 1, 0, 0)
        assert response == assert_ideal

