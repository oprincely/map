from __future__ import print_function, division
import datetime
from .webscrapping_extended_new_prog import planet_points
from .convert_time import time_to_int,int_to_time,get_hour_or_min
from .Moon_pos_2 import planet_pos



def calculate_prog_pts(btd,btm,bty,tday,tmonth,tyear):
    
    daten = datetime.datetime(tyear,tmonth,tday)
    acd = datetime.datetime(tyear,2,1)
    acd_month = acd.strftime("%b")
    
    month = daten.strftime("%b")
    if daten >= acd:
        days_in_time = daten.year - bty #40
    else:
        days_in_time = (daten.year - bty) - 1 #39
        
        
    #curr_month = daten.month
    #curr_day = daten.day
    
    
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
    
    
    #position of moon day after progressed date
    day_after_planets_pos = planet_points(prog_date(btd,btm,bty)[0],
                                          prog_date(btd,btm,bty)[1]-1,
                                          prog_date(btd,btm,bty)[2],
                                          'natal')
    #print('day_after_planets_pos = ',day_after_planets_pos)
    #position of moon progressed date
    bday_planets_pos = planet_points(prog_date(btd,btm,bty)[3],prog_date(btd,btm,bty)[4]-1,prog_date(btd,btm,bty)[5],'natal') 
    #print('positions = ',day_after_planets_pos[1],' and ',bday_planets_pos[1]) #(22, 4, 8) (8, 4, 8)
    
    #take it to be corected planet_pos from Moon_pos
    #print(curr_month,curr_day)
    #print()
    return planet_pos(day_after_planets_pos[1],bday_planets_pos[1],month)
    
#print(calculate_prog_pts(22,2,1982,13,1,2022))
#print(calculate_prog_pts(22,2,1982,13,2,2022))
#print(calculate_prog_pts(22,2,1982,13,3,2022))

