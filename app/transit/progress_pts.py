from __future__ import print_function, division
import datetime
from .webscrapping_extended_new import planet_points
from .convert_time import time_to_int,int_to_time,get_hour_or_min

#asc = [13,9]
#mc = [13,6]
#prog_moon = [15,4]
def calculate_prog_pts(btd,btm,bty,tday,tmonth,tyear,Year):
    def prog_date(btd,btm,bty):
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
        progressed_day_after = int(progressed_date_after.strftime("%d"))
        progressed_month_after = int(progressed_date_after.strftime("%m"))
        progressed_year_after = int(progressed_date_after.strftime("%Y"))

        progressed_day = int(progressed_date.strftime("%d"))
        progressed_month = int(progressed_date.strftime("%m"))
        progressed_year = int(progressed_date.strftime("%Y"))
        
        return progressed_day_after, progressed_month_after,progressed_year_after,progressed_day, progressed_month,progressed_year

    #print(prog_date()) #returns 02 04 1982 01 04 1982

    #position of moon day after birth
    day_after_planets_pos = planet_points(prog_date(btd,btm,bty)[0],prog_date(btd,btm,bty)[1]-1,prog_date(btd,btm,bty)[2],'natal')

    #position of moon birthday
    bday_planets_pos = planet_points(prog_date(btd,btm,bty)[3],prog_date(btd,btm,bty)[4]-1,prog_date(btd,btm,bty)[5],'natal') 
    #print(day_after_planets_pos,bday_planets_pos) #(22, 4, 8) (8, 4, 8)

    #start processing each
    def prog_planets(tday,tmonth,tyear):
        prog_list = []
        n = 0
        while n != len(bday_planets_pos):
            #run code
            day_after_planet = day_after_planets_pos[n]
            day_after_pos1 = day_after_planet[0]
            day_after_pos2 = day_after_planet[2]
            
            bday_planet = bday_planets_pos[n]
            bday_pos1 = bday_planet[0]
            bday_pos2 = bday_planet[2]
            bday_pos_sigh = bday_planet[1]
            
            prog_planet_pos = time_to_int(day_after_pos1, day_after_pos2, 0) - time_to_int(bday_pos1, bday_pos2, 0)
            prog_planet_move_monthly = prog_planet_pos/12 #monthly rate

            #moon position on May 01 is that of april 01 plus monthly rate so to get sept will keep adding result to rate
            Feb_21 = time_to_int(bday_pos1, bday_pos2, 0) + prog_planet_move_monthly
            Mar_21 = Feb_21 + prog_planet_move_monthly
            Apr_21 = Mar_21 + prog_planet_move_monthly
            May_21 = Apr_21 + prog_planet_move_monthly
            Jun_21 = May_21 + prog_planet_move_monthly
            Jul_21 = Jun_21 + prog_planet_move_monthly
            Aug_21 = Jul_21 + prog_planet_move_monthly
            Sep_21 = Aug_21 + prog_planet_move_monthly
            Oct_21 = Sep_21 + prog_planet_move_monthly
            Nov_21 = Oct_21 + prog_planet_move_monthly
            Dec_21 = Nov_21 + prog_planet_move_monthly
            Jan_21 = Dec_21 + prog_planet_move_monthly
            
            def what_month():
                #cur_month = datetime.datetime.now().strftime("%b")
                cur_month = datetime.datetime(tyear, tmonth, tday).strftime("%b")
                #print('check_date = ',cur_month)
                ###
                current_month = {'Jan':Jan_21,'Feb':Feb_21,'Mar':Mar_21,'Apr':Apr_21,'May':May_21,'Jun':Jun_21,
                         'Jul':Jul_21,'Aug':Aug_21,'Sep':Sep_21,'Oct':Oct_21,'Nov':Nov_21,'Dec':Dec_21}
                return current_month[cur_month]
                ###
            #print('month = ',get_hour_or_min(what_month())[0])
            
            prog_list.append((round(get_hour_or_min(what_month())[0]),bday_pos_sigh,round(get_hour_or_min(what_month())[1]),bday_planet[3]))
            
            n += 1
        return prog_list
    return prog_planets(tday,tmonth,tyear)