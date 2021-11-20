from app.api import bp
from flask import jsonify,request,render_template,make_response

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

@bp.route('/api/num/queryString', methods=['GET', 'POST'])
def query_string():
    user = request.args.get('pas')
    print("user = ",type(user))
    return jsonify(user)

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

#

# rendering contact.html template and making JSON response
###from flask import Flask, render_template, jsonify
# using Flask-WTF CSRF protection for AJAX requests
###from flask_wtf.csrf import CSRFProtect
# initializing app
###app = Flask(__name__)
# protecting our app 
###csrf = CSRFProtect(app)
from flask_mail import Message

@bp.route('/api/num/contact', methods=['GET', 'POST']) ##document/my website/how-to..
def contact():
    """User can send e-mail via contact form"""
    
    if request.method == 'POST':
        """User sent an email request"""
        
        msg = Message("Feedback", recipients=['oprincely@gmail.com'])
        msg.body = "You have received new feedback from {0} {1} <{2}>.\n\n {3}".format(
            request.form['first-name'],
            request.form['last-name'],
            request.form['mail-address'],
            request.form['comment-field'])
        print('msg.body = ',msg.body)
        try:
            mail.send(msg)
            msg = "We will respond as soon as possible."
            category = "success"
        except Exception as err:
            msg = str(err)
            category = "danger"

        resp = {'feedback': msg, 'category': category}
        return make_response(jsonify(resp), 200)

    elif request.method == 'GET':
        """User is viewing the page"""
        return render_template('medium_contact_example/contact.html')