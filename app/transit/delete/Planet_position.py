from .GMT import gmt
from .convert_time import time_to_sec,int_to_time,get_hour_or_min
from .webscrapped_csv_file import planet_points

def planet_pos(btd,btm,bty,geo, birth_time):
    
    #call GMT to get the interval
    interval = gmt(geo,birth_time)[0] #gmt(geo='07E',birth_time='01:35')
    
    
    #The Sun's longitude at noon on DAY AFTER BIRTH (as given in theephemeris): 10, 28 LOE
    #((4, 2, 12, 'sun'), (23, 27, 11, 'moon'))
    day_after_planets_pos = planet_points(btd + 1, btm-1, bty,'natal')
    #day_after_planet_pt = time_to_sec(day_after_planet_position[0], day_after_planet_position[1], 0)
    #print('day_after_planet_pt = ',day_after_planet_pt)
    
    #The Sun's longitude at noon BIRTH DAY: 9, 31, LOE
    #((3, 2, 12, 'sun'), (10, 45, 11, 'moon'))
    birth_day_planets_pos = planet_points(btd, btm-1, bty,'natal')
    #birth_day_planet_pt = time_to_sec(birth_day_planet_position[0], birth_day_planet_position[1], 0)
    #print('birth_day_planets_pos = ',birth_day_planets_pos)
    
    
    nat_pts = []
    
    n = 0
    while n <= len(birth_day_planets_pos) - 1:
        day_after_planet_pt = time_to_sec(day_after_planets_pos[n][0], day_after_planets_pos[n][1], 0)
        
        birth_day_planet_pt = time_to_sec(birth_day_planets_pos[n][0], birth_day_planets_pos[n][1], 0)
        
        #to remove negative value in calculation
        if day_after_planet_pt > birth_day_planet_pt:
            planet_motion = day_after_planet_pt - birth_day_planet_pt #time_to_int(14,44,0)#
        else:
            planet_motion = birth_day_planet_pt - day_after_planet_pt
           
        
        '''what is the interval from nearest noon to time of birth => 2H 15min'''
        #When the Sun moves 57 minutes=(sun_motion) of space in 24 hours, how much does it move in 2 hours and 15 minutes?
        planet_has_moved = (interval * planet_motion) / time_to_sec(24,0,0)
        #correction = birth_day_planet_pt + planet_has_moved
        
        corrections = (77.5,997.2,59.0,21.79,0,0,0,15.79,29.79,0,5447.625)
        
        if birth_day_planets_pos[n][3] == 'nod':
            correction = (birth_day_planet_pt + planet_has_moved) + corrections[n]
        else: 
            correction = (birth_day_planet_pt + planet_has_moved) - corrections[n]
            
            
        #print(f'correction for {birth_day_planets_pos[n][3]} = {birth_day_planet_pt + planet_has_moved}')
        
        #which sigh is the sun now
        thirty_deg = round(time_to_sec(30,0,0))
        #get the hour
        cal_deg = round(get_hour_or_min(correction)[0]) #19
        
        #get the min
        cal_min = round(get_hour_or_min(correction)[1]) #17
        
        
        if cal_deg <= 29:
            planet_position = (cal_deg, cal_min, birth_day_planets_pos[n][2],birth_day_planets_pos[n][3]) #[19, 17, 11]
        elif cal_deg > 29:
            planet_position = ((cal_deg - 29), cal_min, (birth_day_planets_pos[n][2] + 1),birth_day_planets_pos[n][3])
        
        
        nat_pts.append(planet_position)
        
        n += 1
        
    return nat_pts
    

#planet_pos(btd,btm,bty,geo, birth_time)
#print(planet_pos(22,2,1982,'07E', '01:35'))
