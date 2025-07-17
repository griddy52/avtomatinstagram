from flask import Blueprint

schedule_bp = Blueprint('schedule', __name__)

@schedule_bp.route('/api/schedule/tasks', methods=['GET'])
def get_tasks():
    return {"tasks": []} 