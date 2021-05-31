from app.api import bp
from flask import jsonify,request

from .planet_status import cal_status

from app.hello import (life_number,your_personal,hearts_d,image_num,real)

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
    
@bp.route('/api/num/planet-status/<path:data>', methods=['GET'])
def status(data):
    _list = data.split('/')
    return cal_status(int(_list[0]),int(_list[1]),int(_list[2]))
    #return jsonify(_list)
    #return cal_status(22,2,1982)