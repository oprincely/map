from app.api import bp
from flask import jsonify
from app.hello import (life_number)
#from app.models import User

@bp.route('/api/num/<int:id>', methods=['GET'])
def get_num_des(id):
    for k, v in life_number.items():
        if k == id:
            return jsonify(v)
'''
from flask import jsonify
from app.models import User

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())
    
@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass
    
@bp.route('/users', methods=['GET'])
def get_users():
    pass

@bp.route('/users/<int:id>/followers', methods=['GET'])
def get_followers(id):
    pass

@bp.route('/users/<int:id>/followed', methods=['GET'])
def get_followed(id):
    pass

@bp.route('/users', methods=['POST'])
def create_user():
    pass

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    pass
'''