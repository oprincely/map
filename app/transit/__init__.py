from flask import Blueprint, redirect, render_template, request, url_for,session,escape
import os

from .webscrapping import call_write_eph_again
from .calculate_transit import * 
from .cal_optunity_waste import *
from .cal_tees import *
import datetime


x = datetime.datetime.now()
year_now = x.year

bp = Blueprint('transit', __name__)

@bp.route('/transit', methods=('GET', 'POST'))
def transit():
    if request.method == 'POST':
        btd = int(request.form['day'])
        btm = int(request.form['month'])
        bty = int(request.form['year'])
        
        #print(bty)
        
        transit_day = int(request.form['tday'])
        transit_month = int(request.form['tmonth'])
        transit_year = int(request.form['tyear'])
        
        asc1 = request.form['asc']
        asc11 = int(asc1[0:2])
        asc111 = int(asc1[3:4])
        asc = [asc11,asc111]
        
        mc1 = request.form['mc']
        mc11 = int(mc1[0:2])
        mc111 = int(mc1[3:4])
        mc = [mc11,mc111]
        
        pr1 = request.form['pr']
        pr11 = int(pr1[0:2])
        pr111 = int(pr1[3:4])
        prog_moon = [pr11,pr111]
        
    
    
        f = main(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon) #forces at work ... conj,squares and opp
        f1 = main_optunity_waste(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon) #opprutuitys and waste ...sextile and trine
        f2 =  main_cal_tees(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon)
        
        return render_template('transit/transit.html',f=f,f1=f1,f2=f2)
    return render_template('transit/transit.html')
    
@bp.route('/eph', methods=('GET', 'POST'))
def eph():
    if request.method == 'POST':
        year = int(request.form['year'])
        start_month = int(request.form['start'])
        call_write_eph_again(year,start_month)
        return 'done'
    return render_template('transit/eph.html')

