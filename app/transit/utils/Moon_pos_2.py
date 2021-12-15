#from GMT import gmt
from .convert_time import time_to_sec,int_to_time,get_hour_or_min

def planet_pos(day_after_planet_pt,birth_day_planet_pt,month):
    #day_after_planet_pt,birth_day_planet_pt = ((5, 58, 5, 'moon'),(22, 8, 4, 'moon'))
    day_after_deg,day_after_min = (day_after_planet_pt[0],day_after_planet_pt[1])
    
    #print(f'day_after_deg = {day_after_deg}, day_after_min = {day_after_min}')
    bday_deg,bday_min = (birth_day_planet_pt[0],birth_day_planet_pt[1])
    #print(f'bday_deg = {bday_deg}, bday_min = {bday_min}')
    
    #print(f'if {day_after_min} > {bday_min}')
    if day_after_min > bday_min:
        min_ = day_after_min - bday_min
        boro = 0
    else:
        min_ = (day_after_min + 60) - bday_min
        boro = 1
        
    if day_after_deg > bday_deg:
        deg_ = (day_after_deg - boro) - bday_deg
    else:
        deg_ = ((day_after_deg - boro) + 30) - bday_deg
        
    #print('deg, min = ',deg_,min_)
        
    monthly_rate = time_to_sec(deg_,min_,0)/12
    half_m = monthly_rate / 2
    
    
    new_bday_pt = time_to_sec(birth_day_planet_pt[0],birth_day_planet_pt[1],0)
    
    #print(f'new_bday_pt = {int_to_time(new_bday_pt)}')
    #prog_moon_month = (('Feb',new_bday_pt),('Mar',new_bday_pt + monthly_rate))
    
    prog_moon_month = {'Feb':new_bday_pt,
                       'Mar': new_bday_pt + monthly_rate,
                       'Apr': new_bday_pt + (monthly_rate * 2),
                       'May': new_bday_pt + (monthly_rate * 3),
                       'Jun': new_bday_pt + (monthly_rate * 4),
                       'Jul': new_bday_pt + (monthly_rate * 5),
                       'Aug': new_bday_pt + (monthly_rate * 6),
                       'Sep': new_bday_pt + (monthly_rate * 7),
                       'Oct': new_bday_pt + (monthly_rate * 8),
                       'Nov': new_bday_pt + (monthly_rate * 9),
                       'Dec': new_bday_pt + (monthly_rate * 10),
                       'Jan':new_bday_pt + (monthly_rate * 11)
                       }
    
    
    #print('feb = ',int_to_time(prog_moon_month[month]))
    correction = prog_moon_month[month] #+ time_to_sec(1,31,0) #=>1,17,0 astrodient correection
    
    correction_plus_half = prog_moon_month[month] + half_m
    #print('correction = ',int_to_time(correction))
    
    def create_pt(correction):
        #which sigh is the sun now
        thirty_deg = round(time_to_sec(30,0,0))
        #get the hour
        cal_deg = round(get_hour_or_min(correction)[0]) #19
        
        #get the min
        cal_min = round(get_hour_or_min(correction)[1]) #17
        
        
        if cal_deg <= 29:
            planet_position = [cal_deg, cal_min, birth_day_planet_pt[2],birth_day_planet_pt[3]] #[19, 17, 11]
        elif cal_deg > 29:
            
            sign = birth_day_planet_pt[2] + 1
            if sign < 12:
                new_sign = sign
            else:
                new_sign = sign - 12
                
            planet_position = [(cal_deg - 29), cal_min, new_sign,birth_day_planet_pt[3]]
        
        return planet_position
        
    planet_position_b4_13 = create_pt(correction)
    planet_position_plus_half = create_pt(correction_plus_half)
    
    #print('planet_position = ',(planet_position_b4_13,planet_position_plus_half))
    
    return planet_position_b4_13,planet_position_plus_half

#print(planet_pos([5, 58, 5,'moon'], [22, 8, 4, 'moon'],(12,2)))
#print(planet_pos([8, 8, 4,'moon'], [22, 8, 4, 'moon'],(2,12)))

#print(planet_pos([5, 58, 5,'moon'], [22, 8, 4, 'moon'],'Feb'))
#print(planet_pos((19, 39, 5, 'moon'), (5, 58, 5, 'moon'),(1,1))) #1/1/22 => [8, 5, 5, 'moon'] 4,22,5
#print(planet_pos([8, 8, 4,'moon'], [22, 8, 4, 'moon'],(0,0,1,35))) #(month,day,hour,min)
#(19, 39, 5, 'moon', (4, 3, 1982)) (5, 58, 5, 'moon', (3, 3, 1982))


