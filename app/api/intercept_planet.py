import csv
from app.transit.webscrapping_extended_new import convert_to_csv
from datetime import date

def intercept_planet_starts(day,month,yr,planet_position):
    '''if there is a planet in interception that is in cap or can, when will it progress out'''
    def plt_pos(position):
        '''because of webscrapping_extended_new, we need planet position sun=3 moon=4...'''
        
        name = ('sun','moon','merc','ven','mars','jup','sat','ura','nep','plu','nod','asc','mc')
        sdeg = int(row[position][0:2]) #a row = 04PI45
        ssigh = row[position][2:4]
        smin = int(row[position][4:6])
        return sdeg,ssigh,smin,name[position - 3]
    
    month_to_num = ('jan','feb','mar','apr','may','june','july','aug','sept','oct','nov','dec')
    try:
        #Open csv
        '''open next month file'''
        with open(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.csv') as f:
            csv_f = csv.reader(f)
            for row in csv_f:
                #Get the natal points and note f'{str(day).zfill(2)}' = 22 = btd
                '''if row != [] so when will the planet be in 1 next sign plt_pos(planet_position)[0] == 1'''
                
                if row != [] and plt_pos(planet_position)[0] == 1: #to convert 1 to 01 str(1).zfill(2)
                    '''get the date when that planet has entered 1 next sign'''
                    non_intercept_date = int(row[1][0:2])
                    
    except:
        convert_to_csv(month, yr)
        #Open csv
        with open(f'./ephemeris/{yr}/{yr}_{month_to_num[month]}.csv') as f:
            csv_f = csv.reader(f)
            for row in csv_f:
                #Get the natal points and note f'{str(day).zfill(2)}' = 22 = btd
                '''if row != [] so when will the planet be in 1 next sign plt_pos(planet_position)[0] == 1'''
                
                if row != [] and plt_pos(planet_position)[0] == 1: #to convert 1 to 01 str(1).zfill(2)
                    '''get the date when that planet has entered 1 next sign'''
                    non_intercept_date = int(row[1][0:2])
                
    birth_date = date(yr, month, day)
    non_intercept_date_starts = date(yr, month+1, non_intercept_date)
    delta = non_intercept_date_starts - birth_date
                
    return {'age':delta.days,'year':delta.days + yr}