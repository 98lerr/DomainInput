from flask import Flask, jsonify, request
import inject

from presentation.flask_request import FlaskRequest
from application.schedule_usecase import ScheduleUsecase

from domain.schedule_reposotory import IScheduleRepository
from infrastructure.inmemory_schedule_repository import InMemoryScheduleRepository


def inject_config(binder):
    binder.bind(IScheduleRepository, InMemoryScheduleRepository())


app = Flask(__name__)
inject.configure(inject_config)


@app.route("/", methods=["GET"])
@app.route("/wareki-register", methods=["GET"])
def hello_world():
    return {"message": "it works!"}


@app.route("/wareki-register", methods=["POST"])
def wareki_register():

    json_data = request.get_json()
    request_obj = FlaskRequest()
    use_case = ScheduleUsecase()

    input_year = json_data.get("schedule-year")
    input_month = json_data.get("schedule-month")
    input_day = json_data.get("schedule-day")
    input_title = json_data.get("schedule-title")

    try:
        schedule_year, schedule_month, schedule_day, schedule_title = request_obj.convert_from_wareki(
            schedule_year=input_year,
            schedule_month=input_month,
            schedule_day=input_day,
            schedule_title=input_title
        )

        use_case.register_schedule(
            schedule_year, schedule_day, schedule_month, schedule_title
        )

    except Exception as e:
        return jsonify({
            "type": "{}".format(type(e)),
            "args": "{}".format(e.args),
            "message": "{}".format(e),
            "inputs": [input_year, input_month, input_day, input_title]
        }), 500

    return jsonify(
        {
            "message": "registration succeed."
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
