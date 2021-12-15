from __future__ import print_function, division
import datetime
from .utils.webscrapped_csv_file import cal_planet_points
from .utils.convert_time import time_to_sec,int_to_time,get_hour_or_min
from .utils.Moon_pos import planet_pos
from .utils.Planet_position import planet_pos as nat_planet_pos
from .moon_phase import sign_to_deg



def solar_arc(btd,btm,bty,tday,tmonth,tyear,geo, birth_time):
    
    daten = datetime.datetime(tyear,tmonth,tday)
    acd = datetime.datetime(tyear,2,13)
    acd_month = acd.strftime("%b")
    
    month = daten.strftime("%b")
    if daten >= acd:
        days_in_time = daten.year - bty #40
    else:
        days_in_time = (daten.year - bty) - 1 #39
    
    
    def prog_date(btd,btm,bty):
        
        birthdate = datetime.datetime.strptime(f"{btm}/{btd}/{bty}", "%m/%d/%Y")
        #progressed_date before
        progressed_date = birthdate + datetime.timedelta(days=days_in_time + 1)
        #print('progressed_date = ',progressed_date)
        
        #progressed_date after
        progressed_date_after = birthdate + datetime.timedelta(days=days_in_time)
        #print('progressed_date_after = ',progressed_date_after)
    
        #print('progressed_date = ',progressed_date)
        progressed_day = int(progressed_date.strftime("%d"))
        progressed_month = int(progressed_date.strftime("%m"))
        progressed_year = int(progressed_date.strftime("%Y"))
        
        progressed_day_after = int(progressed_date_after.strftime("%d"))
        progressed_month_after = int(progressed_date_after.strftime("%m"))
        progressed_year_after = int(progressed_date_after.strftime("%Y"))
        
        #print('progressed_day = ',progressed_day, progressed_month,progressed_year)
        #print('progressed_day_after = ',progressed_day_after, progressed_month_after,progressed_year_after)
        
        return progressed_day, progressed_month,progressed_year,progressed_day_after, progressed_month_after,progressed_year_after
    #print('prog_date = ',prog_date(btd,btm,bty)) #02 04 1982 01 04 1982
    
    prog_day, prog_m,prog_yr,prog_day_after, prog_m_after,prog_yr_after = prog_date(btd,btm,bty)
    
    #position of moon day after progressed date
    day_after_planets_pos = cal_planet_points(prog_day,prog_m-1,prog_yr,'natal')
    #print('day_after_planets_pos = ',day_after_planets_pos)
    
    #position of moon progressed date
    bday_planets_pos = cal_planet_points(prog_day_after,prog_m_after-1,prog_yr_after,'natal') 
    #print('positions = ',day_after_planets_pos[1],' and ',bday_planets_pos[1]) #(22, 4, 8) (8, 4, 8)
    
    '''Find the position of the progressed Sun.'''
    prog_sun = planet_pos(day_after_planets_pos[0],bday_planets_pos[0],month)
    
    nat_points = nat_planet_pos(btd,btm,bty,geo, birth_time)
    nat_sun = nat_points[0]
    
    #print(f'prog_sun = {prog_sun} and nat_sun = {nat_sun}')
    
    '''Subtract the natal Sun from this new progressed Sun position.'''
    #print(f'{nat_sun} - {prog_sun}')
    
    prog_sun_pt = sign_to_deg(prog_sun)
    nat_sun_pt = sign_to_deg(nat_sun)
    #print(f'prog_sun_pt = {prog_sun_pt} and nat_sun_pt = {nat_sun_pt}')
    
    '''-------------------------------------------prog_sun minute - nat_sun_minutes'''
    #solar_arc = (360 - (nat_sun_pt - prog_sun_pt),prog_sun[1] - nat_sun[1])
    arc_deg = 360 - (nat_sun_pt - prog_sun_pt)#,prog_sun[1] - nat_sun[1],0) #39,42
    arc_min = prog_sun[1] - nat_sun[1]
    #print('arc_deg = ',arc_deg)
    #print('arc_min = ',arc_min)
    
    arc_list = []
    
    for pt in nat_points:
        deg,min_,sign,name = pt
        
        #print('arc_deg = ',arc_deg)
        #print('arc_min = ',arc_min)
        add_mins = min_ + arc_min
        #print(f'arc_min = {arc_min} and min = {min_} and add_mins = {add_mins} => {name}')
        
        if add_mins <= 59:
            pt_min = add_mins
            extra = 0
        else:
            pt_min = add_mins - 60
            extra = 1
        #print(f'arc_min = {arc_min} and min = {min_} and add_mins = {add_mins} and pt_min = {pt_min} & extra = {extra} => {name}')   
            
        add_degs = deg + arc_deg + extra
        if add_degs <= 29:
            pt_deg = add_degs
            bpt_sign = sign
        else:
            bpt_deg = add_degs - 30
            bpt_sign = sign + 1
            if bpt_deg <= 29:
                pt_deg = bpt_deg
            else:
                pt_deg = bpt_deg - 30
                bpt_sign = sign + 2
        
        
        if bpt_sign <= 12:
            pt_sign = bpt_sign
        else:
            pt_sign = bpt_sign - 12
            
        #print(f'arc_deg = {get_hour_or_min(arc)[0]} and arc_min = {get_hour_or_min(arc)[1]}')
        
        
        planet_arc = (pt_deg, pt_min, pt_sign,name)
        ###
             
        arc_list.append(planet_arc)
            
    #print(f'solar_arc = {solar_arc}')
    
    return arc_list
    
#print(solar_arc(22,2,1982,13,12,2021,'07E','01,35'))

