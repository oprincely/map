"""for midpont conversion to 360 addition"""
def sign_num(sdeg,ssign):#(a, n):
    if ssign == 1:
        sign = sdeg
    elif ssign == 2:
        sign = sdeg + 30
    elif ssign == 3:
        sign = sdeg + 60
    elif ssign == 4:
        sign = sdeg + 90
    elif ssign == 5:
        sign = sdeg + 120
    elif ssign == 6:
        sign = sdeg + 150
    elif ssign == 7:
        sign = sdeg + 180
    elif ssign == 8:
        sign = sdeg + 210
    elif ssign == 9:
        sign = sdeg + 240
    elif ssign == 10:
        sign = sdeg + 270
    elif ssign == 11:
        sign = sdeg + 300
    elif ssign == 12:
        sign = sdeg + 330 #12+330 = 342
    return sign

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