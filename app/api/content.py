from flask import Blueprint

content_bp = Blueprint('content', __name__)

@content_bp.route('/api/content/folders', methods=['GET'])
def get_content_folders():
    return {"folders": []} 