from .tob import to_symbol
from .midptmodel import sign_num,mp_sign
#from webscrapping_extended import planet_points,month_year

btd = 22
btm = 2
bty = 1982

#transit_day = 1
#transit_month = 9
#transit_year = 2020

#asc = (13,9,43)
#mc = (13,6,18)
#prog_moon = [15,4]

natName = (('sun'), ('moon'), ('merc'), ('ven'), ('mars'), ('jup'), ('sat'), ('ura'),
                   ('nep'), ('plu'), ('nod'), ('asc'), ('mc'))
                   
#natPts = planet_points(day, month_year,'nat')
natPts = ((3, 12, 2), (10, 11, 45), (6, 11, 39), (25, 10, 41), (19, 7, 10), (10, 8, 19), (21, 7, 50), (4, 9, 31),
 (26, 9, 42), (26, 7, 46), (20, 4, 26), (13, 9, 43), (13, 6, 18),(16, 12, 6))

class MidPts(object):
    def calculate_midpts(self):
        planet_midpt = []
        s = []
        symbol = []
        
        def mid_pts(planet1,planet2,name_of_planet1,name_of_planet2):
            sdeg = planet1[0]
            sname = name_of_planet1#name of midpt eg sun
            ssign = planet1[1]
            mdeg = planet2[0]
            mname = name_of_planet2#name of midpt eg moon
            msign = planet2[1]
            sun_moon_midpt = mp_sign(int(round((sign_num(sdeg,ssign) + sign_num(mdeg,msign))/2,0)))
            g = f'{sname}/{mname}'
            s1 = to_symbol(sname)
            s2 = to_symbol(mname)
            l = f'{s1}/{s2}'
            #print(sun_moon_midpt)
            planet_midpt.append(mp_sign(int(round((sign_num(sdeg,ssign) + sign_num(mdeg,msign))/2,0))))
            s.append(g)
            symbol.append(l)
            
        def call_midpts(w,w1,w2,w3): 
            n,n1,n2,n3 = w,w1,w2,w3
            while n3 != len(natName) and n1 != len(natPts):
                mid_pts(natPts[n],natPts[n1],natName[n2],natName[n3])
                n1,n3 = n1 + 1,n3 + 1
                
        def increment(g):#1
            n = g
            n2 = n
            n1 = n + 1
            n3 = n1
            return n,n1,n2,n3
        
        def calculate():
            va = 0
            while va != len(natPts):
                call_midpts(increment(va)[0], increment(va)[1], increment(va)[2], increment(va)[3])
                va = va + 1
        calculate()
        return planet_midpt,s,symbol
obj = MidPts()
#print(obj.calculate_midpts()[0])
#print()
#print(obj.calculate_midpts()[1]) 
