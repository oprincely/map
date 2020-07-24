#import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import json
import textwrap

month_to_num = ['jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec']

def create_eph(n,yr,p):#0,1
    url = f'https://www.findyourfate.com/astrology/ephemeris/{yr}{p}.html'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "lxml")

    astro_ele = soup.find_all('pre')

    texts = astro_ele[n].get_text()  #type = str

    def write_json(data, filename=f'./ephemeris/{yr}{p}/eph_{yr}{p}_{month_to_num[n]}.txt'): 
        with open(filename,'w') as f:
            json.dump(data, f)
            
    write_json(texts)
    

#create_eph(5) #0=jan,1=feb,2=march,3=apr,4=may,5=june,6=july,7=aug,8=sept,9=oct,10=nov,11=dec

def write_eph(yr,p):   #n=0,p=1 
    n=0
    while n <= 11:
        create_eph(n,yr,p)
        time.sleep(1)
        n += 1

def call_write_eph_again(yr,p): #n=0, p=1
    p=p
    while p <= 11:
        write_eph(yr,p)#0,1
        time.sleep(1)
        p += 1

#call_write_eph_again(201,0)

def before_month_call(number, month,year):
    def check_fest_lata(start,end):
            with open(f'./ephemeris/{year}/eph_{year}_{month}.txt', 'r') as f:
                texts = f.readlines()
                raw_month = texts[0][number:]
                birth_calender = textwrap.fill(raw_month, 95)
                
                first_two_words = birth_calender[start:end] #first_two_words
                return first_two_words
            
    start_num = []
    start = 0
    end = 2
    while start <= 10 and end <= 20:
        if check_fest_lata(start,end) in ['Mo','Tu','We','Th','Fr','Sa','Su']:
            break
        else:
            start_num.append(1)
        start = start + 1
        end = end + 1
    return sum(start_num) + number

def month(number, month,year):   
    with open(f'./ephemeris/{year}/eph_{year}_{month}.txt', 'r') as f:
        texts = f.readlines()
        raw_month = texts[0][number:] #all moth is 98 jan is 104 and sept  1988 takes 99
        birth_calender = textwrap.fill(raw_month, 95)
        #print(birth_calender)
        return birth_calender,year,month
    
#month(102, 'jan', 2019) #feb,mar,apr,may,june,july,aug,sept,oct,...nov,dec

def sigh_2_num(m):
    if m == 'AR':
        sn = 1
    elif m == 'TA':
        sn = 2
    elif m == 'GE':
        sn = 3
    elif m == 'CN':
        sn = 4
    elif m == 'LE':
        sn = 5
    elif m == 'VI':
        sn = 6
    elif m == 'LI':
        sn = 7
    elif m == 'SC':
        sn = 8
    elif m == 'SG':
        sn = 9
    elif m == 'CP':
        sn = 10
    elif m == 'AQ':
        sn = 11
    elif m == 'PI':
        sn = 12
    return sn

def month_2_num(m):
    if m == 'jan':
        sn = 1
    elif m == 'feb':
        sn = 2
    elif m == 'mar':
        sn = 3
    elif m == 'apr':
        sn = 4
    elif m == 'may':
        sn = 5
    elif m == 'june':
        sn = 6
    elif m == 'july':
        sn = 7
    elif m == 'aug':
        sn = 8
    elif m == 'sept':
        sn = 9
    elif m == 'oct':
        sn = 10
    elif m == 'nov':
        sn = 11
    elif m == 'dec':
        sn = 12
    return sn

