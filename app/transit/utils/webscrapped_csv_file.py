from __future__ import print_function, division
import requests
from bs4 import BeautifulSoup
import os
import csv
from .ephemeris_engine import create_ephemeris

#from Allaspects import conj_or_opp
month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')

def sigh_2_num(m):
    sigh_dict = {'AR':1,'TA':2,'GE':3,'CN':4,'LE':5,'VI':6,'LI':7,'SC':8,'SG':9,'CP':10,'AQ':11,'PI':12}
    return sigh_dict[m]

def cal_planet_points(day, month, yr, type_of_points): #planet_points(day, month, year)
    
    def plt_pos(position):
        name = ('sun','moon','merc','ven','mars','jup','sat','ura','nep','plu','nod','asc','mc')
        date = int(row[1])
        
        sdeg = int(row[position][0:2])
        #print("sdeg = ",sdeg)
        ssigh = sigh_2_num(row[position][2:4])
        smin = int(row[position][4:6])
        
        return sdeg,smin,ssigh,name[position - 3]
    
    #Open csv
    with open(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.csv') as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            
            #Get the natal points
            if type_of_points == 'natal':
                #to convert 1 to 01 str(1).zfill(2)
                if row != [] and f'{str(day).zfill(2)}' in row:
                    return (plt_pos(3),plt_pos(4),plt_pos(5),plt_pos(6),plt_pos(7),plt_pos(8),plt_pos(9),plt_pos(10),
                               plt_pos(11),plt_pos(12),plt_pos(13))
                
            
        
def planet_points(day, month, yr, type_of_points):
    try:
        return cal_planet_points(day, month, yr, type_of_points)
    except FileNotFoundError as e: #except Exception:
        create_ephemeris(yr)
        return cal_planet_points(day, month, yr, type_of_points)

#print(planet_points(22, 1, 2021, "natal"))