"""for midpont conversion to 360 addition"""
def sign_num(sdeg,ssign):#(a, n):
    sign_to_angle = {1:0,2:30,3:60,4:90,5:120,6:150,7:180,8:210,9:240,10:270,11:300,12:330}
    return sign_to_angle[ssign] + sdeg

def mp_sign(n,planet_min,first_planets_name,second_planets_name): #sign_num(sdeg,ssign) + sign_num(mdeg,msign)=> 342 + 400 =652/2 = 326
    if n in range(0, 30):
        midpt_deg = n
        sign = 1
    elif n in range(29, 60):
        midpt_deg = n - 30
        sign = 2       
    elif n in range(59, 90):
        midpt_deg = n - 60
        sign = 3       
    elif n in range(89, 120):
        midpt_deg = n - 90
        sign = 4        
    elif n in range(119, 150):
        midpt_deg = n - 120
        sign = 5       
    elif n in range(149, 180):
        midpt_deg = n - 150
        sign = 6       
    elif n in range(179, 210):
        midpt_deg = n - 180
        sign = 7        
    elif n in range(209, 240):
        midpt_deg = n - 210
        sign = 8       
    elif n in range(239, 270):
        midpt_deg = n - 240
        sign = 9        
    elif n in range(269, 300):
        midpt_deg = n - 270
        sign = 10        
    elif n in range(299, 330): #326
        midpt_deg = n - 300
        sign = 11      
    elif n in range(329, 360):
        midpt_deg = n - 330
        sign = 12         
    return midpt_deg,planet_min,sign, first_planets_name,second_planets_name