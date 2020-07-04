from flask import Blueprint, render_template, url_for, redirect, request, session

import datetime
from app.genum import generate_numbers
from app.hello import contains_y,jeff, life_number,your_personal,real,hearts_d,image_num,bddict,year_num,lesson,debt
from app.hello import check_karma,peak,digit_sum,b_t_ms

x = datetime.datetime.now()
year_now = x.year


bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html',year_now=year_now)

@bp.route('/profile', methods=['GET', 'POST'])
#@login_required
def profile():
    msg=''
    return render_template('profile.html',msg=msg,year_now=year_now)


#-------------------Numerology Readings----------------------#

@bp.route('/event')
#@login_required
def event():
    
    
    e = generate_numbers('uchechukwu','emeka','okwu','22','02','1982')[3]
    
    return render_template('event.html',exp11=e[0],sU=e[1],iM1=e[2],lp=e[3],Mrity=e[4],phy=e[5],men=e[6],emo=e[7],intt=e[8],one=e[9],
                            two=e[10],thr=e[11],fou=e[12],fiv=e[13],six=e[14],sev=e[15],eig=e[16],nin=e[17],ps=e[18],cH=e[19],cH1=e[20],cH2=e[21],cH3=e[22],
                            Essence=e[23],pynum=e[24],uniynum=e[25],pina=e[26],rc=e[27],pmonth=e[28],uniday=e[29],pday=e[30],Gpina=e[31],Gcha=e[32],Gper_pi=e[33],
                            Gper_cha=e[34],k_day=e[35],k_pday=e[36],year_now=e[37])


@bp.route('/reading')
#@login_required
def reading():
    
    
    r = generate_numbers('uchechukwu','emeka','okwu','22','02','1982')[0]
    
    return render_template('reading.html', exp=r[0],exp11=r[1], sU=r[2], sU1=r[3], iM=r[4], iM1=r[5],
                           hP=r[6], ln=r[7], lp=r[8],bd1=r[9], lb=r[10], cH=r[11], cH1=r[12], cH2=r[13], cH3=r[14], LEB=r[15], 
                            Mrity=r[16],cha=r[17],btd1=r[18],bd22=r[19],p1=r[20],p11=r[21],p2=r[22],p22=r[23],p3=r[24],
                            p33=r[25],p4=r[26],p44=r[27],year_now=r[28],py_num=r[29],karma=r[30],karma1=[31],karma2=r[32],                           
                           FN=FN,MN=MN,LN=LN,btd=btd,btm=btm,bty=bty,life_number=life_number,b_t_ms=b_t_ms,bddict=bddict,
                           year_num=year_num,lesson=lesson,debt=debt,your_personal=your_personal,real=real,peak=peak,
                           hearts_d=hearts_d,image_num=image_num,)


@bp.route('/reading1')
#@login_required
def reading1():
    
    
    r = generate_numbers('uchechukwu','emeka','okwu','22','02','1982')[2]#[1]
    
    return 'soon'#render_template('reading1.html',FN=FN,lp=lp,A=A,B=B,C=C,D=D,E=E,F=F,G=G,H=H,I=I,
                 #          Rall=Rall,R1all=R1all,R2all=R2all,R3all=R3all,R4all=R4all,R5all=R5all,R6all=R6all,R7all=R7all,
                 #          p=p,missing_numbers=missing_numbers,bash1=bash1,bash2=bash2,bash3=bash3,
                 #          bash4=bash4,bash5=bash5,bash6=bash6,bash7=bash7,bash8=bash8,bash9=bash9,year_now=year_now)