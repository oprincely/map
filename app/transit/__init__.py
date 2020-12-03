from flask import Blueprint, redirect, render_template, request, url_for,session,escape
import os
from .Transit_model import cal_transit_planet
from .aspect_now import cal_aspects_now

from .webscrapping import call_write_eph_again
from .calculate_transit import * 
from .cal_optunity_waste import *
from .cal_tees import *
from .astro_transit_cal import *
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
        
        A = astro_cal_tees(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon)[0]
        A1 = astro_cal_tees(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon)[1]#square,conj,opp
    
        f = main(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon) #forces at work ... conj,squares and opp
        f1 = main_optunity_waste(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon) #opprutuitys and waste ...sextile and trine
        f2 =  main_cal_tees(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon)
        
        return render_template('transit/transit.html',f=f,f1=f1,f2=f2,A=A,A1=A1)
    return render_template('transit/transit.html')

################# Transit 2 ############
@bp.route('/transit2', methods=('GET', 'POST'))
def transit2():
    if request.method == 'POST':
        btd = int(request.form['day'])
        btm = int(request.form['month'])
        bty = int(request.form['year'])
        
        #print(bty)
        
        tday = int(request.form['tday'])
        tmonth = int(request.form['tmonth'])
        tyear = int(request.form['tyear'])
        Year = tyear
        
        #asc1 = request.form['asc']
        #asc11 = int(asc1[0:2])
        #asc111 = int(asc1[3:4])
        #asc = [asc11,asc111]
        
        #mc1 = request.form['mc']
        #mc11 = int(mc1[0:2])
        #mc111 = int(mc1[3:4])
        #mc = [mc11,mc111]
        
        #pr1 = request.form['pr']
        #pr11 = int(pr1[0:2])
        #pr111 = int(pr1[3:4])
        #prog_moon = [pr11,pr111]
        def next_(): #next_month_transit(tmonth, tyear)
            l = tmonth + 1
            if l < 12:
                m = l
                y = tyear
            else:
                m = 12 - l
                y = tyear + 1
            return m, y
         
        A = cal_transit_planet(btd,btm,bty,tmonth-1,tyear)
        B = cal_transit_planet(btd,btm,bty,tmonth,tyear)
        C = cal_transit_planet(btd,btm,bty,next_()[0],next_()[1])
        #A1 = astro_cal_tees(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon)[1]#square,conj,opp
    
        #f = main(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon) #forces at work ... conj,squares and opp
        #f1 = main_optunity_waste(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon) #opprutuitys and waste ...sextile and trine
        #f2 =  main_cal_tees(btd,btm,bty,transit_day,transit_month,transit_year,asc,mc,prog_moon)
        D = cal_aspects_now(btd,btm,bty,tday,tmonth,tyear,Year)
        
        return render_template('transit/transit2.html',A=A,B=B,C=C,D=D)
    return render_template('transit/transit2.html')

################# Transit 2 ends ############

@bp.route('/eph', methods=('GET', 'POST'))
def eph():
    if request.method == 'POST':
        year = int(request.form['year'])
        start_month = int(request.form['start'])
        call_write_eph_again(year,start_month)
        return 'done'
    return render_template('transit/eph.html')

