from flask import Blueprint, render_template, url_for, redirect, request, session

from flask_login import current_user, login_user,login_required,logout_user
from app import db
from app.models import User,Post
from app.auth.forms import PostForm

import datetime
from app.genum import generate_numbers
from app.hello import contains_y,jeff, life_number,your_personal,real,hearts_d,image_num,bddict,year_num,lesson,debt
from app.hello import check_karma,peak,digit_sum,b_t_ms
from app.hello1 import missing_numbers
from app.destiny_num import destiny,birthForce,heart_desire

from app.auth.forms import NumberOfQuestions,AskQuestions

x = datetime.datetime.now()
year_now = x.year


bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html',year_now=year_now)


@bp.route('/about')
def about():
    return render_template('about.html',year_now=year_now)

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = PostForm()
    user = User.query.filter_by(username=current_user.username).first()
    print(user.number_of_questions)
    if user.number_of_questions == 0:
        msg = 'You do not have enough questions'
    else:
        msg = ''
    if user.number_of_questions != 0 and form.validate_on_submit():
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        
        
        user.number_of_questions = user.number_of_questions - 1
        
        db.session.commit()
        
        msg = 'You will receive a reply soon'
        
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    return render_template('profile.html',msg=msg,year_now=year_now,form=form)

#------------------Payments ----------------------#
@bp.route('/questions', methods=['GET', 'POST'])
@login_required
def question():
    form = NumberOfQuestions()
    if form.validate_on_submit():
        numberofquestions = int(form.numberofquestions.data)
        usertoupdate = form.username.data
        
        user = User.query.filter_by(username=usertoupdate).first()
        
        user.number_of_questions = numberofquestions
        db.session.commit()
        
        #msg = 'Number Of Questions Updated'
        return 'Number Of Questions Updated'
    return render_template('questions.html', form=form)

#------------------Payments Ends----------------------#

#------------------Ask Question----------------------#

@bp.route('/ask', methods=['GET', 'POST'])
@login_required
def askQuestion():
    form = AskQuestions()
    if form.validate_on_submit():
        question = form.numberofquestions.data
        
        user = User.query.filter_by(username=current_user).first()
        
        #user.number_of_questions = numberofquestions
        #db.session.commit()
        
        #msg = 'Number Of Questions Updated'
        return 'Number Of Questions Updated'
    return render_template('questions.html', form=form)

#------------------Ask Question Ends----------------------#

#------------------- Payment successful ----------------------#
@bp.route('/paysuccess')
@login_required
def paysuccess():
    return render_template('paysuccess.html')
#------------------- Payment successful End ----------------------#

#-------------------Numerology Readings----------------------#

@bp.route('/event')
@login_required
def event():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    
    FN = user.firstname
    MN = user.middlename
    LN = user.lastname
    
    btd = user.dob[0:2] #1982
    btm = user.dob[3:5] #02
    bty = user.dob[6:10] #22
    
    e = generate_numbers(FN,MN,LN,btd,btm,bty)[3]
    
    #e = generate_numbers('uchechukwu','emeka','okwu','22','02','1982')[3]
    
    return render_template('event.html',exp11=e[0],sU=e[1],iM1=e[2],lp=e[3],Mrity=e[4],phy=e[5],men=e[6],emo=e[7],intt=e[8],one=e[9],
                            two=e[10],thr=e[11],fou=e[12],fiv=e[13],six=e[14],sev=e[15],eig=e[16],nin=e[17],ps=e[18],cH=e[19],cH1=e[20],cH2=e[21],cH3=e[22],
                            Essence=e[23],pynum=e[24],uniynum=e[25],pina=e[26],rc=e[27],pmonth=e[28],uniday=e[29],pday=e[30],Gpina=e[31],Gcha=e[32],Gper_pi=e[33],
                            Gper_cha=e[34],k_day=e[35],k_pday=e[36],year_now=e[37])


@bp.route('/reading')
@login_required
def reading():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    
    FN = user.firstname
    MN = user.middlename
    LN = user.lastname
    
    btd = user.dob[0:2] #1982
    btm = user.dob[3:5] #02
    bty = user.dob[6:10] #22
    
    r = generate_numbers(FN,MN,LN,btd,btm,bty)[0]
    
    #r = generate_numbers('uchechukwu','emeka','okwu','22','02','1982')[0]
    
    return render_template('reading.html', exp=r[0],exp11=r[1], sU=r[2], sU1=r[3], iM=r[4], iM1=r[5],
                           hP=r[6], ln=r[7], lp=r[8],bd1=r[9], lb=r[10], cH=r[11], cH1=r[12], cH2=r[13], cH3=r[14], LEB=r[15], 
                            Mrity=r[16],cha=r[17],btd1=r[18],bd22=r[19],p1=r[20],p11=r[21],p2=r[22],p22=r[23],p3=r[24],
                            p33=r[25],p4=r[26],p44=r[27],year_now=r[28],py_num=r[29],karma=r[30],karma1=[31],karma2=r[32],                           
                           FN=FN,MN=MN,LN=LN,btd=btd,btm=btm,bty=bty,life_number=life_number,b_t_ms=b_t_ms,bddict=bddict,
                           year_num=year_num,lesson=lesson,debt=debt,your_personal=your_personal,real=real,peak=peak,
                           hearts_d=hearts_d,image_num=image_num,)


@bp.route('/reading1')
@login_required
def reading1():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    
    FN = user.firstname
    MN = user.middlename
    LN = user.lastname
    
    btd = user.dob[0:2] #1982
    btm = user.dob[3:5] #02
    bty = user.dob[6:10] #22
    
    r = generate_numbers(FN,MN,LN,btd,btm,bty)[1]
    
    #r = generate_numbers('uchechukwu','emeka','okwu','22','02','1982')[2]#[1]
    
    return render_template('reading1.html',FN=FN,lp=r[0],A=r[1],B=r[2],C=r[3],D=r[4],E=r[5],F=r[6],G=r[7],H=r[8],I=r[9],
                           Rall=r[10],R1all=r[11],R2all=r[12],R3all=r[13],R4all=r[14],R5all=r[15],R6all=r[16],R7all=r[17],
                           missing_numbers=missing_numbers,p=r[18],bash1=r[19],bash2=r[20],bash3=r[21],
                           bash4=r[22],bash5=r[23],bash6=r[24],bash7=r[25],bash8=r[26],bash9=r[27],year_now=year_now)

    
@bp.route('/fullreading', methods=['GET', 'POST'])
@login_required
def fullreading():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    
    if user.username == 'admin':
        FN = user.firstname
        MN = user.middlename
        LN = user.lastname
        
        btd = user.dob[0:2] #1982
        btm = user.dob[3:5] #02
        bty = user.dob[6:10] #22
        
        r = generate_numbers(FN,MN,LN,btd,btm,bty)[2]
        
        return render_template('transit/fullreading.html',
                               exp=r[0],exp11=r[1],ln=r[2], lp=r[3],year_now=r[4],sU=r[5], sU1=r[6],
                               destiny=destiny,birthForce=birthForce,heart_desire=heart_desire)
    return 'ACCESS DENIED'
