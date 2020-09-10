from flask import Blueprint, render_template, url_for, redirect, request, session

from flask_login import current_user, login_user,login_required,logout_user
from app import db
from app.models import User,Post
from app.auth.forms import PostForm,PredictionForm,NumberOfQuestions,AskQuestions

import datetime
from app.hello1 import missing_numbers
from app.genum import generate_numbers
from app.hello import (contains_y,jeff, life_number,your_personal,real,hearts_d,image_num,bddict,year_num,lesson,debt,
                       check_karma,peak,digit_sum,b_t_ms)

from app.destiny_num import (destiny,birthForce,heart_desire,personality,karmas,reality,one_in_plane,two_in_plane,
                             three_in_plane,four_in_plane,six_in_plane,sev_in_plane,eig_in_plane,nin_in_plane,
                             five_in_plane,zero_in_plane,ones,twos,threes,fours,fives,sixs,sevens,eights,nines,vocation)
from app.count_numbers import (count_1s,count_2s,count_3s,count_4s,count_5s,count_6s,count_7s,count_8s,count_9s,vocation_pointer)
from app.timing import (Ess,B_T_K,E_N_W,F_O_X,I_R,C_L_U,D_M_V,G_P_Y,A_J_S,H_Q_Z)

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
    #e = generate_numbers('princely','emeka','okwuego','22','02','1982')[3]
    #e = generate_numbers('John','Joseph','Pershing','22','02','1982')[3]#[1]
    
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
        #r = generate_numbers('John','Joseph','Pershing','22','02','1982')[2]#[1]
        #r = generate_numbers('princely','emeka','okwuego','22','02','1982')[2]#[1]
        
        def num_to_strs(g): #g=r[10]
            g = digit_sum(g)
            if g == 0:
                return zero_in_plane
            elif g == 1:
                return one_in_plane
            elif g == 2:
                return two_in_plane
            elif g == 3:
                return three_in_plane
            elif g == 4:
                return four_in_plane
            elif g == 5:
                return five_in_plane
            elif g == 6:
                return six_in_plane
            elif g == 7:
                return sev_in_plane
            elif g == 8:
                return eig_in_plane
            elif g == 9:
                return nin_in_plane
        
        phy_num_to_str = num_to_strs(r[10])
        m_num_to_str = num_to_strs(r[11])
        emo_num_to_str = num_to_strs(r[12])
        i_num_to_str = num_to_strs(r[13])
        
        t_num1 = count_1s(r[14])
        t_num2 = count_2s(r[15])
        t_num3 = count_3s(r[16])
        t_num4 = count_4s(r[17])
        t_num5 = count_5s(r[18])
        t_num6 = count_6s(r[19])
        t_num7 = count_7s(r[20])
        t_num8 = count_8s(r[21])#many_8s
        t_num9 = count_9s(r[22])
        
        v_point = []
        v_points = []
        
        v_point.append(vocation_pointer(t_num1))
        v_point.append(vocation_pointer(t_num2))
        v_point.append(vocation_pointer(t_num3))
        v_point.append(vocation_pointer(t_num4))
        v_point.append(vocation_pointer(t_num5))
        v_point.append(vocation_pointer(t_num6))
        v_point.append(vocation_pointer(t_num7))
        v_point.append(vocation_pointer(t_num8))
        v_point.append(vocation_pointer(t_num9))
        
        for v in v_point:
            if v != []:
                v_points.append(v[0])
        
        
        v_pointer = v_points
        
        
        return render_template('transit/fullreading.html',
                               exp=r[0],exp11=r[1],ln=r[2], lp=r[3],year_now=r[4],sU=r[5], sU1=r[6],
                               iM=r[7], iM1=r[8],Mrity=r[9],phy=r[10],men=r[11],emo=r[12],intt=r[13],one=r[14],two=r[15],
                               thr=r[16],fou=r[17],fiv=r[18],six=r[19],sev=r[20],eig=r[21],nin=r[22],
                               destiny=destiny,birthForce=birthForce,heart_desire=heart_desire,
                               personality=personality,reality=reality,one_in_plane=one_in_plane,sev_in_plane=sev_in_plane,
                               six_in_plane=six_in_plane,three_in_plane=three_in_plane,four_in_plane=four_in_plane,
                               eig_in_plane=eig_in_plane,nin_in_plane=nin_in_plane,five_in_plane=five_in_plane,
                               ones=ones,twos=twos,threes=threes,fours=fours,fives=fives,
                               sixs=sixs,sevens=sevens,eights=eights,nines=nines,vocation=vocation,
                               phy_num_to_str=phy_num_to_str,m_num_to_str=m_num_to_str,emo_num_to_str=emo_num_to_str,
                               i_num_to_str=i_num_to_str,t_num1=t_num1,t_num2=t_num2,t_num3=t_num3,t_num4=t_num4,t_num5=t_num5,
                               t_num6=t_num6,t_num7=t_num7,t_num8=t_num8,t_num9=t_num9,v_pointer=v_pointer,karmas=karmas)
    return 'ACCESS DENIED'


