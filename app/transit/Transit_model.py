from __future__ import print_function, division
from .tob import oppoAct,sqareAct,conj,sextile,trine,sesquaAct,semiquaAct,to_symbol,aspect_to_symbol
from .numOfDays import Num_of_days
from .webscrapping_extended import planet_points,month_year

def cal_transit_planet(btd,btm,bty,tmonth,tyear):
    nat_points = planet_points(btd, month_year(btm-1, bty),'natal')
    nat_points_name = (('sun'), ('moon'), ('merc'), ('ven'), ('mars'), ('jup'), ('sat'), ('ura'),
                       ('nep'), ('plu'), ('nod'), ('asc'), ('mc'),('vetx'))

    def loop_nat_points(n):
        planet = nat_points[n] #sun
        planet_name = nat_points_name[n] #sun
        planet_deg = planet[0]
        planet_sigh = planet[1]
        planet_min = planet[2]
        return planet_deg,planet_sigh,planet_min,planet_name

    transit_all = []
    transit_filter = []
    transit_starts = []
    transit_exact = []
    transit_ends = []
    transit_sextile = []
    transit_sextile_starts = []
    transit_trine = []
    transit_trine_starts = []

    def get_transit_planet(day, month_year,aspect,tipe):
        #print(day,month_year)
        transit_name = (('mars'), ('jup'), ('sat'), ('ura'),('nep'), ('plu'), ('nod'))
        transit = planet_points(day, month_year,'transit')
        #transit = ((26, 1, 4), (17, 10, 43), (25, 10, 21), (9, 2, 59), (19, 12, 8), (22, 10, 30), (23, 3, 56))
        #transit = ((25, 10, 21),(0,45,45))
        #transit_name = (('sat'),('not'))
        
        get_day = ((day - 1) * 94) + (2 * (day - 1)) #=answer 2208
        day = month_year[0][get_day:get_day + 2]
        date = month_year[0][get_day + 3:get_day + 5]
        
        def loop_transit_points(n):
            planet = transit[n] #(26, 1, 4)
            planet_name = transit_name[n] #mars
            planet_deg = planet[0]
            planet_sigh = planet[1]
            planet_min = planet[2]
            return planet_deg,planet_sigh,planet_min,planet_name
        
        n = 0
        while n != len(nat_points):
            #------------------------------ run --#loop_nat_points(n) #returns (3,12,2,'sun')
            planet_deg = loop_nat_points(n)[0]
            planet_sigh = loop_nat_points(n)[1]
            planet_min = loop_nat_points(n)[2] #
            exact_range = (planet_min,planet_min+1,planet_min+2,planet_min+3)
            #lets put range to the mins for exactness todo(38,39,40,41)
            planet_name = loop_nat_points(n)[3]
            
            d = 0
            while d != len(transit):
                #----------------- first code to run ----- transit_planet_deg too long we shotened it as ura...
                uraname =  loop_transit_points(d)[3]#mars
                uradeg = loop_transit_points(d)[0] #transit_planet_deg
                urasigh = loop_transit_points(d)[1] #transit_planet_sigh
                uramin = loop_transit_points(d)[2] #transit_planet_min
                #----------------- first code to run ends -----
                
                asp_deg = aspect(planet_deg,planet_sigh)[0]
                
                #upper sq
                if uradeg == asp_deg and uramin not in exact_range and urasigh == aspect(planet_deg,planet_sigh)[1]:
                    if f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact' not in transit_filter:
                        transit_filter.append(f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact')
                        
                        transit_starts.append([f'{day}/{date}/{month_year[1]}',
                                               f'{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}','view'])
                        
                #lower sq        
                elif uradeg == asp_deg and uramin not in exact_range and urasigh == aspect(planet_deg,planet_sigh)[2]:
                    if f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact' not in transit_filter:
                        transit_filter.append(f'{uraname} {aspect_to_symbol(tipe)} {planet_name} in deg but not exact')
                        
                        transit_starts.append([f'{day}/{date}/{month_year[1]}',
                                               f'{to_symbol(uraname)} {aspect_to_symbol(tipe)} {to_symbol(planet_name)}','view'])
                        
                d += 1
            n += 1
        #return (transit_all) #[int(uradeg),sigh_2_num(urasigh),int(uramin)]

    days = Num_of_days()
    b= tmonth
    while b <= tmonth:
        n=1 #day
        while n <= days.numberOfDays(tyear, b):
            
            #run code  ,,sextile,trine,sesquaAct,semiquaAct
            get_transit_planet(n, month_year(b, tyear),oppoAct,'opp') #sqareAct
            get_transit_planet(n, month_year(b, tyear),sqareAct,'square')
            get_transit_planet(n, month_year(b, tyear),conj,'conj')
            get_transit_planet(n, month_year(b, tyear),sesquaAct,'sesqua')
            get_transit_planet(n, month_year(b, tyear),semiquaAct,'semiqua')
            
            get_transit_planet(n, month_year(b, tyear),sextile,'setai')
            get_transit_planet(n, month_year(b, tyear),trine,'trin')
            
            n += 1
        b += 1
        
    return transit_starts #transit_all

#if __name__ == '__main__':
    
    #cal_transit_planet()
    