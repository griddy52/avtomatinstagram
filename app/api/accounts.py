from flask import Blueprint

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/api/accounts', methods=['GET'])
def get_accounts():
    return {"accounts": []} 