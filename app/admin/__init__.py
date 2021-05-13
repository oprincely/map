from flask import Blueprint, flash,render_template, url_for, redirect, request, session
from flask_login import current_user,login_required
from .Check_admin_permit import check_admin
from .Relationship import relationships
import os
from app.models import User
from app import db
from app.auth.forms import RelationshipForm #PostForm,PredictionForm,NumberOfQuestions,AskQuestions

bp = Blueprint('admin', __name__)


@bp.route('/admin')
@login_required
@check_admin
def querydb():
    users = User.query.all()
    return render_template("admin.html", users=users,title='Querying DB')


@bp.route('/deleteuser')
@login_required
@check_admin
def delete_user():
    delete_name = 'jeff'
    users = User.query.all()
    for user in users:
        if user.username == delete_name:
            db.session.delete(user)
            db.session.commit()
    return render_template("admin.html", users=users,title='Querying DB')

@bp.route('/relationship', methods=['GET', 'POST'])
@login_required
@check_admin
def relation():
    form = RelationshipForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            #person 1
            FN = form.firstname.data
            MN = form.middlename.data
            LN = form.lastname.data
            dob = form.dob.data
            
            btd = dob[0:2] #1982
            btm = dob[3:5] #02
            bty = dob[6:10] #22
            #person 2
            FN1 = form.firstname1.data
            MN1 = form.middlename1.data
            LN1 = form.lastname1.data
            dob1 = form.dob1.data
            
            btd1 = dob1[0:2] #1982
            btm1 = dob1[3:5] #02
            bty1 = dob1[6:10] #22
            
            year_in_past = form.year.data
            
            #info = {FN,MN,LN,btd,btm,bty,FN1,MN1,LN1,btd1,btm1,bty1,year_in_past}
            
            data = relationships(FN,MN,LN,btd,btm,bty,FN1,MN1,LN1,btd1,btm1,bty1,year_in_past)
            #print(data)
            return render_template('relationship.html',data=data,form=form)
    elif request.method == 'GET':
        return render_template('relationship.html',form=form)
