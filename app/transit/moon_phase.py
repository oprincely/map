def sign_to_deg(pt): #stoped change3 t0 (3, 3, 12, 'sun')
    sign_to_angle = {1:0,2:30,3:60,4:90,5:120,6:150,7:180,8:210,9:240,10:270,11:300,12:330}
    return sign_to_angle[pt[2]] + pt[0]


def prog_moon_phase(prog_sun,prog_moon):
    
    def ck360(num):
        return num - 360 if num > 360 else num
    
    start = sign_to_deg(prog_sun)
    
    prog_moon_pt = sign_to_deg(prog_moon)
    
    
    if start < 12:
        beging = 360 + (start - 12)
    else:
        beging = start - 12
    
    
    phase_range = ((ck360(beging), ck360(start + 34),'new_moon'),
                   (ck360(start + 33), ck360(start + 89),'crescent'),
                   (ck360(start + 88), ck360(start + 124),'1st_quarter'),
                   (ck360(start + 123), ck360(start + 179),'gibbous'),
                   (ck360(start + 178), ck360(start + 215),'full'),
                   (ck360(start + 214), ck360(start + 260),'disseminating'),
                   (ck360(start + 259), ck360(start + 305),'3rd_quarter'),
                   (ck360(start + 304), ck360(start + 350),'balsamic')
                   )
    
    for start_range,end_range,phase in phase_range:
        if prog_moon_pt in range(start_range,end_range):
            return phase
        elif 360 - prog_moon_pt in range(start_range,end_range):
            return phase
        
#print('NK = ',prog_moon_phase((4,3),(5,12))) #88 behind
#print('IBE = ',prog_moon_phase((12,5),(10,12)))
#print('D = ',prog_moon_phase((3,3),(12,1))) #48 behind balis
#print('Odbo = ',prog_moon_phase((13,9),(19,11))) 
#print('P = ',prog_moon_phase((12,1),(3,5))) #111 ahead
#print('P nat = ',prog_moon_phase((3, 3, 12, 'sun'),(11, 3, 11, 'moon'))) #111 ahead