@bp.route('/newuser', methods=['GET', 'POST'])
@login_required
def newuser():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    
    if user.username == 'admin':
    
        form = PredictionForm()
        if form.validate_on_submit():
            
            FN = form.firstname.data
            MN = form.middlename.data
            LN = form.lastname.data
            dob = form.dob.data
            
            btd = dob[0:2] #1982
            btm = dob[3:5] #02
            bty = dob[6:10] #22
            
            r = generate_numbers(FN,MN,LN,btd,btm,bty)[2]
            
            def num_to_strs(g): #g=r[10]
                g = digit_sum(g)
                if g == 0:
                    return zero_in_plane
                elif g == 1:
                    return one_in_plane
                elif g == 2:
                    return two_in_plane
                elif g == 3:
                    return three_in_plane
                elif g == 4:
                    return four_in_plane
                elif g == 5:
                    return five_in_plane
                elif g == 6:
                    return six_in_plane
                elif g == 7:
                    return sev_in_plane
                elif g == 8:
                    return eig_in_plane
                elif g == 9:
                    return nin_in_plane
            
            phy_num_to_str = num_to_strs(r[10])
            m_num_to_str = num_to_strs(r[11])
            emo_num_to_str = num_to_strs(r[12])
            i_num_to_str = num_to_strs(r[13])
            
            t_num1 = count_1s(r[14])
            t_num2 = count_2s(r[15])
            t_num3 = count_3s(r[16])
            t_num4 = count_4s(r[17])
            t_num5 = count_5s(r[18])
            t_num6 = count_6s(r[19])
            t_num7 = count_7s(r[20])
            t_num8 = count_8s(r[21])#many_8s
            t_num9 = count_9s(r[22])
            
            v_point = []
            v_points = []
            
            v_point.append(vocation_pointer(t_num1))
            v_point.append(vocation_pointer(t_num2))
            v_point.append(vocation_pointer(t_num3))
            v_point.append(vocation_pointer(t_num4))
            v_point.append(vocation_pointer(t_num5))
            v_point.append(vocation_pointer(t_num6))
            v_point.append(vocation_pointer(t_num7))
            v_point.append(vocation_pointer(t_num8))
            v_point.append(vocation_pointer(t_num9))
            
            for v in v_point:
                if v != []:
                    v_points.append(v[0])
            
            v_pointer = v_points
            
            def what_lata(s):
                if s == 0:
                    return B_T_K
                elif s.lower() in ['a','j','s']:
                    return A_J_S
                elif s.lower() in ['c','l','u']:
                    return C_L_U
                elif s.lower() in ['d','m','v']:
                    return D_M_V
                elif s.lower() in ['g','p','y']:
                    return G_P_Y
                elif s.lower() in ['i','r']:
                    return I_R
                elif s.lower() in ['e','n','w']:
                    return E_N_W
                elif s.lower() in ['b','t','k']:
                    return B_T_K
                elif s.lower() in ['f','o','x']:
                    return F_O_X
                elif s.lower() in ['h','q','z']:
                    return H_Q_Z
                
            lata1 = what_lata(r[28])#w
            lata2 = what_lata(r[29])#0
            lata3 = what_lata(r[30])#O
            
            return render_template('transit/fullreading.html',
                               exp=r[0],exp11=r[1],ln=r[2], lp=r[3],year_now=r[4],sU=r[5], sU1=r[6],
                               iM=r[7], iM1=r[8],Mrity=r[9],phy=r[10],men=r[11],emo=r[12],intt=r[13],one=r[14],two=r[15],
                               thr=r[16],fou=r[17],fiv=r[18],six=r[19],sev=r[20],eig=r[21],nin=r[22],pina_change=r[23],
                               k_rity=r[24],Ess_karma=r[25],Essence=r[26],Ess_change=r[27],
                               cur_lata1=r[28],cur_lata2=r[29],cur_lata3=r[30],
                               destiny=destiny,birthForce=birthForce,heart_desire=heart_desire,
                               personality=personality,reality=reality,one_in_plane=one_in_plane,sev_in_plane=sev_in_plane,
                               six_in_plane=six_in_plane,three_in_plane=three_in_plane,four_in_plane=four_in_plane,
                               eig_in_plane=eig_in_plane,nin_in_plane=nin_in_plane,five_in_plane=five_in_plane,
                               ones=ones,twos=twos,threes=threes,fours=fours,fives=fives,
                               sixs=sixs,sevens=sevens,eights=eights,nines=nines,vocation=vocation,
                               phy_num_to_str=phy_num_to_str,m_num_to_str=m_num_to_str,emo_num_to_str=emo_num_to_str,
                               i_num_to_str=i_num_to_str,t_num1=t_num1,t_num2=t_num2,t_num3=t_num3,t_num4=t_num4,t_num5=t_num5,
                               t_num6=t_num6,t_num7=t_num7,t_num8=t_num8,t_num9=t_num9,v_pointer=v_pointer,karmas=karmas,
                              Ess=Ess,B_T_K=B_T_K,E_N_W=E_N_W,F_O_X=F_O_X,
                              lata1=lata1,lata2=lata2,lata3=lata3)
        
        elif request.method == 'GET':
            return render_template('newuser.html',form=form)
        
    return 'ACCESS DENIED'

