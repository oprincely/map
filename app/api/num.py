from app.api import bp
from flask import jsonify,request
from app.hello import (life_number,your_personal,hearts_d,image_num,real)
#from app.models import User

@bp.route('/api/num/<int:id>/Destiny', methods=['GET'])
def get_destiny(id):    
    for k, v in your_personal.items():
        if k == id:
            return v

@bp.route('/api/num/<int:id>/Birth', methods=['GET'])
def get_birth(id):    
    for k, v in life_number.items():
        if k == id:
            return v
        
@bp.route('/api/num/<int:id>/Heart', methods=['GET'])
def get_heart(id):    
    for k, v in hearts_d.items():
        if k == id:
            return v
        
@bp.route('/api/num/<int:id>/Personality', methods=['GET'])
def get_per(id):
    for k, v in image_num.items():
        if k == id:
            return v
        
@bp.route('/api/num/<int:id>/Reality', methods=['GET'])
def get_real(id):    
    for k, v in real.items():
        if k == id:
            return v
        
@bp.route('/api/num/test', methods=['GET', 'POST'])
def testfn():    
    if request.method == 'GET':
        message = {'greeting': 'Hello from flask!'}
        return jsonify(message)
    
    if request.method == 'POST':
        print(request.get_json())
        return 'Sucess', 200
    
@bp.route('/api/num/getdata/<index_no>', methods=['GET', 'POST'])
def data_get(index_no):
    
    data = list(range(1, 30, 3))
    #print('data = ',data)

    if request.method == 'POST':
        print(request.get_text())
        return 'Ok', 200
    
    else:
        return 't_in = %s ; result: %s ; '%(index_no, data[int(index_no)])
    
    
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