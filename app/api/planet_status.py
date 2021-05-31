from flask import jsonify#,request
from app.transit.webscrapping_extended_new import planet_points
from .intercept_planet import intercept_planet_starts

#--------------------------- check exaltation, detriment, fall --------------------------
def cal_status(btd,btm,bty):
    natal = planet_points(btd, btm-1, bty,(13,9,18,'asc'),(13,6,41,'mc'),'status')
    #print(natal)
                
    check_status = [{"det":[11],"ext":[1],"fall":[7],"lord":[6]},
    {"det":[10],"ext":[2],"fall":[8],"lord":[4]},
    {"det":[9,12],"ext":[6],"fall":[12],"lord":[3,6]},
    {"det":[8,1],"ext":[12],"fall":[6],"lord":[2,7]},
    {"det":[7,2],"ext":[10],"fall":[4],"lord":[1,8]},
    {"det":[6,3],"ext":[4],"fall":[10],"lord":[12,9]},
    {"det":[4,6],"ext":[7],"fall":[1],"lord":[10,11]},
    {"det":[5],"ext":[8],"fall":[2],"lord":[11]},
    {"det":[6],"ext":[4],"fall":[11],"lord":[12]}]

    check_Interception = {"intercept":[4, 10]}

    status = {} #{'mars_det': 'det', 'sat_ext': 'ext'}

    n = 0
    while n != len(natal):
        for k, v in check_status[n].items():
            if natal[n][1] in v:
                status[f"{natal[n][3]}_{k}"] = k
                break
        #check for intercepting planet
        if natal[n][1] in check_Interception["intercept"] and natal[n][3] in ['sun','moon','merc','ven','mars']:
            status[f"{natal[n][3]}_int"] = ['int',intercept_planet_starts(btd,btm,bty)]
        elif natal[n][1] in check_Interception["intercept"] and natal[n][3] not in ['sun','moon','merc','ven','mars']:
            status[f"{natal[n][3]}_int"] = ['int',natal[n][3]]
        #else:
            #status[f"{natal[n][3]}_int"] = ['int',natal[n][3]]
        n+=1
        
    #--------------------------- check interception --------------------------

    '''When a planet is within an orb of 3 degrees of any of these points, it will be found to exercise a
    much stronger influence in the life than otherwise.'''

    cardinal_signs = {'sigh':[1,4,7,10],'deg':[0,1,2,3,4,10,11,12,13,14,15,16,23,24,25,26,27,28,29]} #['AR','CN','LI', 'CP']:[1,13,26]
    fixed_signs = {'sigh':[2, 5, 8, 11],'deg':[6,7,8,9,10,11,12,18,19,20,21,22,23,24]} #TU, LE, SC, AQ,:9,21
    common_signs = {'sigh':[3, 6, 9, 12],'deg': [1,2,3,4,5,6,7,14,15,16,17,18,19,20]} #GE, VI, SG, PI:4,17

    critical_deg = []

    def critical_degrees(planet_deg,planet_sigh,planet_name):
        if planet_sigh in cardinal_signs['sigh'] and planet_deg in cardinal_signs['deg']:
            return planet_name
        elif planet_sigh in common_signs['sigh'] and planet_deg in common_signs['deg']:
            return planet_name
        elif planet_sigh in fixed_signs['sigh'] and planet_deg in fixed_signs['deg']:
            return planet_name
        #print(f'{planet_name} is not in critical degrees')
            
    for a_planet in natal:
        deg = a_planet[0]
        sigh = a_planet[1]
        name = a_planet[3]
        
        if critical_degrees(deg,sigh,name) is not None:
            critical_deg.append(critical_degrees(deg,sigh,name))
        
    #print("critical_deg = ",critical_deg)
    return jsonify(status,critical_deg)

#print(cal_status(21,3,1985))
