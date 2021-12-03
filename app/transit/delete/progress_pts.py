from __future__ import print_function, division
import datetime
from .webscrapping_extended_new_prog import planet_points
from .convert_time import time_to_int,int_to_time,get_hour_or_min
from .Moon_pos import planet_pos

#asc = [13,9]
#mc = [13,6]
#prog_moon = [15,4]
#date = '2021,11,28'
#daten = datetime.datetime(int(date[0:4]),int(date[5:7]),int(date[8:10]))

def calculate_prog_pts(btd,btm,bty,tday,tmonth,tyear):

    daten = datetime.datetime(tyear,tmonth,tday)
        
    days_in_time = daten.year - bty
    curr_month = daten.month
    curr_day = daten.day
        
    
    def prog_date(btd,btm,bty):
        
        birthdate = datetime.datetime.strptime(f"{btm}/{btd}/{bty}", "%m/%d/%Y")
        #progressed_date before
        progressed_date_after = birthdate + datetime.timedelta(days=days_in_time + 1)
        #progressed_date after
        progressed_date = birthdate + datetime.timedelta(days=days_in_time)
    
    
        #print(progressed_date)
        progressed_day_after = int(progressed_date_after.strftime("%d"))
        progressed_month_after = int(progressed_date_after.strftime("%m"))
        progressed_year_after = int(progressed_date_after.strftime("%Y"))

        progressed_day = int(progressed_date.strftime("%d"))
        progressed_month = int(progressed_date.strftime("%m"))
        progressed_year = int(progressed_date.strftime("%Y"))
        
        return progressed_day_after, progressed_month_after,progressed_year_after,progressed_day, progressed_month,progressed_year
    #returns 02 04 1982 01 04 1982

    #position of moon day after progressed date
    day_after_planets_pos = planet_points(prog_date(btd,btm,bty)[0],
                                          prog_date(btd,btm,bty)[1]-1,
                                          prog_date(btd,btm,bty)[2],
                                          'natal')
    
    #position of moon progressed date
    bday_planets_pos = planet_points(prog_date(btd,btm,bty)[3],prog_date(btd,btm,bty)[4]-1,prog_date(btd,btm,bty)[5],'natal') 
    #print(day_after_planets_pos,bday_planets_pos) #(22, 4, 8) (8, 4, 8)
    
    #take it to be corected planet_pos from Moon_pos
    return planet_pos(day_after_planets_pos[1],bday_planets_pos[1],(curr_month,curr_day))


#print(calculate_prog_pts(22,2,1982,''))