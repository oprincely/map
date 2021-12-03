#from GMT import gmt
from .convert_time import time_to_sec,int_to_time,get_hour_or_min

def planet_pos(day_after_planet_position, birth_day_planet_position,month_day):
    
    #convert the day to minus
    day = month_day[1] * 4  + (int(month_day[2]) * 15) + (int(month_day[3]) / 4)
    
    month = month_day[0]
    
    #The Sun's longitude at noon on DAY AFTER BIRTH (as given in theephemeris): 10, 28 LOE
    day_after_planet_pt = time_to_sec(day_after_planet_position[0], day_after_planet_position[1], 0)
    
    #The Sun's longitude at noon BIRTH DAY: 9, 31, LOE
    birth_day_planet_pt = time_to_sec(birth_day_planet_position[0], birth_day_planet_position[1], 0)
    
    #to remove negative value in calculation
    if day_after_planet_pt > birth_day_planet_pt:
        planet_motion = day_after_planet_pt - birth_day_planet_pt #time_to_int(14,44,0)#
    else:
        planet_motion = birth_day_planet_pt - day_after_planet_pt
       
    #print('planet_motion = ',int_to_time(planet_motion))
    
    #for corrected birth time we call our GMT i.e corrected and converted birth time i.e 01.35 nigeria is -1 to GMT
    #birth_time = gmt(geo='07E',birth_time='01:35') #8:7:0 pm
    #print('birth_time = ',int_to_time(birth_time[0]))
    
    
    """#which ephemeris noon is nearer to birth_time
    ephe = [13,14,15,16,17,18,19,20,21,22,23,0,1,2,3,4,5,6,7,8,9,10,11,12]
    birth_day_noon = time_to_sec(0,35,0) - time_to_sec(10,6,18)#10,6,18
    day_after_birth_noon = time_to_sec(0,35,0) + time_to_sec(10,10,15) #10,10,15
    
    print('birth_day_noon = ',int_to_time(birth_day_noon))
    print('day_after_birth_noon = ',int_to_time(day_after_birth_noon))
    """
    
    '''what is the interval from nearest noon to time of birth => 2H 15min'''
    #When the Sun moves 57 minutes=(sun_motion) of space in 24 hours, how much does it move in 2 hours and 15 minutes?
    planet_has_moved = (time_to_sec(month,day,0) * planet_motion) / time_to_sec(24,0,0) #2.15*57min/24hrs
    correction = birth_day_planet_pt + planet_has_moved + time_to_sec(1,31,0) #=>1,17,0 astrodient correection
    
    '''print('correction = ',correction)
    print('value = ',int_to_time(time_to_sec(3,16,0) - correction))
    print('correction = ',correction - time_to_sec(3,16,0))
    print('value = ',int_to_time(correction - time_to_sec(3,16,0)))'''
    
    
    #which sigh is the sun now
    thirty_deg = round(time_to_sec(30,0,0))
    #get the hour
    cal_deg = round(get_hour_or_min(correction)[0]) #19
    
    #get the min
    cal_min = round(get_hour_or_min(correction)[1]) #17
    
    
    if cal_deg <= 29:
        planet_position = [cal_deg, cal_min, birth_day_planet_position[2],birth_day_planet_position[3]] #[19, 17, 11]
    elif cal_deg > 29:
        
        sign = birth_day_planet_position[2] + 1
        if sign < 12:
            new_sign = sign
        else:
            new_sign = sign - 12
            
        planet_position = [(cal_deg - 29), cal_min, new_sign,birth_day_planet_position[3]]
    
    #print('planet_position = ',planet_position)
    
    return planet_position

#print(planet_pos([5, 58, 5,'moon'], [22, 8, 4, 'moon'],(12,2)))
#print(planet_pos([8, 8, 4,'moon'], [22, 8, 4, 'moon'],(2,12)))


