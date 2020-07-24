"""for midpont conversion to 360 addition"""
def sign_num(a, n):
    if n == 1:
        s = a
    if n == 2:
        s = a + 30
    if n == 3:
        s = a + 60
    if n == 4:
        s = a + 90
    if n == 5:
        s = a + 120
    if n == 6:
        s = a + 150
    if n == 7:
        s = a + 180
    if n == 8:
        s = a + 210
    if n == 9:
        s = a + 240
    if n == 10:
        s = a + 270
    if n == 11:
        s = a + 300
    if n == 12:
        s = a + 330
    return s

def mp_sign(n):
    if n in range(0, 30):
        g = n
        sign = 1
    elif n in range(29, 60):
        g = n - 30
        sign = 2       
    elif n in range(59, 90):
        g = n - 60
        sign = 3       
    elif n in range(89, 120):
        g = n - 90
        sign = 4        
    elif n in range(119, 150):
        g = n - 120
        sign = 5       
    elif n in range(149, 180):
        g = n - 150
        sign = 6       
    elif n in range(179, 210):
        g = n - 180
        sign = 7        
    elif n in range(209, 240):
        g = n - 210
        sign = 8       
    elif n in range(239, 270):
        g = n - 240
        sign = 9        
    elif n in range(269, 300):
        g = n - 270
        sign = 10        
    elif n in range(299, 330):
        g = n - 300
        sign = 11      
    elif n in range(329, 360):
        g = n - 330
        sign = 12         
    return g, sign