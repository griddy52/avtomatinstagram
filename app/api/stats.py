from flask import Blueprint

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/api/stats/dashboard', methods=['GET'])
def get_dashboard_stats():
    return {"stats": {}} 