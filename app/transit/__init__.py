from flask import Blueprint, redirect, render_template, request, url_for,session,escape
from .Transit_engine import cal_transit_planet

from .prog_moon.prog_moon_engine import cal_prog_moon
import datetime



bp = Blueprint('transit', __name__)

@bp.route('/transit', methods=('GET', 'POST'))
def transit():
    if request.method == 'POST':
        btd = int(request.form['day'])
        btm = int(request.form['month'])
        bty = int(request.form['year'])
        
        tday = int(request.form['tday'])
        tmonth = int(request.form['tmonth'])
        tyear = int(request.form['tyear'])
        
        
        mc_str = request.form['mc']
        mc = (int(mc_str[0:2]),int(mc_str[3:5]),int(mc_str[6:8]),'mc')
        
        asc_str = request.form['asc']
        asc = (int(asc_str[0:2]),int(asc_str[3:5]),int(asc_str[6:8]),'asc')
        
        
        pr_m = request.form['pr']
        prog_moon = (int(pr_m[0:2]),int(pr_m[3:5]),int(pr_m[6:8]),'moon')
        
        geo_and_bt = request.form['bt']
        geo = geo_and_bt[0:3]
        birth_time = ':'.join((geo_and_bt[4:6],geo_and_bt[7:9]))


        transit_to_natals = cal_transit_planet(btd,btm,bty,geo,birth_time,tday,tmonth,tyear,asc,mc,'natal','natal','transit')
        transit_to_mid_points = ''#cal_transit_planet(btd,btm,bty,geo,birth_time,tday,tmonth,tyear,asc,mc,'mid_pts','mid_pt','transit')
        
        arc_to_natals = ''#cal_transit_planet(btd,btm,bty,geo,birth_time,tday,tmonth,tyear,asc,mc,'natal','natal','arc')
        arc_to_mid_points = ''#cal_transit_planet(btd,btm,bty,geo,birth_time,tday,tmonth,tyear,asc,mc,'mid_pts','mid_pt','arc')
        
        progresion_to_natals = cal_prog_moon(btd,btm,bty,geo,birth_time,tday,tmonth,tyear,prog_moon,asc,mc,'natal','natal','prog')
        progresion_to_mid_points = cal_prog_moon(btd,btm,bty,geo,birth_time,tday,tmonth,tyear,prog_moon,asc,mc,'mid_pts','mid_pt','prog')
        
        
        return render_template('transit/transit.html',transit_to_natals=transit_to_natals,
                               transit_to_mid_points=transit_to_mid_points,
                               arc_to_natals=arc_to_natals,
                               arc_to_mid_points=arc_to_mid_points,
                               progresion_to_natals=progresion_to_natals,
                               progresion_to_mid_points=progresion_to_mid_points
                               )
        
        
    return render_template('transit/transit.html')
    