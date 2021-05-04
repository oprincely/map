from flask import Blueprint, redirect, render_template, request, url_for,session,escape
from .Transit_model_new import cal_transit_planet

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

        transit_to_natals = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,'natal','natal','transit')
        transit_to_mid_points = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,'mid_pts','mid_pt','transit')
        
        arc_to_natals = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,'natal','natal','arc')
        arc_to_mid_points = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,'mid_pts','mid_pt','arc')
        print(arc_to_natals)

        progresion_to_natals = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,'natal','natal','prog')
        progresion_to_mid_points = cal_transit_planet(btd,btm,bty,Year,tday,tmonth,tyear,'mid_pts','mid_pt','prog')
        
        return render_template('transit/transit.html',transit_to_natals=transit_to_natals,
                               transit_to_mid_points=transit_to_mid_points,
                               arc_to_natals=arc_to_natals,
                               arc_to_mid_points=arc_to_mid_points,
                               progresion_to_natals=progresion_to_natals,
                               progresion_to_mid_points=progresion_to_mid_points)
    return render_template('transit/transit.html')