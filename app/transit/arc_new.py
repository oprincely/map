from __future__ import print_function, division
import datetime
from .webscrapping_extended_new import planet_points
from .convert_time import time_to_int,int_to_time,get_hour_or_min
import time

def prog_date(btd,btm,bty,Year,tday,tmonth,tyear):
    cur_year = datetime.datetime.now().year
    if Year == '':
        days_in_time = cur_year - bty
    else:
        days_in_time = Year - bty
    
    birthdate = datetime.datetime.strptime(f"{btm}/{btd}/{bty}", "%m/%d/%Y")
    #progressed_date before
    progressed_date_after = birthdate + datetime.timedelta(days=days_in_time + 1)
    #progressed_date after
    progressed_date = birthdate + datetime.timedelta(days=days_in_time)

    #print(progressed_date)
    prog_day_after = int(progressed_date_after.strftime("%d"))
    prog_month_after = int(progressed_date_after.strftime("%m"))
    prog_year_after = int(progressed_date_after.strftime("%Y"))

    prog_day = int(progressed_date.strftime("%d"))
    prog_month = int(progressed_date.strftime("%m"))
    prog_year = int(progressed_date.strftime("%Y"))
    
    #print(prog_date()) #returns 02 04 1982 01 04 1982
    
    #Advanced calculated date ACD
    def acd(btd, btm, bty, Year,tday,tmonth,tyear):
        #position of sun day after birth
        
        day_after_planet_pos = planet_points(prog_day_after,prog_month_after - 1,prog_year_after,'natal')[0]

        #position of sun birthday
        bday_planet_pos = planet_points(prog_day,prog_month - 1,prog_year,'natal')[0]
        #print(day_after_moom_pos,bday_moon_pos) #(22, 4, 8) (8, 4, 8)
        
        prog_moon_pos = time_to_int(day_after_planet_pos[0], day_after_planet_pos[2], 0) - time_to_int(bday_planet_pos[0], bday_planet_pos[2], 0)
        prog_moon_move_monthly = prog_moon_pos/12 #monthly rate
        
        #moon position on May 01 is that of april 01 plus monthly rate so to get sept will keep adding result to rate
        Feb_21 = time_to_int(bday_planet_pos[0], bday_planet_pos[2], 0) + prog_moon_move_monthly
        Mar_21 = Feb_21 + prog_moon_move_monthly
        Apr_21 = Mar_21 + prog_moon_move_monthly
        May_21 = Apr_21 + prog_moon_move_monthly
        Jun_21 = May_21 + prog_moon_move_monthly
        Jul_21 = Jun_21 + prog_moon_move_monthly
        Aug_21 = Jul_21 + prog_moon_move_monthly
        Sep_21 = Aug_21 + prog_moon_move_monthly
        Oct_21 = Sep_21 + prog_moon_move_monthly
        Nov_21 = Oct_21 + prog_moon_move_monthly
        Dec_21 = Nov_21 + prog_moon_move_monthly
        Jan_21 = Dec_21 + prog_moon_move_monthly
        
        #cur_month = datetime.datetime.now().strftime("%b")
        cur_month = datetime.datetime(tyear, tmonth, tday).strftime("%b")
        #print('check_date = ',check_date)
        
        current_month = {'Jan':Jan_21,'Feb':Feb_21,'Mar':Mar_21,'Apr':Apr_21,'May':May_21,'Jun':Jun_21,
                         'Jul':Jul_21,'Aug':Aug_21,'Sep':Sep_21,'Oct':Oct_21,'Nov':Nov_21,'Dec':Dec_21}
        return current_month[cur_month]
    
    def cal_arc(btd, btm, bty, year,tday,tmonth,tyear):
        nat_pts = planet_points(btd,btm-1,bty,'natal')
        arc_list = []
        n=0
        while n != len(nat_pts):
            
            #current possition of prog sun - nat position
            prog_sun_dis = acd(btd, btm, bty, year,tday,tmonth,tyear) - time_to_int(nat_pts[0][0],nat_pts[0][2],0)
            arc_pos = prog_sun_dis + time_to_int(nat_pts[n][0],nat_pts[n][2],0)

            cal_deg = round(get_hour_or_min(arc_pos)[0]) #19
            #get the min
            cal_min = round(get_hour_or_min(arc_pos)[1]) #17

            if cal_deg <= 29:
                new_arc_sigh = nat_pts[n][1] + 1
                if new_arc_sigh <= 12:
                    planet_arc = (cal_deg, new_arc_sigh,cal_min,nat_pts[n][3])
                elif new_arc_sigh > 12:
                    planet_arc = (cal_deg, (new_arc_sigh - 12),cal_min,nat_pts[n][3])
            elif cal_deg > 29:
                new_arc_sigh = nat_pts[n][1] + 2
                if new_arc_sigh <= 12:
                    planet_arc = (cal_deg - 30, new_arc_sigh,cal_min,nat_pts[n][3])
                elif new_arc_sigh > 12:
                    planet_arc = (cal_deg - 30, (new_arc_sigh - 12),cal_min,nat_pts[n][3])
                
                
            arc_list.append(planet_arc)
            
            n += 1
        return arc_list
    return cal_arc(btd, btm, bty, Year,tday,tmonth,tyear)
   

#print(prog_date(nat_pts,btd,btm,bty,Year,tday,tmonth,tyear))
#print('arc = ',prog_date(22,2,1982,'',4,5,2021))