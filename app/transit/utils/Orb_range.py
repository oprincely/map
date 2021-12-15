from .convert_time import time_to_sec,int_to_time,get_hour_or_min

def orb_applying(orb, point): #(25,10,41)
    
    orb_applied = []
    #for point in points:
    planet_deg = get_hour_or_min(time_to_sec(point[0],point[1],0) - time_to_sec(0,orb,0))[0] #24
    planet_min = get_hour_or_min(time_to_sec(point[0],point[1],0) - time_to_sec(0,orb,0))[1] # 41
    
    if planet_deg >= 30:
        new_planet_deg = 30 - planet_deg
        sign = point[2] + 1
    else:
        new_planet_deg = planet_deg
        sign = point[2]
        
    if sign > 12:
        new_sign = 12 - sign
    else:
        new_sign = sign
    
    new_point = (new_planet_deg,planet_min,new_sign)
    
    #new_point = (planet_deg,point[1],planet_min)
    orb_applied.append(new_point)
        
    return orb_applied[0]

#aspect_list = (orb_applying(60, (6, 11, 40, 'merc')))

#print(aspect_list)

def orb_separating(orb, point): #(25,10,41)
    
    orb_applied = []
    #for point in points:
    planet_deg = get_hour_or_min(time_to_sec(point[0],point[1],0) + time_to_sec(0,orb,0))[0] #24
    planet_min = get_hour_or_min(time_to_sec(point[0],point[1],0) + time_to_sec(0,orb,0))[1] # 41
    
    if planet_deg >= 30:
        new_planet_deg = 30 - planet_deg
        sign = point[2] + 1
    else:
        new_planet_deg = planet_deg
        sign = point[2]
        
    if sign > 12:
        new_sign = 12 - sign
    else:
        new_sign = sign
    
    new_point = (new_planet_deg,planet_min,new_sign)
    
    #new_point = (planet_deg,point[1],planet_min)
    orb_applied.append(new_point)
        
    return orb_applied[0]