def ephemeris_of_day(day_date, month): #date of the month[0]
    get_day = ((day_date - 1) * 94) + (2 * (day_date - 1)) #=answer 2208
    day = month[0][get_day:get_day + 2]
    date = month[0][get_day + 3:get_day + 5]
    
    time = month[0][get_day + 6:get_day + 14]
    
    #sun
    sdeg = month[0][get_day + 15:get_day + 17]
    ssigh = month[0][get_day + 17:get_day + 19]
    smin = month[0][get_day + 19:get_day + 21]
    
    #moon
    mdeg = month[0][get_day + 22:get_day + 24] #start=22, end=start+2, [start:end]
    msigh = month[0][get_day + 24:get_day + 26]
    mmin = month[0][get_day + 26:get_day + 28]
    #mercury
    merdeg = month[0][get_day + 29:get_day + 31]
    mersigh = month[0][get_day + 31:get_day + 33]
    mermin = month[0][get_day + 33:get_day + 35]
    #venus
    vdeg = month[0][get_day + 36:get_day + 38]
    vsigh = month[0][get_day + 38:get_day + 40]
    vmin = month[0][get_day + 40:get_day + 42]
    #mars
    marsdeg = month[0][get_day + 43:get_day + 45]
    marssigh = month[0][get_day + 45:get_day + 47]
    marsmin = month[0][get_day + 47:get_day + 49]
    #jup
    jupdeg = month[0][get_day + 50:get_day + 52]
    jupsigh = month[0][get_day + 52:get_day + 54]
    jupmin = month[0][get_day + 54:get_day + 56]
    #sat
    satdeg = month[0][get_day + 57:get_day + 59]
    satsigh = month[0][get_day + 59:get_day + 61]
    satmin = month[0][get_day + 61:get_day + 63]
    #ura
    uradeg = month[0][get_day + 64:get_day + 66]
    urasigh = month[0][get_day + 66:get_day + 68]
    uramin = month[0][get_day + 68:get_day + 70]
    #nep
    nepdeg = month[0][get_day + 71:get_day + 73]
    nepsigh = month[0][get_day + 73:get_day + 75]
    nepmin = month[0][get_day + 75:get_day + 77]
    #plu
    pludeg = month[0][get_day + 78:get_day + 80]
    plusigh = month[0][get_day + 80:get_day + 82]
    plumin = month[0][get_day + 82:get_day + 84]
    #nod
    noddeg = month[0][get_day + 85:get_day + 87]
    nodsigh = month[0][get_day + 87:get_day + 89]
    nodmin = month[0][get_day + 89:get_day + 91]
    
    return [[0,45], [0,45], [0,45], [0,45],[int(marsdeg),sigh_2_num(marssigh)],[int(jupdeg),sigh_2_num(jupsigh)],
            [int(satdeg),sigh_2_num(satsigh)],[int(uradeg),sigh_2_num(urasigh)],[int(nepdeg),sigh_2_num(nepsigh)],
            [int(pludeg),sigh_2_num(plusigh)],[int(noddeg),sigh_2_num(nodsigh)],[0,45], [0,45]]
    

#j = ephemeris_of_day(27, month(102, 'jan', 2019)) #other_month('apr',2020)#other_month(month,year)
#print('j = ',j)

def naspect(day_date, month,asc,mc):
    get_day = ((day_date - 1) * 94) + (2 * (day_date - 1)) #=answer 2208
    day = month[0][get_day:get_day + 2]
    date = month[0][get_day + 3:get_day + 5]
    
    time = month[0][get_day + 6:get_day + 14]
    
    #sun
    sdeg = month[0][get_day + 15:get_day + 17]
    ssigh = month[0][get_day + 17:get_day + 19]
    smin = month[0][get_day + 19:get_day + 21]
    
    #moon
    mdeg = month[0][get_day + 22:get_day + 24] #start=22, end=start+2, [start:end]
    msigh = month[0][get_day + 24:get_day + 26]
    mmin = month[0][get_day + 26:get_day + 28]
    
    #mercury
    merdeg = month[0][get_day + 29:get_day + 31]
    mersigh = month[0][get_day + 31:get_day + 33]
    mermin = month[0][get_day + 33:get_day + 35]
    #venus
    vdeg = month[0][get_day + 36:get_day + 38]
    vsigh = month[0][get_day + 38:get_day + 40]
    vmin = month[0][get_day + 40:get_day + 42]
    #mars
    marsdeg = month[0][get_day + 43:get_day + 45]
    marssigh = month[0][get_day + 45:get_day + 47]
    marsmin = month[0][get_day + 47:get_day + 49]
    #jup
    jupdeg = month[0][get_day + 50:get_day + 52]
    jupsigh = month[0][get_day + 52:get_day + 54]
    jupmin = month[0][get_day + 54:get_day + 56]
    #sat
    satdeg = month[0][get_day + 57:get_day + 59]
    satsigh = month[0][get_day + 59:get_day + 61]
    satmin = month[0][get_day + 61:get_day + 63]
    #ura
    uradeg = month[0][get_day + 64:get_day + 66]
    urasigh = month[0][get_day + 66:get_day + 68]
    uramin = month[0][get_day + 68:get_day + 70]
    #nep
    nepdeg = month[0][get_day + 71:get_day + 73]
    nepsigh = month[0][get_day + 73:get_day + 75]
    nepmin = month[0][get_day + 75:get_day + 77]
    #plu
    pludeg = month[0][get_day + 78:get_day + 80]
    plusigh = month[0][get_day + 80:get_day + 82]
    plumin = month[0][get_day + 82:get_day + 84]
    #nod
    noddeg = month[0][get_day + 85:get_day + 87]
    nodsigh = month[0][get_day + 87:get_day + 89]
    nodmin = month[0][get_day + 89:get_day + 91]
    
    return [[int(sdeg),sigh_2_num(ssigh)], [int(mdeg),sigh_2_num(msigh)],
            [int(merdeg),sigh_2_num(mersigh)],[int(vdeg),sigh_2_num(vsigh)],
            [int(marsdeg),sigh_2_num(marssigh)],[int(jupdeg),sigh_2_num(jupsigh)],
            [int(satdeg),sigh_2_num(satsigh)],[int(uradeg),sigh_2_num(urasigh)],
            [int(nepdeg),sigh_2_num(nepsigh)],[int(pludeg),sigh_2_num(plusigh)],
            [int(noddeg),sigh_2_num(nodsigh)],[asc[0],asc[1]],[mc[0],mc[1]]]


