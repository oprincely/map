from __future__ import print_function, division
import requests
from bs4 import BeautifulSoup
import os
import csv
from .ephemeris_engine import create_ephemeris

#from Allaspects import conj_or_opp
month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')

def convert_to_csv(month, yr):
    try:
        #Convert to csv
        astro_elements_csv = []
        with open(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.txt', "r") as file: #ephemeris/1983/1983_feb.txt
            lines = file.readlines()
            for line in lines:
                if 'DATE' not in line and line != '\n':
                    word_list = line.strip().split()
                    astro_elements_csv.append(word_list)
                    
        with open(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.csv',"w") as astro_elements_to_csv:
            writer = csv.writer(astro_elements_to_csv)
            #writer.writerow(['DATE','SID.TIME','SUN','MOON','MERCURY','VENUS','MARS','JUPITER','SATURN','URANUS','NEPTUNE','PLUTO','NODE'])
            writer.writerows(astro_elements_csv)
            
        """Delete the text file"""
        os.remove(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.txt')
    except Exception:
        create_ephemeris(yr)
        convert_to_csv(month, yr)

def sigh_2_num(m):
    sigh_dict = {'AR':1,'TA':2,'GE':3,'CN':4,'LE':5,'VI':6,'LI':7,'SC':8,'SG':9,'CP':10,'AQ':11,'PI':12}
    return sigh_dict[m]

def cal_planet_points(day, month, yr, asc, mc, type_of_points): #planet_points(day, month, year)
    t_list = []
    def plt_pos(position):
        name = ('sun','moon','merc','ven','mars','jup','sat','ura','nep','plu','nod','asc','mc')
        date = int(row[1])
        
        sdeg = int(row[position][0:2])
        #print("sdeg = ",sdeg)
        ssigh = sigh_2_num(row[position][2:4])
        smin = int(row[position][4:6])
        
        return sdeg,ssigh,smin,name[position - 3],date
    
    #Open csv
    with open(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.csv') as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            #Get the natal points
            if type_of_points == 'natal':
                #to convert 1 to 01 str(1).zfill(2)
                if row != [] and f'{str(day).zfill(2)}' in row:
                    return (plt_pos(3),plt_pos(4),plt_pos(5),plt_pos(6),plt_pos(7),plt_pos(8),plt_pos(9),plt_pos(10),
                               plt_pos(11),plt_pos(12),plt_pos(13),(asc[0],asc[1],asc[2],asc[3]),(mc[0],mc[1],mc[2],mc[3]))
                    
                    #to get the transit for one dayin question uncomment and remove #Get the transit points
                    #transit = (plt_pos(7),plt_pos(8),plt_pos(9),plt_pos(10),plt_pos(11),plt_pos(12),plt_pos(13))
                
            #Get the transit points
            elif type_of_points == 'transit':
                if row != []: #Get the transit of the whole month
                #if row != [] and f'{str(day).zfill(2)}' in row: #just get the transit of the exact day
                    t_list.append((plt_pos(7),plt_pos(8),plt_pos(9),plt_pos(10),plt_pos(11),plt_pos(12),plt_pos(13)))
            
            #Get the planet status
            elif type_of_points == 'status':
                if row != [] and f'{str(day).zfill(2)}' in row:
                    return (plt_pos(3),plt_pos(4),plt_pos(5),plt_pos(6),plt_pos(7),plt_pos(8),plt_pos(9),plt_pos(10),plt_pos(11))
             
    return t_list
        
def planet_points(day, month, yr, asc, mc, type_of_points):
    try:
        return cal_planet_points(day, month, yr, asc, mc, type_of_points)
    except FileNotFoundError: #except Exception:
        create_ephemeris(yr)
        return cal_planet_points(day, month, yr, asc, mc, type_of_points)

#print(planet_points(22, 2, 1982,[16,9,15],[16,6,48], "natal"))