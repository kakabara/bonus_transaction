from flask import request, jsonify, make_response, abort

from avia_transaction import app
from controllers import UserController, TransactionController


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,X-Requested-With,X-Auth-Token')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH')
    response.headers.add('Access-Control-Expose-Headers', 'X-Auth-Token')
    return response


@app.before_request
def before_request():
    if not (request.headers.environ.get('REQUEST_METHOD') == 'OPTIONS'):
        pass
        # token = request.headers.get('X-Auth-Token')
        # if not token:
        #     return abort(401)


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.route('/auth/<code>', methods=['POST'])
def authorization(code):
    UserController.auth(code)


@app.route('/users/<user_id>', methods=['GET'])
def get_user_information(user_id):
    result = UserController.get_profile(user_id)
    if result:
        return make_response(jsonify(result))
    else:
        return abort(404)


@app.route('/transactions/<card_id>', methods=['GET'])
def get_transactions(card_id):
    result = TransactionController.get(card_id)
    if result:
        return make_response(jsonify(result))
    else:
        return abort(404)