#k = naspect(22, month(98, 'feb',1982),[13,9],[13,6])
#print('k = ', k)

def list_for_solar_arc(day_date, month, asc, mc):
    get_day = ((day_date - 1) * 94) + (2 * (day_date - 1)) #=answer 2208
    day = month[0][get_day:get_day + 2]
    date = month[0][get_day + 3:get_day + 5]
    
    time = month[0][get_day + 6:get_day + 14]
    
    #sun
    sdeg = month[0][get_day + 15:get_day + 17]
    ssigh = month[0][get_day + 17:get_day + 19]
    smin = month[0][get_day + 19:get_day + 21]
    
    #moon
    mdeg = month[0][get_day + 22:get_day + 24] #start=22, end=start+2, [start:end]
    msigh = month[0][get_day + 24:get_day + 26]
    mmin = month[0][get_day + 26:get_day + 28]
    #mercury
    merdeg = month[0][get_day + 29:get_day + 31]
    mersigh = month[0][get_day + 31:get_day + 33]
    mermin = month[0][get_day + 33:get_day + 35]
    #venus
    vdeg = month[0][get_day + 36:get_day + 38]
    vsigh = month[0][get_day + 38:get_day + 40]
    vmin = month[0][get_day + 40:get_day + 42]
    #mars
    marsdeg = month[0][get_day + 43:get_day + 45]
    marssigh = month[0][get_day + 45:get_day + 47]
    marsmin = month[0][get_day + 47:get_day + 49]
    #jup
    jupdeg = month[0][get_day + 50:get_day + 52]
    jupsigh = month[0][get_day + 52:get_day + 54]
    jupmin = month[0][get_day + 54:get_day + 56]
    #sat
    satdeg = month[0][get_day + 57:get_day + 59]
    satsigh = month[0][get_day + 59:get_day + 61]
    satmin = month[0][get_day + 61:get_day + 63]
    #ura
    uradeg = month[0][get_day + 64:get_day + 66]
    urasigh = month[0][get_day + 66:get_day + 68]
    uramin = month[0][get_day + 68:get_day + 70]
    #nep
    nepdeg = month[0][get_day + 71:get_day + 73]
    nepsigh = month[0][get_day + 73:get_day + 75]
    nepmin = month[0][get_day + 75:get_day + 77]
    #plu
    pludeg = month[0][get_day + 78:get_day + 80]
    plusigh = month[0][get_day + 80:get_day + 82]
    plumin = month[0][get_day + 82:get_day + 84]
    #nod
    noddeg = month[0][get_day + 85:get_day + 87]
    nodsigh = month[0][get_day + 87:get_day + 89]
    nodmin = month[0][get_day + 89:get_day + 91]
    
    return [[int(sdeg),sigh_2_num(ssigh),int(smin)], [int(mdeg),sigh_2_num(msigh),int(mmin)],
            [int(merdeg),sigh_2_num(mersigh),int(mermin)],[int(vdeg),sigh_2_num(vsigh),int(vmin)],
            [int(marsdeg),sigh_2_num(marssigh),int(marsmin)],[int(jupdeg),sigh_2_num(jupsigh),int(jupmin)],
            [int(satdeg),sigh_2_num(satsigh),int(satmin)],[int(uradeg),sigh_2_num(urasigh),int(satmin)],
            [int(nepdeg),sigh_2_num(nepsigh),int(nepmin)],[int(pludeg),sigh_2_num(plusigh),int(nepmin)],
            [int(noddeg),sigh_2_num(nodsigh),int(nodmin)],[asc[0],asc[1]],[mc[0],mc[1]]]

