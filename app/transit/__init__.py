from flask import Blueprint, redirect, render_template, request, url_for,session,escape
from .Transit_model_new import cal_transit_planet
from .Transit_model_new_prog import prog_moon_to_pts



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
        Year = tyear
        
        mc_str = request.form['mc']
        mc = (int(mc_str[0:2]),int(mc_str[3:5]),int(mc_str[6:8]),'mc')
        
        asc_str = request.form['asc']
        asc = (int(asc_str[0:2]),int(asc_str[3:5]),int(asc_str[6:8]),'asc')
        
        prog_moon_str = request.form['pr']
        prog_moon = (int(prog_moon_str[0:2]),int(prog_moon_str[3:5]),int(prog_moon_str[6:8]),'moon')

        transit_to_natals = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,prog_moon,asc,mc,
                                               'natal','natal','transit')
        transit_to_mid_points = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,prog_moon,asc,mc,'mid_pts','mid_pt','transit')
        
        arc_to_natals = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,prog_moon,asc,mc,'natal','natal','arc')
        arc_to_mid_points = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,prog_moon,asc,mc,'mid_pts','mid_pt','arc')

        progresion_to_natals = prog_moon_to_pts(btd,btm,bty,Year,tday,tmonth,tyear,prog_moon,asc,mc,'natal','natal','prog')
        progresion_to_mid_points = prog_moon_to_pts(btd,btm,bty,Year,tday,tmonth,tyear,prog_moon,asc,mc,'mid_pts','mid_pt','prog')
        
        return render_template('transit/transit.html',transit_to_natals=transit_to_natals,
                               transit_to_mid_points=transit_to_mid_points,
                               arc_to_natals=arc_to_natals,
                               arc_to_mid_points=arc_to_mid_points,
                               progresion_to_natals=progresion_to_natals,
                               progresion_to_mid_points=progresion_to_mid_points)
        
        
    return render_template('transit/transit.html')