@bp.route('/newuser/event', methods=['GET', 'POST'])
@login_required
def n_event():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    
    if user.username == 'admin':
    
        form = PredictionForm()
        if form.validate_on_submit():
            
            FN = form.firstname.data
            MN = form.middlename.data
            LN = form.lastname.data
            dob = form.dob.data
            
            btd = dob[0:2] #1982
            btm = dob[3:5] #02
            bty = dob[6:10] #22
            
            e = generate_numbers(FN,MN,LN,btd,btm,bty)[3]
    
            return render_template('event.html',exp11=e[0],sU=e[1],iM1=e[2],lp=e[3],Mrity=e[4],phy=e[5],men=e[6],
                                   emo=e[7],intt=e[8],one=e[9],two=e[10],thr=e[11],fou=e[12],fiv=e[13],six=e[14],
                                   sev=e[15],eig=e[16],nin=e[17],ps=e[18],cH=e[19],cH1=e[20],cH2=e[21],cH3=e[22],
                                   Essence=e[23],pynum=e[24],uniynum=e[25],pina=e[26],rc=e[27],pmonth=e[28],uniday=e[29],
                                   pday=e[30],Gpina=e[31],Gcha=e[32],Gper_pi=e[33],Gper_cha=e[34],k_day=e[35],k_pday=e[36],
                                   year_now=e[37])
        
        elif request.method == 'GET':
            return render_template('newuser.html',form=form)
        
    return 'ACCESS DENIED'