#import pandas as pd
from __future__ import print_function, division
import requests
import datetime
import time
from bs4 import BeautifulSoup
import json
import textwrap

#from Allaspects import conj_or_opp

month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')

def create_eph(n,p):#0,1
    url = f'https://www.findyourfate.com/astrology/ephemeris/198{p}.html'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "lxml")

    astro_ele = soup.find_all('pre')

    texts = astro_ele[n].get_text()  #type = str

    def write_json(data, filename=f'./ephemeris/198{p}/eph_198{p}_{month_to_num[n]}.txt'): 
        with open(filename,'w') as f:
            json.dump(data, f)
            
    write_json(texts)
    

#create_eph(5) #0=jan,1=feb,2=march,3=apr,4=may,5=june,6=july,7=aug,8=sept,9=oct,10=nov,11=dec

def write_eph(p):   #n=0,p=1 
    n=0
    while n <= 11:
        create_eph(n,p)
        time.sleep(1)
        n += 1

def call_write_eph_again(p): #n=0, p=1
    p=p
    while p <= 10:
        write_eph(p)#0,1
        time.sleep(1)
        p += 1

#call_write_eph_again(0)
        
def month_year(month,year):
    month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')
    number = 98
    
    with open(f'./ephemeris/{year}/eph_{year}_{month_to_num[month]}.txt', 'r') as f:
        texts = f.readlines()
        raw_month = texts[0][number:]
        birth_calender = textwrap.fill(raw_month, 95)
            
    start_num = []
    start = 0
    end = 2
    while start <= 10 and end <= 20:
        if birth_calender[start:end] in ['Mo','Tu','We','Th','Fr','Sa','Su']:
            break
        else:
            start_num.append(1)
        start = start + 1
        end = end + 1
    general_number = sum(start_num) + number #munber that can access all month wtout error
    
    birth_calender = textwrap.fill(texts[0][general_number:], 95)
    
    return birth_calender,month_to_num[month],year

#birth_calender = month_year(2,2020) #month(month, year)[0]
#print(birth_calender)

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

def planet_pos(day_date, month,start_num):#start_num = 22
    get_day = ((day_date - 1) * 94) + (2 * (day_date - 1))
    
    #moon                        22                   24
    mdeg = month[0][get_day + start_num:get_day + start_num+2]
    msigh = month[0][get_day + start_num+2:get_day + start_num+4]
    mmin = month[0][get_day + start_num+4:get_day + start_num+6]
    
    return int(mdeg),sigh_2_num(msigh),int(mmin)
    
#planet_pos(31, month(2,1982),22) #moon=22

def planet_points(day_date, month,type_of_points):
    asc = (13,9,43)
    mc = (13,6,18)
    get_day = ((day_date - 1) * 94) + (2 * (day_date - 1)) #=answer 2208
    #day = month[0][get_day:get_day + 2]
    #date = month[0][get_day + 3:get_day + 5]
    
    #time = month[0][get_day + 6:get_day + 14]
    
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
    
    
    if type_of_points == 'natal':
        return ((int(sdeg),sigh_2_num(ssigh),int(smin)), (int(mdeg),sigh_2_num(msigh),int(mmin)),
                (int(merdeg),sigh_2_num(mersigh),int(mermin)),(int(vdeg),sigh_2_num(vsigh),int(vmin)),
                (int(marsdeg),sigh_2_num(marssigh),int(marsmin)),(int(jupdeg),sigh_2_num(jupsigh),int(jupmin)),
                (int(satdeg),sigh_2_num(satsigh),int(satmin)),(int(uradeg),sigh_2_num(urasigh),int(uramin)),
                (int(nepdeg),sigh_2_num(nepsigh),int(nepmin)),(int(pludeg),sigh_2_num(plusigh),int(plumin)),
                (int(noddeg),sigh_2_num(nodsigh),int(nodmin)),(asc[0],asc[1],asc[2]),(mc[0],mc[1],mc[2]))
    elif type_of_points == 'transit':
        return ((int(marsdeg),sigh_2_num(marssigh),int(marsmin)),(int(jupdeg),sigh_2_num(jupsigh),int(jupmin)),
                (int(satdeg),sigh_2_num(satsigh),int(satmin)),(int(uradeg),sigh_2_num(urasigh),int(uramin)),
                (int(nepdeg),sigh_2_num(nepsigh),int(nepmin)),(int(pludeg),sigh_2_num(plusigh),int(plumin)),
                (int(noddeg),sigh_2_num(nodsigh),int(nodmin)))
    elif type_of_points == 'prog':
        return ((int(sdeg),sigh_2_num(ssigh),int(smin)), (int(mdeg),sigh_2_num(msigh),int(mmin)),
                (int(merdeg),sigh_2_num(mersigh),int(mermin)),(int(vdeg),sigh_2_num(vsigh),int(vmin)),
                (int(marsdeg),sigh_2_num(marssigh),int(marsmin)),(int(jupdeg),sigh_2_num(jupsigh),int(jupmin)),
                (int(satdeg),sigh_2_num(satsigh),int(satmin)),(int(uradeg),sigh_2_num(urasigh),int(uramin)),
                (int(nepdeg),sigh_2_num(nepsigh),int(nepmin)),(int(pludeg),sigh_2_num(plusigh),int(plumin)),
                (int(noddeg),sigh_2_num(nodsigh),int(nodmin)))

#print(planet_points(22, month_year(1,1982),'natal'))
#print(planet_points(31, month_year(0,2020),'transit'))