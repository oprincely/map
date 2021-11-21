from __future__ import print_function, division
import requests
from bs4 import BeautifulSoup
import os
import csv

month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')

def create_ephemeris(yr):
    """Downloads the ephemeris and process the file and save it as csv"""
    
    #saving the file so if the directory is not we creat it
    if not os.path.exists(f'./ephemeris/{yr}'):
        os.mkdir(f'./ephemeris/{yr}')
    
    #URL
    #print('Calling URL ...')
    url = f'https://www.findyourfate.com/astrology/ephemeris/{yr}.html'
    
    #using beautiful soup
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")
        astro_ele = soup.find_all('pre')
        
        ele_list = []
        for ele in astro_ele:
            #we extract each element to a list, but years 2021 first element contains all the elem and 1982 is normal
            ele_list.append(ele.get_text())
        
        n = 0
        while n != len(month_to_num):
            with open(f'./ephemeris/{yr}/{yr}_{month_to_num[n]}.txt', "w") as file:
                file.write(ele_list[n])
                n += 1
        
        '''n = 0
        while n != len(month_to_num):
            convert_to_csv(n, yr)
            n += 1'''
        #print('done')
    except Exception as e:
        print("Connection failed due to {}".format(e))