def how_far_progressed(progressed_sun_deg, nat_planet_sigh): #the planet new place
    if progressed_sun_deg >= 60:
        has_prog_this_far = progressed_sun_deg - 60 #41-30=11
        new_planet_sigh = nat_planet_sigh + 2
        if new_planet_sigh == 13:
            arc_sigh = new_planet_sigh - 12
        else:
            arc_sigh = new_planet_sigh
    elif progressed_sun_deg <= 60:
        has_prog_this_far = progressed_sun_deg - 30 #41-30=11
        new_planet_sigh = nat_planet_sigh + 1
        if new_planet_sigh == 13:
            arc_sigh = new_planet_sigh - 12
        else:
            arc_sigh = new_planet_sigh
    arc_deg = has_prog_this_far
    return arc_deg, arc_sigh

def solar_arc(day_date, month,asc,mc, cyear): #solar_arc(22, month[0](98, 'feb', 1982),[13,9],[13,6], cyear) #(number, month[0],year)
    list_for_arced_nat_planets = []
    shot = list_for_solar_arc(day_date, month,asc,mc)
    
    n=0
    while n <= len(shot) - 1:
        #other planets
        nat_planet_deg = shot[n][0] #3
        nat_planet_sigh = shot[n][1] #12
        #print('nat_planet_sigh',nat_planet_sigh)
        #nat_planet_min = shot[n][2]
        
        #add age to sun deg
        age = cyear - month[1]
        #print(age)
        progressed_sun_deg = age + nat_planet_deg #45
        #print('progressed_sun_deg',progressed_sun_deg)
        how_far_progressed(progressed_sun_deg, nat_planet_sigh) #the planet new place
        arc = [how_far_progressed(progressed_sun_deg, nat_planet_sigh)[0],
               how_far_progressed(progressed_sun_deg, nat_planet_sigh)[1]]#, nat_planet_min]
        #print(how_far_progressed(progressed_sun_deg, nat_planet_deg, nat_planet_sigh))
        list_for_arced_nat_planets.append(arc)
        n += 1
            
    #print(progressed_sun_deg)
    return list_for_arced_nat_planets
    

#k = solar_arc(22, month(98, 'feb', 1982),[13,9],[13,6], 2019)
#print('k',k)
#j = list_for_solar_arc(22, month(98, 'feb', 1982),[13,9],[13,6])
#print('j',j)

#PROGRESSED MOON
def progressed_moon(day_date, month, cday, cmonth, cyear): #day_date,feb, year, month
    moon_return_age = 0
    
    birth_month = cmonth - month_2_num(month[2]) #2

    if birth_month <= cmonth: #2<=4
        age_in_year = cyear - month[1] #2020 - 1982 = 38yrs
        age_in_year_to_months = (age_in_year * 12) + (cmonth - month_2_num(month[2]))
    elif birth_month >= cmonth: #9>=4
        age_in_year = (cyear - month[1]) #2020 - 1982 = 38yrs
        age_in_year_to_months = (age_in_year * 12) - (cmonth - month_2_num(month[2]))
    #print(age_in_year_to_months * 0.91)
        
    #print('age_in_year_to_months',age_in_year_to_months)
    
    get_day = ((day_date - 1) * 94) + (2 * (day_date - 1))
    #moon
    mdeg = month[0][get_day + 22:get_day + 24] #start=22, end=start+2, [start:end]
    msigh = month[0][get_day + 24:get_day + 26]
    mmin = month[0][get_day + 26:get_day + 28]
    #print(mdeg,msigh,mmin)
    return [int(mdeg), sigh_2_num(msigh), int(mmin)]
    
'''    
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%m"))
'''
#g = progressed_moon(22, month(98, 'feb', 1982), 29, 4 , 2020)
#print('progressed moon = ',g)